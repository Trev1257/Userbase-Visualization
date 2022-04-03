import argparse
from datetime import datetime
import requests
import plotext as plt
import json


# Accessing the data from the end-point API
def read():
    end_point_url = 'http://sam-user-activity.eu-west-1.elasticbeanstalk.com/'
    access = requests.get(end_point_url)
    data = access.json()
    low = min(data.keys())
    high = max(data.keys())

    # changing the formats of the earliest and latest days
    low = datetime.strptime(low, "%d-%m-%Y")
    earliest = low.strftime('%d %B %Y')

    high = datetime.strptime(high, "%d-%m-%Y")
    latest = high.strftime('%d %B %Y')
    return data, earliest, latest

# Inputting the correct format to read on terminal
def valid_date(s):
    try:
        ms=datetime.strptime(s, "%Y-%m-%d")
        return ms.strftime('%d-%m-%Y')
    except ValueError:
        msg = "not a valid date: {0!r}".format(s)
        raise argparse.ArgumentTypeError(msg)


#setting the flags(arguments)
def arguments(data, earliest, latest):
    parser = argparse.ArgumentParser(description = f'This application draws graphs on the terminal for the range between {earliest} and {latest}',
    epilog='Enjoy the program!')

    parser.add_argument('-s', "--startdate",
                    action = "store",
                    help="The Start Date => format YYYY-MM-DD",
                    required=True,
                    type=valid_date)

    parser.add_argument('-e', "--enddate",
                    action = "store",
                    help="The End Date => format YYYY-MM-DD",
                    required=True,
                    type=valid_date)

    flags = parser.parse_args()
    a,b = flags.startdate, flags.enddate

    new_data = {key:value for key,value in data.items() if key >= a and key <= b}

    return new_data, a,b
        

# plotting on the graph
def plot_on_terminal(new_data,a,b):
    plt.bar(new_data.keys(), new_data.values(),orientation='h', width=0.3)
    plt.title("Userbase Growth")
    plt.xlabel("Number of Users")
    plt.ylabel("Date")
    plt.show()
    return plt.show
    
if __name__ == '__main__':
    initial = read()
    second = arguments(*initial)
    third = plot_on_terminal(*second)




   



