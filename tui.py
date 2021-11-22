"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""


def welcome():
    welcome_message = "COVID-19 (january) Data"
    # Courts number of characters in welcome message
    num_dashes = len(welcome_message) * "-"

    print(f"{num_dashes}\n{welcome_message}\n{num_dashes}")


def error(msg):
    print(f"Error! '{'{msg}'}'.")


def progress(operation, value):
    status = ""
    if operation != "":
        if value == 0:
            status = "has started"
        elif value > 0 & value < 100:
            status = f"is in progress ({value}% completed)"
        elif value == 100:
            status = "has completed"
    else:
        error("Operation in not recognized")

    if status != "":
        # Capitalizes first letter in string parameter before printing
        operation.capitalize()
        print(f"{operation}: {status}")


def menu(variant=0):
    """
    Task 4: Display a menu of options and read the user's response.
    If no value or a zero is supplied for the parameter 'variant' then a menu with the following options
    If the value of the parameter 'variant' is 1 then a menu with the following options should be displayed:
    If the value of the parameter 'variant' is 2 then a menu with the following options should be displayed:
    If the value of the parameter 'variant' is 3 then a menu with the following options should be displayed:
    In each of the above cases, the user's response should be read in and returned as an integer
    corresponding to the selected option.
    E.g. 1 for 'Process Data', 2 for 'Visualise Data' and so on.
    If the user enters a invalid option then a suitable error message should be displayed
    :return: nothing if invalid selection otherwise an integer for a valid selection
    """
    # A while loop seems most appropriate here to ensure correct selection has been made in case of invalid selection
    # Took a while to
    has_selected = False
    user_input = 0

    while not has_selected:

        if variant is None or variant == 0:
            user_input = int(input("[1] Process Data\n[2] Visualise Data\n[3] Export Data\n[4] Exit"))
            if 1 <= user_input <= 4:
                has_selected = True
            else:
                print("Please make appropriate selection")

        elif variant == 1:
            user_input = int(input("""[1] Record by Serial Number\n[2] Records by Observation Date
            [3] Group Records by Country/Region\n[4] Summarise Records"""))
            if 1 <= user_input <= 4:
                has_selected = True
            else:
                print("Please make appropriate selection")

        elif variant == 2:
            user_input = int(input("[1] Country/Region Pie Chart\n[2] Observations Chart\n[3] Animated Summary"))
            if 1 <= user_input <= 3:
                has_selected = True
            else:
                print("Please make appropriate selection")

        elif variant == 3:
            user_input = int(input("[1] All Data\n[2] Data for Specific Country/Region"))
            if 1 <= user_input <= 2:
                has_selected = True
        else:
            print("Please make appropriate selection")

    else:
        return user_input


def total_records(num_records):
    f"""
    Task 5: Display the total number of records in the data set.
    
    The function should display a message in the following format:

    "There are {num_records} records in the data set."

    Where {num_records} is the value of the parameter passed to this function
    
    :param num_records: the total number of movies in the data set
    :return: Does not return anything
    """
    num_records
    for record in num_records:
# once reletaion esatblished add code to iterete through data structure
    print(f"There are {num_records} records in the data set.")


def serial_number():
    """
    Task 6: Read in the serial number of a record and return the serial number.

    The function should ask the user to enter a serial number for a record e.g. 189
    The function should then read in and return the user's response as an integer.

    :return: the serial number for a record
    """

    serial_number = int(input("Enter a serial number for a record e.g. 189"))
    return serial_number
# need to add error loop

def observation_dates():
    """
    Task 7: Read in and return a list of observation dates.

    The function should ask the user to enter some observation dates
    This should be entered in the format dd/mm/yyyy where dd is two-digit day, mm is two digit month and yyyy is
    a four digit year e.g. 01/22/2020
    The function should return a list containing the specified observation dates.

    :return: a list of observation dates
    """
    user_dates = []

    for count in range(int(input("How many dates do you want to display?"))):
        user_dates.append(input("Entered date in the format dd/mm/yyyy\n"))

    return user_dates
# GOTTA ADD FAILSAFE


def display_record(record, cols=None):
    """
    Task 8: Display a record. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for the record will be displayed.

    The parameter record is a list of values e.g. [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]
    The parameter cols is a list of column indexes e.g. [0,3,5]
    The function should display a list of values.
    The displayed list should only consist of those values whose column index is in cols.

    E.g. if cols is [1,3] then for the record [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]
    the following should be displayed:
    ['01/22/2020','Mainland China']

    E.g. if cols is [0,1,4] then for the record [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]
    the following should be displayed:
    [1,'01/22/2020','1/22/2020 17:00']

    E.g. if cols is an empty list or None then all the values will be displayed
    [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]

    :param record: A list of data values for a movie
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """

    list_to_display = [record[cols]]
    if cols is not None or cols != 0:
        print(list_to_display)
    else:
        print(record)


def display_records(records, cols=None):
    """
    Task 9: Display each record in the specified list of records.
    Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for a movie will be displayed.

    The function should have two parameters as follows:

    records     which is a list of records where each record itself is a list of data values.
    cols        this is a list of integer values that represent column indexes.
                the default value for this is None.

    You will need to add these parameters to the function definition.

    The function should iterate through each record in records and display the record.

    Each record should be displayed as a list of values e.g. [1,01/22/2020,Anhui,Mainland China,1/22/2020 17:00,1,0,0]
    Only the columns whose indexes are included in cols should be displayed for each record.

    If cols is an empty list or None then all values for the record should be displayed.

    :param records: A list of records
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    list_to_display = []
    for record in records:
        if cols is not None or cols != 0:
            list_to_display.append(record[cols])
        else:
            print(record)
