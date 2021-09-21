import pytest
from pages.mls.search_mls_container import SearchMlsContainer


@pytest.fixture()
def mls_setup(setup, config):
    search_mls_container = SearchMlsContainer(setup)
    search_mls_container.open_home_page(config)
    search_mls_container.close_select_city_modal()
    search_mls_container.wait_mapbox_loaded()

