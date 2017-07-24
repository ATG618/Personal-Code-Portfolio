import xlwings as xw

excel_app = xw.apps[0]


def hello_xlwings():
    wb = excel_app.Book.caller()
    wb.sheets[0].range("A1").value = "Hello xlwings!"


@xw.func
def hello(name):
    return "hello {0}".format(name)
