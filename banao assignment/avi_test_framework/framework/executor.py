#  i use chatgpt for only this file

def pre_fetch(api_client):
    print("Pre-fetching data...")

    tenants = api_client.get("/api/tenant")
    print("Tenants count:", len(tenants["results"]))

    virtual_services = api_client.get("/api/virtualservice")
    print("Virtual Services count:", len(virtual_services["results"]))

    service_engines = api_client.get("/api/serviceengine")
    print("Service Engines count:", len(service_engines["results"]))

    return virtual_services["results"]


def get_vs_by_name(vs_list, vs_name):
    for vs in vs_list:
        if vs["name"] == vs_name:
            return vs

    print("Virtual Service not found!")
    return None
