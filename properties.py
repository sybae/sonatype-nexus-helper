NEXUS = 'http://nexus/'
NEXUS_AUTH = ('id', 'pw')
NEXUS_REST_V1 = {
    'base': 'service/rest/v1/',
    'search': 'search?',
    'components': 'components'
}

search_conditions = {
    'repository': 'hello-releases',
    'group': 'com.world',
    'name': 'something-special'
    # 'version': '99999'
}


# Get API - http://nexus/service/rest/v1/
def get_api():
    return NEXUS + NEXUS_REST_V1['base']


# Get API Search without version
def get_api_search_without_version():
    return get_api() \
           + NEXUS_REST_V1['search'] \
           + f'repository={search_conditions["repository"]}' \
           + f'&group={search_conditions["group"]}' \
           + f'&name={search_conditions["name"]}' \
           + f'&version='


# Get API Components
def get_api_components():
    return get_api() \
           + NEXUS_REST_V1['components']
