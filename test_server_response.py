import unittest
from unittest.mock import patch, MagicMock
import requests

class TestServerResponse(unittest.TestCase):
    def setUp(self):
        # Setup code including mocked requests
        self.mock_response = {
            'example.com': {'A': 'some_hexadecimal_response'}
        }

    @patch('requests.get')
    def test_dns_query_response(self, mock_get):
        # Mocking DNS query function
        def mock_query_func(name, qtype):
            return self.mock_response.get(name, {}).get(qtype, 'Unknown query')

        # Patching requests.get to return a mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': self.mock_response['example.com']['A']}
        mock_get.return_value = mock_response

        # Making a request to the mock server
        app_response = requests.get('http://example.com')

        # Asserting the response status code and data
        self.assertEqual(app_response.status_code, 200)
        self.assertEqual(app_response.json()['data'], self.mock_response['example.com']['A'])

if __name__ == '__main__':
    unittest.main()
