from framework.executor import pre_fetch, get_vs_by_name

def run_test(api_client, testcase):
    print(f"Running test: {testcase['name']}")

    # Pre-fetch required objects
    vs_list = pre_fetch(api_client)

    # Identify target Virtual Service
    target_vs = get_vs_by_name(vs_list, testcase["target_vs_name"])
    uuid = target_vs["uuid"]

    # Pre-validation
    vs_details = api_client.get(f"/api/virtualservice/{uuid}")
    if not vs_details["enabled"]:
        raise Exception("Virtual Service is already disabled")

    # Disable Virtual Service
    api_client.put(
        f"/api/virtualservice/{uuid}",
        testcase["action"]["payload"]
    )

    # Post-validation
    vs_details = api_client.get(f"/api/virtualservice/{uuid}")
    if vs_details["enabled"]:
        raise Exception("Failed to disable Virtual Service")

    print("Test passed")
