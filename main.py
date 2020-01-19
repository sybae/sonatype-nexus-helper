import search_and_delete_component as sd

# Search and Delete Components
def search_and_delete_components():
    sd.init_api_url_search()
    sd.search_components_by_range(range(10000, 10999))
    # sd.search_component_by_version('0.0.1')
    sd.components_delete()


def main():
    search_and_delete_components()


if __name__ == '__main__':
    main()