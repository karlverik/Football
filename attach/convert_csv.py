#coding=utf-8
import csv
import xlrd

book = xlrd.open_workbook('football_rank.xls',encoding_override='uft-8')
list_1 = book.sheet_names() #210


for i in list_1:
    with open('./nation_csv/'+i+'.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        table = book.sheet_by_name(i)
        rows = table.nrows
        for k in range(0,rows):
            writer.writerow(table.row_values(k))
    file.close()






