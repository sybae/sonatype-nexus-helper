import properties
import requests

api_url_search = ''
api_url_components = ''
component_ids = []


# Init API URL - search
def init_api_url_search():
    global api_url_search
    global api_url_components
    api_url_search = properties.get_api_search_without_version()
    api_url_components = properties.get_api_components()


# Search component by range and collect them
def search_components_by_range(range_by_number):
    for version in range_by_number:
        url = api_url_search + str(version)
        print(f'[GET] {url} - RUNNING...')

        resp = requests.get(url)
        json = resp.json()
        items = json['items']
        if not items:
            continue

        parse_json_into_component(json)


# Search component by version
def search_component_by_version(version):
    url = api_url_search + version
    print(f'[GET] {url} - RUNNING...')

    resp = requests.get(url)
    json = resp.json()
    parse_json_into_component(json)


# Parse JSON into component
def parse_json_into_component(json):
    items = json['items']
    component = items[0]

    # Some cookies
    component_id = component['id']
    component_repository = component['repository']
    component_group = component['group']
    component_name = component['name']
    component_version = component['version']
    print(f'..... {component_repository} | {component_group}:{component_name}:{component_version} | {component_id}')

    component_ids.append(component_id)


# Components delete from collected ids
def components_delete():
    url = api_url_components + '/'
    for component_id in component_ids:
        print(f'[DELETE] /v1/components/{component_id} - RUNNING...')
        resp = requests.delete(url + component_id, auth=properties.NEXUS_AUTH)
        print(f'........ {resp.status_code} / {resp.headers} / {resp.reason}')
