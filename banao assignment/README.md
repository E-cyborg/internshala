<<<<<<< HEAD
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
=======
# VMware Avi Load Balancer Test Automation Framework

## Overview
This is a Python-based test automation framework designed to interact with a mock VMware Avi Load Balancer API. It serves as a demonstration of robust automation practices, including configuration-driven workflows and parallel execution.

### Key Features
* **Configuration-driven:** Automation logic is decoupled via YAML files.
* **Modular Architecture:** Clean separation of concerns for test structure.
* **Parallel Execution:** Support for concurrent task handling.
* **Mock Connectivity:** Simulated SSH and RDP connections for workflow testing.
* **End-to-End Workflow:** Includes pre-fetching, pre-validation, task execution (disabling a virtual service), and post-validation.

---

## Prerequisites
* **Python:** version 3.8 or higher
* **Package Manager:** pip

---

## Setup

1.  **Clone the Repository**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment**
    Update `config.yaml` with your sandbox credentials:
    ```yaml
    base_url: "[https://semantic-brandea-banao-dc049ed0.koyeb.app](https://semantic-brandea-banao-dc049ed0.koyeb.app)"
    username: "your_username"
    password: "your_password"
    ```

4.  **Define Test Cases**
    Modify `testcases.yaml` to target specific Virtual Services or change the payload:
    ```yaml
    target_vs_name: "backend-vs-t1r_1000-1"
    disable_payload:
      enabled: false
    ```

---

## Usage

Execute the framework by running the main entry point:

```bash
python main.py

Here is the formatted README.md code for your project. I have organized it to be scannable and professional.

Markdown

# VMware Avi Load Balancer Test Automation Framework

## Overview
This is a Python-based test automation framework designed to interact with a mock VMware Avi Load Balancer API. It serves as a demonstration of robust automation practices, including configuration-driven workflows and parallel execution.

### Key Features
* **Configuration-driven:** Automation logic is decoupled via YAML files.
* **Modular Architecture:** Clean separation of concerns for test structure.
* **Parallel Execution:** Support for concurrent task handling.
* **Mock Connectivity:** Simulated SSH and RDP connections for workflow testing.
* **End-to-End Workflow:** Includes pre-fetching, pre-validation, task execution (disabling a virtual service), and post-validation.

---

## Prerequisites
* **Python:** version 3.8 or higher
* **Package Manager:** pip

---

## Setup

1.  **Clone the Repository**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment**
    Update `config.yaml` with your sandbox credentials:
    ```yaml
    base_url: "[https://semantic-brandea-banao-dc049ed0.koyeb.app](https://semantic-brandea-banao-dc049ed0.koyeb.app)"
    username: "your_username"
    password: "your_password"
    ```

4.  **Define Test Cases**
    Modify `testcases.yaml` to target specific Virtual Services or change the payload:
    ```yaml
    target_vs_name: "backend-vs-t1r_1000-1"
    disable_payload:
      enabled: false
    ```

---

## Usage

Execute the framework by running the main entry point:

```bash
python main.py

# Automation Workflow

Upon execution, the framework follows a structured sequence to manage virtual services.

## Execution Steps



1.  **Authentication**: Logs into the mock API and retrieves a session token.
2.  **Discovery**: Pre-fetches tenants, virtual services, and service engines.
3.  **Pre-Validation**: Confirms the target Virtual Service is currently enabled.
4.  **Execution**: Disables the Virtual Service (`enabled: false`).
5.  **Post-Validation**: Verifies that the Virtual Service status is successfully updated to disabled.

---

## Technical Notes

### Mock API Details
* **Base URL**: `https://semantic-brandea-banao-dc049ed0.koyeb.app`
* **Endpoints**: While the root URL (`/`) returns an `OK` status, functional API calls must be directed to specific endpoints (e.g., `/login`).

### Simulated Connections
> [!IMPORTANT]
> SSH and RDP connection steps are **mocked**. This framework simulates these steps for workflow validation and does not establish actual network connections to remote hosts.
>>>>>>> 4ebde82 (completed the work)
