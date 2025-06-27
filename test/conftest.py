import pytest
from fixture._application import Application

fixture = None

@pytest.fixture ()
def app(request):
    global fixture
    if fixture is Null:
        fixture = Application()
        fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
                fixture = Application()
                fixture.session.login(username="admin", password="secret")
    return fixture

@pytest.fixture (scope="session", autouse = True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.session.destroy()
    request.addfinalizer(fin)
    return fixture