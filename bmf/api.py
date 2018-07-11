from contextlib import contextmanager
from requests import Session

def _create_session(bmf_addr, user, password, verify, proxies):
    s = Session()
    s.api_url = "https://{}:8443/api/v1".format(bmf_addr)
    s.verify = verify
    s.headers.update({'Content-type':'application/json'})
    s.proxies=proxies
    s.post(s.api_url + "/auth/login", json={'user': user, 'password': password})
    return s

def _logout(session):
    r = session.delete(session.api_url + '/data/controller/core/aaa/session[auth-token="{}"]'.format(session.cookies['session_cookie']))

@contextmanager
def bmfsession(bmf_addr, user, password, verify=True, proxies=None):
    session = _create_session(bmf_addr, user, password, verify, proxies)
    yield session
    _logout(session)

def get(session, endpoint):
    return session.get(session.api_url + endpoint).json()
