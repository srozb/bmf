from contextlib import contextmanager
from requests import Session

def _create_session(bmf_addr, user, password, verify, proxies):
    s = Session()
    s.bmf_addr = bmf_addr
    s.api_url = "https://{}:8443/api/v1/data/controller".format(bmf_addr)
    s.verify = verify
    s.headers.update({'Content-type':'application/json'})
    s.proxies=proxies
    return s

def _login(session, user, password):
    r = session.post("https://{}:8443/api/v1/auth/login".format(session.bmf_addr), json={'user': user, 'password': password})
    if not r.json()['success']:
        raise ValueError(r.json()['error_message'])

def _logout(session):
    delete(session, '/core/aaa/session[auth-token="{}"]'.format(session.cookies['session_cookie']))

@contextmanager
def bmfsession(bmf_addr, user, password, verify=True, proxies=None):
    session = _create_session(bmf_addr, user, password, verify, proxies)
    _login(session, user, password)
    yield session
    _logout(session)

def get(session, endpoint):
    return session.get(session.api_url + endpoint).json()

def post(session, endpoint, data):
    r = session.post(session.api_url + endpoint, json=data)
    if not r.ok:
        raise RuntimeError(r.json()['description'])

def delete(session, endpoint):
    r = session.delete(session.api_url + endpoint)
    if not r.ok:
        raise RuntimeError(r.json()['description'])

