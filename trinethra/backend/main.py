from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import requests
import json
import os

app = FastAPI(title="Trinethra — Supervisor Feedback Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

# Load rubric and sample transcripts at startup
BASE_DIR = os.path.dirname(__file__)

with open(os.path.join(BASE_DIR, "rubric.json"), "r") as f:
    RUBRIC = json.load(f)

with open(os.path.join(BASE_DIR, "transcript.json"), "r") as f:
    SAMPLE_TRANSCRIPTS = json.load(f)


class TranscriptRequest(BaseModel):
    transcript: str


def call_ollama(prompt: str) -> str:
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0.1,
            "top_p": 0.9,
            "num_predict": 2000,
            "repeat_penalty": 1.1,
        },
    }
    response = requests.post(OLLAMA_URL, json=payload, timeout=180)
    response.raise_for_status()
    data = response.json()
    if "response" not in data:
        raise ValueError("Invalid Ollama response")
    return data["response"]


def extract_json(text: str):
    try:
        return json.loads(text)
    except Exception:
        pass
    decoder = json.JSONDecoder()
    for i, char in enumerate(text):
        if char == "{":
            try:
                obj, _ = decoder.raw_decode(text[i:])
                return obj
            except Exception:
                continue
    return None


def build_prompt(transcript: str) -> str:
    # Inject actual rubric levels from rubric.json
    rubric_levels = []
    for band in RUBRIC["rubric"]["bands"]:
        for level in band["levels"]:
            rubric_levels.append(
                f"  Score {level['score']} ({level['label']}): {level['description']} | Signals: {', '.join(level['signals'])}"
            )
    rubric_text = "\n".join(rubric_levels)

    # Inject KPI definitions
    kpi_text = "\n".join(
        [f"  - {k['label']}: {k['description']}" for k in RUBRIC["kpis"]]
    )

    # Inject assessment dimensions
    dim_text = "\n".join(
        [f"  - {d['label']} ({d['id']}): {d['description']}" for d in RUBRIC["assessmentDimensions"]]
    )

    critical = RUBRIC["rubric"]["criticalBoundary"]

    return f"""
You are a performance evaluator for DT Fellows placed inside Indian manufacturing companies.
Evaluate ONLY using evidence explicitly stated in the transcript. Do not infer.

SCORING RUBRIC (use these exact levels):
{rubric_text}

CRITICAL BOUNDARY — {critical['boundary']}:
{critical['description']}
- Score 6 example: "{critical['score6Example']}"
- Score 7 example: "{critical['score7Example']}"

ASSESSMENT DIMENSIONS (check all 4 — missing ones become gaps):
{dim_text}

KPIs TO MAP (supervisors use plain language, map to these):
{kpi_text}

HARD SCORING GATES:
- Score > 6 REQUIRES proactive problem identification (not just execution)
- Score > 7 REQUIRES evidence of SOPs, trackers, or repeatable systems others can follow
- Score > 8 REQUIRES measurable business impact OR adoption by others

BIAS CHECKS — watch for these traps:
1. Helpfulness bias: "takes work off my plate" = task absorption, NOT systems building
2. Presence bias: "always on the floor" ≠ high score
3. Dependency trap: if Fellow left tomorrow and everything stops = cap at 5-6
4. Hero story trap: one crisis response ≠ repeatable improvement
5. Recency bias: one recent win ≠ sustained performance

BEFORE SCORING, ANSWER INTERNALLY:
1. If this Fellow left tomorrow, would any system keep running without them?
2. Is the supervisor praising the PERSON or praising SYSTEMS they built?
3. Is "taking work off my plate" = systems building or task absorption?

If answer to Q1 is NO → score must be 5-6 maximum.
If supervisor praises person not systems → score must be 5-6 maximum.

TRANSCRIPT TO ANALYZE:
{transcript}

Return ONLY this JSON structure, no extra text:
{{
  "score": {{
    "value": <integer 1-10>,
    "label": "<exact label from rubric>",
    "band": "<Need Attention|Productivity|Performance>",
    "justification": "<2-3 sentences citing specific transcript evidence>",
    "confidence": "<low|medium|high>"
  }},
  "evidence": [
    {{
      "quote": "<exact verbatim quote from transcript>",
      "signal": "<positive|negative|neutral>",
      "dimension": "<execution|systems_building|kpi_impact|change_management>",
      "interpretation": "<why this quote matters for scoring>"
    }}
  ],
  "kpiMapping": [
    {{
      "kpi": "<kpi label>",
      "evidence": "<what supervisor said that maps to this KPI>",
      "systemOrPersonal": "<system|personal>"
    }}
  ],
  "gaps": [
    {{
      "dimension": "<dimension id>",
      "detail": "<what was NOT mentioned and why it matters>"
    }}
  ],
  "followUpQuestions": [
    {{
      "question": "<specific question for next call>",
      "targetGap": "<dimension id>",
      "lookingFor": "<what answer would reveal>"
    }}
  ]
}}
"""


@app.post("/analyze")
async def analyze(request: TranscriptRequest):
    transcript = request.transcript.strip()
    if not transcript:
        return {"success": False, "error": "Transcript cannot be empty"}

    try:
        prompt = build_prompt(transcript)
        raw_response = call_ollama(prompt)
        parsed = extract_json(raw_response)

        if not parsed:
            return {
                "success": False,
                "error": "Could not parse model response. Try again.",
                "raw": raw_response[:2000],
            }

        return {"success": True, "data": parsed}

    except requests.exceptions.ConnectionError:
        return {
            "success": False,
            "error": "Cannot connect to Ollama. Make sure it is running: ollama serve",
        }
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "Ollama timed out. Try a smaller model or shorter transcript.",
        }
    except Exception as e:
        return {"success": False, "error": str(e)}


@app.get("/health")
async def health():
    return {"status": "ok", "model": MODEL, "rubric_loaded": True, "kpis": len(RUBRIC["kpis"])}


@app.get("/samples")
async def get_samples():
    """Return sample transcript IDs and fellow names for the frontend dropdown."""
    return {
        "samples": [
            {
                "id": t["id"],
                "fellow": t["fellow"]["name"],
                "company": t["company"]["name"],
                "transcript": t["transcript"],
            }
            for t in SAMPLE_TRANSCRIPTS["transcripts"]
        ]
    }


# Serve frontend
frontend_dir = os.path.join(os.path.dirname(__file__), "..", "frontend")
if os.path.exists(frontend_dir):
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")