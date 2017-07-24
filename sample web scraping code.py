import requests, bs4, openpyxl

#open excel and identify sheet to dump data into
wb = openpyxl.load_from_workbook('Book1.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

#identify website and obtain html document for web page
url_str = 'website.com'
res = requests.get(url_str)
res.raise_for_status() #checks for html error codes when accessing page
htmldoc = bs4.beautifulsoup(res.text)

#identify selectors and put them into a list
elements_list  htmldoc.select('.question-summary narrow') #selects the class ('.' indicats html type class)

#for each instance in elements_list, add the title to a MS excel file
i=2
for each instance in elements_list:
	sheet.cell(row=i,column=1).value = instance.get_text()
	sheet.cell(row=i,column=2).value = instance.get('href')
	i += 1
	
#save the workbook and close
wb.save('Book1.xlsx')
wb.close()
