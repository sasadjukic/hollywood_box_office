

import unittest 
from unittest.mock import MagicMock, patch
from bs4 import BeautifulSoup
from box_office import BoxOfficeMojo, get_headers

class BoxOfficeTest(unittest.TestCase):

    def setUp(self):
        '''Setting up the test with the help of outsourced boxoffice.txt file
           This file helps with mocking the results and is a copy of all 
           the info received from the live scraper'''

        with open('boxoffice.txt', 'r') as file:
            self.boxoffice = file.read()

        '''the actual test (if needed) for BeautifulSoup is some lines below
           but this helps not to repeat lines when mocking the scraper results'''

        soup = BeautifulSoup(self.boxoffice, 'html.parser')
        self.all_headers = soup.select('div h2')
        self.all_titles = soup.select('td', class_='a-link-normal')

    def test_url(self):
        '''make sure we're testing the right link'''

        url = BoxOfficeMojo()
        self.assertEqual(url.__repr__(), 'https://www.boxofficemojo.com/')

    @patch('box_office.requests')
    def test_mock_connection(self, mock_request):
        '''mocking the requests''' 

        mock_response = MagicMock()
        mock_response.status_code = 200

        mock_request = mock_response.status_code
        self.assertEqual(mock_request, 200)

    @patch('box_office.BoxOfficeMojo')
    def test_website_response_text(self, mock_web_text):
        '''mocking the text in response to requests using boxoffice.txt'''

        mock_response = MagicMock()
        mock_response.return_value = self.boxoffice 
        mock_web_text = mock_response.return_value

        self.assertTrue('!doctype' in mock_web_text)

    def test_beautifulsoup(self):
        '''testing BeautifulSoup'''

        soup = BeautifulSoup(self.boxoffice, 'html.parser')
        match = soup.select('div a')
        self.assertEqual(len(match), 155)

    @patch('box_office.BoxOfficeMojo.scrape_all_titles')
    def test_find_all_titles(self, mock_titles):
        '''mocking the scrape_all_titles method'''

        mock_titles = self.all_titles
        self.assertEqual(len(mock_titles), 140)

    @patch('box_office.BoxOfficeMojo.scrape_headers')
    def test_scrape_headers(self, mock_headers):
        '''mocking the scrape_headers method'''

        mock_headers = self.all_headers
        self.assertEqual(len(mock_headers), 5)

    def test_get_headers(self):
        '''testing the get_headers function'''

        self.assertTrue(len(get_headers(self.all_headers)), 5)

    def test_display_daily_boxoffice(self):
        '''mocking the dailies display function
           chose to mock the headers because daily and weekend results 
           can be the same'''

        with patch('box_office.display_daily_boxoffice') as patch_dailies:
            patch_dailies = ['LATEST DAILIES', 'LATEST WEEKEND', 'TOP 2022 MOVIES', 'WORLDWIDE 2022']

            self.assertTrue('LATEST DAILIES' in patch_dailies)

    def test_display_weekend_boxoffice(self):
        '''mocking the weekend boxoffice function'''

        with patch('box_office.display_weekend_boxoffice') as patch_weekends:
            patch_weekends = ['Black Panther', 'Violent Night', 'Strange World', 'The Menu', 'Devotion']

            self.assertTrue('Violent Night' in patch_weekends)

    def test_display_usa_yearly(self):
        '''mocking the USA yearly function'''

        with patch('box_office.display_usa_yearly') as patch_usa:
            patch_usa = ['Top Gun: Maverick', 'Doctor Strange', 'Black Panther', 'Jurrasic World', 'Minions: The Rise of Gru']

            self.assertTrue('Top Gun: Maverick' in patch_usa)

    def test_display_worldwide_yearly(self):
        '''mocking the worldwide function'''

        with patch('box_office.display_worldwide_yearly') as patch_worldwide:
            patch_worldwide = ['Top Gun: Maverick', 'Jurrasic World', 'Doctor Strange', 'Minions: The Rise of Gru', 'Batman']

            self.assertTrue('Batman' in patch_worldwide)

if __name__ == '__main__':
    unittest.main()
