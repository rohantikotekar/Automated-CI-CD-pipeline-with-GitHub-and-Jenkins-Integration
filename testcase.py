import unittest
import requests

class WebsiteLoadTest(unittest.TestCase):
    def test_website_loads(self):
        print("Sending a GET request to the website.")
        response = requests.get('https://atg.world')

        print("Checking if the website loaded properly.")
        self.assertEqual(response.status_code, 200, 'Website did not load properly. Hi. ')

        if response.status_code == 200:
            print("Website is running. hihi ")

if __name__ == '__main__':
    unittest.main()
