import pandas as pd
import pre_processing_for_AI_hub_data as pre
from tqdm import trange
import csv
import shutil

TOTAL_NUM = 622545
TRAIN_NUM = int( 622545 * 0.96 )
VAL_NUM = int( 622545 * 0.02 )
TEST_NUM = TOTAL_NUM - TRAIN_NUM - VAL_NUM

#train 96% test 2% val 2%

count = 0

with open("AI_hub_all_shuffle.csv", newline='') as csvfile:
    file_path = csv.reader(csvfile)
    
    for i in file_path:
        # print(i[0]) - wav 파일
        # print(i[1]) - txt 파일
        if count < TRAIN_NUM:
            # move train 으로
            with open('AI_hub_train.csv', 'a', encoding='utf-8') as f:
                a = csv.writer(f)
                path_list = [i[0], i[1]]
                a.writerow(path_list)
           
        elif count < TRAIN_NUM + VAL_NUM :
            # move val 로
            with open('AI_hub_val.csv', 'a', encoding='utf-8') as ff:
                a = csv.writer(ff)
                path_list = [i[0], i[1]]
                a.writerow(path_list)
              
        else:
            #test 로
            with open('AI_hub_test.csv', 'a', encoding='utf-8') as fff:
                a = csv.writer(fff)
                path_list = [i[0], i[1]]
                a.writerow(path_list)
             
        if count%5000 == 0:
            print(count)
        count += 1
