#coding=utf-8
import main.pandas_run as pr
from main.pandas_run import Football as ft
import csv




def rank_stat():
    csv_id = ['国家', '进球', '失球', '总场次', '胜场', '负场', '排名范围']
    with open('china.csv','a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(csv_id)
        rank_range = [[i * 20 + 1, i * 20 + 20] for i in range(0, 10)]
        for i in rank_range:
            p = ft(name=['70_中国'], game_type=False, time=[2014, 2018], rank=i)
            s_list = p.mulprocess(8)
            print(s_list)
            writer.writerow(list(s_list[0])+[i])

if __name__ == '__main__':
     #pr.query('中国')
     rank_stat()






