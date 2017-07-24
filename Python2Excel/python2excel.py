import pandas as pd #pandas module
import xlwings as xw #xlwings module
pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
# pd.figsize(15, 5) TODO not working

''' 
Algorithm:
    1) Pull Data from Excel push to python
    2) Clean and Format Data
    3) Validate Data based on program requirements
    4) Process Data based on program requirements
    5) Push Data from python to Excel
    
'''

def main():
    '''script is not run directly from python, main function is called from excel macro in order to run program
    Variables:
        excel_app: xlwings data structure, an excel application that is accessed via python
        excel_wb: xlwings data structure, an excel workbook currently open and accessible in python
        excel_sht: xlwings data structure, an excel worksheet currently open and accessing in python.
    '''

    def pull_data(file_type, file_name, range_name=None, input_data_type="pandas", file_path=None):
        '''This function will do the following:
            1) Pull Data from Excel or CSV File
            2) saves the data to pandas or list data type

            Arguments to Function:
                file_type: string data type, the file type of the file that data will be retrieved from.
                can be either (excel or csv)
                data_type: string data type, the data structure that the retrieved data will be saved as.
                 can be either (pandas or list).
                file_path: string data type, the location of the file data is pulled from, if variable is empty then
                 file will be assumed to be saved in the current working directory
                file_name: string data type, the name of the file that data is pulled from.
                range_name: string data type, the name of the excel range that data is pulled from when applicable
                global variables used: excel_app, excel_wb, excel_sht

            Variables:
                input_df: pandas data frame,
                input_ds: pandas data series,
                input_data_list: python list,


         '''
        input_df = None
        input_ds = None
        input_data_list = None


        # pull data from excel range and save as pandas data frame or python list based on argument.
        if file_type == "excel" and input_data_type == "pandas":
            # pull data range from excel range and save to data frame
            input_df = excel_sht.range(range_name).options(pd.DataFrame).value
        elif file_type == "excel" and input_data_type == "list":
            # pull data range from excel range and save to list variables
            input_data_list = excel_sht.range(range_name).value

        # pull data from csv file and save as pandas data frame or python list based on argument.
        if file_type == "csv" and input_data_type == "pandas":
            # pull data range from csv file and save to data frame
            input_df = pd.read_csv(file_name)
        elif file_type == "csv" and input_data_type == "list":
            # pull data range from csv file and save to list variables
            if file_path == None:
                #if file path is none read from csv saved in current working directory
                input_data_list = pd.read_csv(file_name)
            else:
                #else concatenate string and pull from location of csv file
                input_data_list = pd.read_csv(file_path&file_name)

        #return input data to main variable
        return input_df,input_data_list,input_ds

    def clean_data():
        '''This function will clean and format the data that has been retrieved.
            Steps:
                1) String --> Trim Data, remove empty space before & after string
                2) Numbers --> Convert to Values, convert to Number Data Variables
                3) Dates --> Convert to Date, compatiable with excel
                4) Floating --> Convert to Floating Rate Values
                3) Empty --> Convert Empty Values to Nan
                4) Macro Specific Formatting:
         Arguments to Functions:

         Variables:

        '''
        return

    def validate_data():
        '''This function will validate data based on the requirements of the specific macro

         Arguments to Functions:

         Variables:

        '''
        return

    def process_data():
        '''This function will process all changes to the input data based on the specifics of the macro

        Arguments to Functions:

        Variables:
        '''
        return

    def push_data():
        '''This function will push data back to specific output. Excel Macro or CSV File in Current Working Directory.

        Arguments to Functions:

        Variables:

        '''
        return


    #main code for running this script

    #variable assignments --- beg.
    excel_app = xw.apps[0]    #set variable equal to excel application
    excel_wb = excel_app.Book('filename.extension') #set variable to filename of excel filename
    excel_sht = excel_wb.sheets['sheet_name'] #set variable to sheet name
    excel_range = None #set variable to specific range
    cwd = None #set to current working directory


    #--- end.



    #call pull data function
    pull_data()

    #call clean data function
    clean_data()

    #call validate data function
    validate_data()

    #call process data function
    process_data()

    #call push data function
    push_data()


def test_main():
    #test data
    test_data = \
        [
            ["Col1", "Col2", "Col3"],
            [1,2,3],
            ["a1","b2","c3"],
            [14,15,16]
        ]
    '''test cases:
        1) excel file does not exist
        2) csv file does not exist
        3) argument used but filetype is not correct
        4) output data failed to save??? 
        
    '''