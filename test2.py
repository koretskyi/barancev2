import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_test(app):
    app.login_buy()
    app.fill_form(Group(username="test", phone="+380 (11) 111-11-11", mail="test@test.com"))

def test_empty_test(app):
    app.login_buy()
    app.fill_form(Group(username="", phone="", mail=""))


