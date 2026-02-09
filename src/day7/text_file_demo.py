# #####n file handling ########
# file = open("sample.text","w")
# file.write("Hello,this is a file handling example.")
# file.close()
# file = open("sample.text","r")
# content = file.read()
# print(content)
# file.close()

# with open("sample.text","r")as file:
#     content = file.read()
#     print(content)

# try:
#  with open("missing.text","r")as file:
#     print(file.read())
# except FileNotFoundError:
#     print("File not found. Plase check the filename.")

# import csv 
# with open("data.csv","w",newline="")as file:
#     writer = csv.writer(file)
#     writer.writerow(["name","age","city"])
#     writer.writerow(["kumar",24,"mangolure"])
#     writer.writerow(["akhil",21,"hospet"])
#     writer.writerow(["abhi",22,"haveri"])
# with open("data.csv","r")as file:
#   reader = csv.reader(file)
#   for row in reader:
#     print(row)

# from openpyxl import load_workbook

# wb = load_workbook("sample_student.xlsx")
# sheet = wb.active

# for row in sheet.values:
#     print(row)

