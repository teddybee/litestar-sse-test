import logging
import unittest
from litestar.testing import TestClient
from litestar.status_codes import HTTP_200_OK

from api.app import app

# https://docs.litestar.dev/2/usage/testing.html

logger = logging.getLogger(__name__)
logger.level = logging.DEBUG

class TestHttp(unittest.TestCase):  

    # def setUp(self):
    # runs before every testcase
    # logger.info("setup")
    
    def test_root_query(self):
      with TestClient(app=app) as client:
        assert client.get("/").status_code == 200
    
    def test_health_query(self):
      with TestClient(app=app) as client:     
        response = client.get("/health")        
        assert response.status_code == HTTP_200_OK
        assert response.text == '{"status":"ok"}'
        #assert client.post("/", json={"name": "xxx", "param": {"coord": {"x": 10, "y": 10}}}).status_code == 201