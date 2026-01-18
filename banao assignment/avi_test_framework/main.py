import yaml
from framework.api_client import APIClient
from tests.disable_vs_test import run_test
from concurrent.futures import ThreadPoolExecutor

# Load config
with open("config.yaml") as f:
    config = yaml.safe_load(f)

# Load testcases
with open("testcases.yaml") as f:
    testcases = yaml.safe_load(f)

# Initialize API client and login
client = APIClient(
    base_url=config["base_url"],
    username=config["username"],
    password=config["password"]
)
client.login()

# Run tests in parallel
with ThreadPoolExecutor(max_workers=2) as executor:
    futures = []
    for tc in [testcases]:  # can expand to multiple tests
        futures.append(executor.submit(run_test, client, tc))

    # Wait for completion
    for future in futures:
        future.result()

print("All tests completed ✅")
