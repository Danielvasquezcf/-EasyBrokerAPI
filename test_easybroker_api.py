import pytest
from easybroker_api import EasyBrokerAPI

@pytest.fixture
def api():
    api_key = 'l7u502p8v46ba3ppgvj5y2aad50lb9'
    return EasyBrokerAPI(api_key)

def test_get_contact_requests(api):
    response = api.get_contact_requests()
    assert 'content' in response

def test_print_contact_request_titles(api, capsys):
    api.print_contact_request_titles()
    captured = capsys.readouterr()

    contact_requests = api.get_contact_requests()
    
    if 'content' in contact_requests:
        titles = [request.get('title') for request in contact_requests['content']]
        for title in titles:
            if title is not None:
                assert isinstance(title, str)
                assert title in captured.out
    else:
        assert 'No contact requests available' in captured.out
