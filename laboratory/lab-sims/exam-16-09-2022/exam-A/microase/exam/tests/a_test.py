import pytest
from exam import app

def test_len(client):
    rv = client.get('/mulstring?a=ciao&n=2')
    print(rv)
    assert rv.status_code == 200
    json = rv.get_json()
    string = json["s"]   
    assert len(string) == 8

def test_invalid_n(client):
    rv = client.get('/mulstring?a=ciao&n=0')
    print(rv)
    assert rv.status_code == 400

def test_invalid_a(client):
    rv = client.get('/mulstring?a=&n=1')
    print(rv)
    assert rv.status_code == 400

