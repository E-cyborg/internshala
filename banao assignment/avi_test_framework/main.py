import yaml
from framework.api_client import API_CLIENT
from tests.disable_vs_test import run_test
from concurrent.futures import ThreadPoolExecutor

# Load config
with open("avi_test_framework/config/config.yaml") as f:
    config = yaml.safe_load(f)
    controller = config["controller"]
# Load testcases
with open("avi_test_framework/config/testcases.yaml") as f:
    testcases = yaml.safe_load(f)

# Initialize API client and login
client = API_CLIENT(
    base_url=controller["base_url"],
    username=controller["username"],
    password=controller["password"]
)
client.login()

# Run tests in parallel
with ThreadPoolExecutor(max_workers=2) as executor:
    futures = []
    for tc in testcases["testcases"]:
        futures.append(executor.submit(run_test, client, tc))

    # Wait for completion
    for future in futures:
        future.result()

print("All tests completed ✅")
