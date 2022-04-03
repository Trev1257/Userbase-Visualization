# Userbase-Visualization
The app visualises userbase growth by drawing graphs on the terminal. The app makes use of: Python Argparse library to build the command line interface using the date flags, the Python Datetime library to dictate the date format with which the users need to enter when running the app, Python Requests for accessing userbase data from the API endpoint, as well as the Python plotext library for drawing the graphs on the terminal.
For the app to work, one needs to create a virtual environment and then install the Python libraries: Argparse, Requests, Plotext, Json, and Datetime.
When using the app, it has a help-menu which has instructions on how the app works. The user can type '-h', and the app outputs the instructions on how to proceed. For instance, the help-menu outputs a message the to instruct the user to pick a date from the earliest date to latest date in the specified format.
The app first accesses the data from the specified API endpoint. From the endpoint, the app identifies the earliest date as well as the latest date and then proceeds to make a custom range using these dates.
When the user inputs the help-menu, the app will then tell the user to enter two dates: the startdate and the enddate based upon the data from the API endpoint.
The app has flags 'startdate' and 'enddate', and these flags(arguments) are mandatory as users are required to input them for the app to function well.
Users are required to enter the dates in the format YYYY-MM-DD, that is to say, the year first, followed by the month, and lastly the day.
If users input the wrong format, the app outputs the error message. If the user inputs the start date as well as the end date in the correct format (YYYY-MM-DD), followed by the ENTER key, the app will draw the user base graph on the terminal with number of users on the x-axis while the dates will be on the y-axis.

