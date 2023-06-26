import json
import pytest
from examOne import app

def test_dice_len(client):
    rv = client.get('/dice?k=4&n=6')
    print(rv)
    assert rv.status_code == 200
    json_list = rv.get_json()
    list = json_list["s"]
    assert len(list) == 4

def test_dice_invalid(client):
    rv = client.get('/dice?k=&n=')
    print(rv)
    assert rv.status_code == 400

def test_dice_ranges(client):
    rv = client.get('/dice?k=4&n=6')
    print(rv)
    assert rv.status_code == 200
    json_list = rv.get_json()
    list = json_list["s"]

    for i in range(len(list)):
        assert  list[i] >= 1 and list[i] <= 6 
