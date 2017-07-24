Module: Python2Excel

Functions:
	1) Pull Excel Table to Data Series
		a) Pull from Excel File, CSV File
	2) Push Data Series to Excel Table
		b) new csv file
		c) existing csv file
	3) Clean Data Functions
	4) Template File:
		a) Input Tab
		b) Input Data
		c) Output Data

Step:
	1) Pull Data from Excel to Panda Data Series
	2) Clean Data
	3) Process Data
	4) Push Panda Data Series to Excel or CSV Output
		
Required Packages:
	Pandas
	BeautiulSoup
	
#set app variable to new excel application
app = xw.App()

#set app variable to existing excel application
app = xw.apps[0]

#set wb variable to new workbook
wb = app.Book()

#set wb variable to existing file in the cwd
wb = app.Book('filename.xlsx')


#set wb variable to existing file in the cwd
wb = app.Book(r '[path\filename.xlsx')

#set sht variable equal to sheet
sht = wb.sheets['Sheet1']


#write to a range
sht.range('A1').value = 'hello'

#read from a range
sht.range('A1').value


#read an excel range to python
df = sht.range('A1:C3').options(pd.DataFrame).value #read excel range to pandas df

list = sht.range('A1:A5').value #automatically returned as list (1D) or nested list (multi-dim)

#write data to excel range
sht.range('A1').value = list #writing data from a list, only top left cell reference is required

sht.range('A1').value = df #writing data from a pandas df, only top left cell reference is required

df.to_csv(file_name, encoding='utf-8') #writing data from pandas to xsc


def hello_xlwings():
    script and function must be referenced in visual basic sub procedure: import python2excel;
        Sub SampleCall()
            mymodule = Left(ThisWorkbook.Name, (InStrRev(ThisWorkbook.Name, ".", -1, vbTextCompare) - 1))
            RunPython ("import " & mymodule & ";" & mymodule & ".hello_xlwings()")
        End Sub

    wb = app.Book('excel2python.xlsm')
    wb.sheets[0].range('A1').value = 'hello world'