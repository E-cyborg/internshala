cd ~/Desktop/Code/trinethra
cat > backend/README.md << 'ENDOFFILE'
# Trinethra — Supervisor Feedback Analyzer

AI-assisted analysis tool for DT Psychology Interns to process supervisor transcripts faster.

## What It Does

Paste a supervisor transcript, get a structured draft analysis in ~60 seconds:
- Rubric score (1-10) with justification
- Extracted evidence quotes tagged positive/negative/neutral
- KPI mapping to 8 business outcomes
- Gap analysis (what the transcript did not cover)
- Follow-up questions for the next call

The AI suggests. The intern decides.

## Setup

1. Install Ollama and pull the model

    curl -fsSL https://ollama.com/install.sh | sh
    ollama pull llama3.2
    ollama serve

2. Install Python dependencies

    cd backend
    pip install fastapi uvicorn requests pydantic

3. Start the backend

    cd backend
    uvicorn main:app --reload

4. Open the app at http://localhost:8000

## Model Choice

Used llama3.2 (3B parameters). Reasons:
- Runs on most laptops with 8GB RAM
- Fast enough for 60-second turnaround on transcript-length inputs
- Reliable JSON output with format=json mode
- Low hallucination on structured tasks

## Architecture

Browser (index.html) sends POST /analyze with transcript to FastAPI backend (main.py). The backend loads rubric.json and transcript.json at startup, injects real rubric data into the prompt, then sends POST to http://localhost:11434/api/generate. Ollama runs llama3.2 locally, returns JSON, which the backend parses and returns to the frontend for the intern to review.

## Design Challenges Tackled

Challenge 1 - One Prompt vs Many: Chose one prompt for MVP. A 10-15 minute transcript is short enough that a single well-structured prompt produces consistent output. Multiple prompts would be slower and harder to coordinate. Tradeoff: prompt is long but clearly sectioned.

Challenge 2 - Structured Output Reliability: Used Ollama format=json mode to force JSON output. Added fallback extract_json() that scans for the first { and attempts parsing from there, handling cases where the model adds preamble text. Temperature set to 0.1 for consistency.

Challenge 4 - Showing Uncertainty: Added a prominent draft notice at the top of every analysis. Confidence field shown on every score. Intern is always reminded they are reviewing, not accepting.

Challenge 5 - Gap Detection: Prompt explicitly lists all 4 assessment dimensions and instructs the model to identify which ones are absent. Reframes gap detection as checking for presence of each dimension rather than open-ended reasoning about absence.

## What I Would Improve With More Time

1. Side-by-side view: transcript on left, analysis on right. Clicking an evidence quote highlights the source text in the transcript.
2. Edit and finalize flow: intern edits score and justification inline, exports a finalized PDF report.
3. Multi-prompt pipeline: separate Ollama calls for scoring, gap detection, and follow-up questions. Better quality, easier to retry individual sections.
4. Confidence calibration: validate all 3 sample transcripts against expected score ranges before shipping.
ENDOFFILE