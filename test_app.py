from app import get_services, add_services
import json 
import requests

TEST_URL="http://127.0.0.1:5000/api/services"

def test_get_services():
    services=json.loads(get_services())["services"]
    length=json.loads(get_services())["length"]
    assert len(services)==length and (services is not None or length is not None)

def test_add_services():
    test_data = ["service1", "service2", "service3"]
    response = requests.post(url=TEST_URL, json={"services": test_data})
    if response.status_code == 200:
        result = response.json()
        assert result["status"] == "ok"
        assert result["length"] == len(test_data)
    else:
        assert False, f"Failed with status code {response.status_code}"
  
      