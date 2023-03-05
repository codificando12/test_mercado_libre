from openpyxl import Workbook

# this funtion will take 2 elements join them in a tuple and then it will be exporte to an excel file
def create_xlsx(title, price):
    wb = Workbook()
    ws = wb.create_sheet('items_list')
    lst = []
    for tupla in zip(title, price):
        lst.append(tupla)
    
    for row in lst:
        ws.append(row)
    

    wb.save("item_list.xlsx")

if __name__ == "__main__":
    create_xlsx()
