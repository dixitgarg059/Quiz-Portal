import urllib,json
import unittest
from flask import Flask
from flask_testing import LiveServerTestCase 

# Testing with LiveServer
class MyTest(LiveServerTestCase):
    # if the create_app is not implemented NotImplementedError will be raised
    SERVER="http://127.0.0.1:5000/"
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8080
        return app 
    def test_path(self):
        urls=["","intro","theory","objective","experiment","feedback","quiz","procedure"]
        for i in range(8):
            response = urllib.request.urlopen(self.SERVER+urls[i])
            self.assertEqual(response.code, 200)
    
    def test_name(self):
        url="check"
        da = {'Q1':'1', 'Q2': '2','Q3':'3','Q4':'4','Q5':'5'}
        da=urllib.parse.urlencode(da).encode()
        r = urllib.request.Request(self.SERVER+url, data=da)
        req=urllib.request.urlopen(r)
        data = json.loads(req.read().decode())

        self.assertEqual(data['status'],'1')
    def test_name1(self):
        url="check1"
        da={'Q1':'1','Q2':'2','Q3':'3'}
        da=urllib.parse.urlencode(da).encode()
        r = urllib.request.Request(self.SERVER+url, data=da)
        req=urllib.request.urlopen(r)
        data = json.loads(req.read().decode())

        self.assertEqual(data['status'],'1')
    def test_name2(self):
        url="check2"
        da={'P1':'1','P2':'2'}
        da=urllib.parse.urlencode(da).encode()
        r = urllib.request.Request(self.SERVER+url, data=da)
        req=urllib.request.urlopen(r)
        data = json.loads(req.read().decode())

        self.assertEqual(data['status'],'1')

if __name__ == '__main__':
    unittest.main()