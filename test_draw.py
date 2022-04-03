import argparse
from ast import arguments
from datetime import datetime
import requests
import plotext as plt
import json
import unittest
from unittest.mock import patch
from unittest import mock
from draw import plot_on_terminal
from unittest.mock import patch, mock_open
import draw


class TestDraw(unittest.TestCase):
    #testing if the status code for the API endpoint is okay
    def test_read(self):
        end_point_url = 'http://sam-user-activity.eu-west-1.elasticbeanstalk.com/'
        access = requests.get(end_point_url)
        data = access.json()
        self.assertEqual(access.status_code, 200)
        

    # testing the earliest date
    def test_read_1(self):
        end_point_url = 'http://sam-user-activity.eu-west-1.elasticbeanstalk.com/'
        access = requests.get(end_point_url)
        data = access.json()
        earliest = min(data.keys())
        assert earliest == '01-01-2022'

    # testing the latest date
    def test_read_2(self):
        end_point_url = 'http://sam-user-activity.eu-west-1.elasticbeanstalk.com/'
        access = requests.get(end_point_url)
        data = access.json()
        latest = max(data.keys())
        assert latest == '15-01-2022'


    # testing the data
    def test_read_3(self):
        end_point_url = 'http://sam-user-activity.eu-west-1.elasticbeanstalk.com/'
        access = requests.get(end_point_url)
        data = access.json()
        actual_data = {
            '01-01-2022':300, '02-01-2022':500, '03-01-2022':700, '04-01-2022':1300, '05-01-2022':2000,
            '06-01-2022':3000, '07-01-2022':3500, '08-01-2022':4000, '09-01-2022':4500, '10-01-2022':5000,
            '11-01-2022':20000, '12-01-2022':35000, '13-01-2022':46000, '14-01-2022':70000, '15-01-2022':90000
        }
        
        assert data == actual_data


    # testing the format of the data
    def test_valid_dates_2(self):
        ms=datetime.strptime('2022-01-01', "%Y-%m-%d")
        ms.strftime('%d-%m-%Y')
        self.assertRaises(argparse.ArgumentTypeError, draw.valid_date, '01-01-2022')

        


    # testing the date format
    def test_valid_date(self):
        ms=datetime.strptime('2022-01-01', "%Y-%m-%d")
        new = ms.strftime('%d-%m-%Y')
        assert new == '01-01-2022'

    #testing the flags
    @mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(accumulate=sum, integers=[1,2,3]))
    def test_arguments(mock_args, autospec=True):
        data={'01-01-2022':300,'02-01-2022':500,'03-01-2022':700}
        earliest = '01-01-2022'
        latest ='03-01-2022'
        result = arguments(data, earliest, latest)
        assert result != None

        

    #testing the graph
    @patch("draw.plt.show")
    def test_plot_on_terminal(mock_show, autospec=True):
        new_data={'01-01-2022':300,'02-01-2022':500,'03-01-2022':700}
        a= '01-01-2022'
        b='03-01-2022' 
        assert plot_on_terminal(new_data,a,b) != None


   
        
          



if __name__ == '__main__':
    unittest.main()