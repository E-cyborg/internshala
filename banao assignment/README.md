# VMware Avi Load Balancer Test Automation Framework

## Overview
A small Python-based test automation framework that interacts with a mock VMware Avi Load Balancer API.  
It demonstrates configuration-driven automation, a modular structure, mock connectivity (SSH/RDP), and parallel execution of tests. The provided example test disables a Virtual Service named `backend-vs-t1r_1000-1`.

## Key Features
- Configuration-driven with YAML files.
- Modular architecture (framework, tests, utils).
- Parallel execution using ThreadPoolExecutor.
- Mocked SSH/RDP connectors for workflow validation.
- End-to-end workflow: pre-fetch, pre-validation, action (PUT), post-validation.

## Prerequisites
- Python 3.8+
- pip

Recommended packages (add to `requirements.txt`):
```text
requests
PyYAML
```

## Repository structure
```
avi_test_framework/
├── config/
│   ├── config.yaml         # Controller credentials and endpoints
│   └── testcases.yaml      # Test cases
├── framework/
│   ├── api_client.py       # API client (login/get/put)
│   ├── executor.py         # Pre-fetch helpers
│   ├── mock_connectors.py  # MOCK_SSH / MOCK_RDP
│   └── utils.py            # YAML loader, helpers
├── tests/
│   └── disable_vs_test.py  # Example test implementation
├── main.py                 # Test runner
├── requirements.txt
└── README.md
```

## Configuration
All configuration is in `config/config.yaml` and testcases in `config/testcases.yaml`.

Example `config/config.yaml`:
```yaml
controller:
  base_url: "https://semantic-brandea-banao-dc049ed0.koyeb.app"
  username: "your_username"
  password: "your_password"
  # Some sandboxes use /login1 instead of /login — change if required:
  login_path: "/login"

headers:
  content_type: "application/json"
```

Example `config/testcases.yaml`:
```yaml
testcases:
  - name: disable_backend_vs
    description: "Disable Virtual Service backend-vs-t1r_1000-1"
    target_vs_name: "backend-vs-t1r_1000-1"
    pre_validation:
      method: GET
      expected:
        enabled: true
    action:
      method: PUT
      payload:
        enabled: false
    post_validation:
      method: GET
      expected:
        enabled: false
```

## Registration and Login (mock API sandbox)
Each user has an isolated sandbox. You must register and then login to obtain a token.

Register (curl):
```bash
curl -X POST "https://semantic-brandea-banao-dc049ed0.koyeb.app/register" \
  -H "Content-Type: application/json" \
  -d '{"username":"your_username","password":"your_password"}'
```

Login (curl) — Basic Auth:
```bash
curl -X POST "https://semantic-brandea-banao-dc049ed0.koyeb.app/login" \
  -u "your_username:your_password" \
  -H "Content-Type: application/json"
```
Note: Some sandboxes use `/login1` — if your login returns 404, try `/login1`. The login response should contain a `token`:
```json
{ "token": "a1b2c3d4-e5f6-7890-1234-567890abcdef" }
```

Use the token as a Bearer token in subsequent API calls:
```
Authorization: Bearer <token>
```

## How the test flow works
For each testcase the framework performs (in order):
1. Pre-Fetch: GET `/api/tenant`, `/api/virtualservice`, `/api/serviceengine` — logs counts.
2. Pre-Validation: GET `/api/virtualservice/<uuid>` and ensure `"enabled": true`.
3. Task/Trigger: PUT `/api/virtualservice/<uuid>` with payload `{"enabled": false}`.
4. Post-Validation: GET `/api/virtualservice/<uuid>` and verify `"enabled": false`.

The example test targets `backend-vs-t1r_1000-1`. The framework looks up the VS by name to get its UUID before making per-VS calls.

## Running the framework
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Update `config/config.yaml` with your `base_url`, `username`, `password`, and `login_path` (if different).

3. Ensure `config/testcases.yaml` contains the tests you wish to run.

4. Execute:
```bash
python main.py
```
Tests will run in parallel (configurable via ThreadPoolExecutor in `main.py`). Output and exceptions will print to console.

## Notes & Troubleshooting
- File locations: `config/config.yaml` and `config/testcases.yaml` must be present relative to the repository root.
- If you receive 401/403 on GET/PUT calls, ensure you registered and logged in successfully and that the `token` is set in the Authorization header. Check the `login_path` in config if you get unexpected login errors.
- If the Virtual Service is not found by name, confirm the `target_vs_name` in `testcases.yaml` matches a VS in your sandbox.
- The framework includes mock connectors (`MOCK_SSH` / `MOCK_RDP`) — these are placeholders and do not open real connections.
- Review `framework/api_client.py` and ensure the login endpoint and paths align with the sandbox behavior. The client uses Bearer tokens for subsequent API calls.

## Deliverables checklist
- Python source code (.py files) — present in `framework/` and `tests/`.
- YAML configuration files — `config/config.yaml`, `config/testcases.yaml`.
- `requirements.txt` — add `requests` and `PyYAML` if not already present.
- README.md — this file.

## Further improvements (suggested)
- Add a dry-run or non-destructive mode to validate config and endpoints without performing PUTs.
- Add logging (instead of prints) and more granular error handling.
- Add automated registration helper (if the sandbox API allows).
- Add unit/integration tests for the API client (mocked responses).

---

If you want, I can:
- Generate a polished `requirements.txt`.
- Prepare an updated `config/config.yaml` sample file with `login_path` set to `/login1` for testing.
- Produce a small script that performs registration, login, and prints the token for you to paste into config. Which would you prefer?
