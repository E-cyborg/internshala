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