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

train_wav_path = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub_dataset/train/wav"
train_txt_path = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub_dataset/train/txt"
val_wav_path = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub_dataset/val/wav"
val_txt_path = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub_dataset/val/txt"
test_wav_path = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub_dataset/test/wav"
test_txt_path = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub_dataset/test/txt"

count = 0

with open("AI_hub_all_shuffle.csv", newline='') as csvfile:
    file_path = csv.reader(csvfile)
    
    for i in file_path:
        # print(i[0]) - wav 파일
        # print(i[1]) - txt 파일
        if count < TRAIN_NUM:
            # move train 으로
            shutil.move(i[0],train_wav_path)
            shutil.move(i[1],train_txt_path)
            
        elif count < TRAIN_NUM + VAL_NUM :
            # move val 로
            shutil.move(i[0],val_wav_path)
            shutil.move(i[1],val_txt_path)
              
        else:
            #test 로
            shutil.move(i[0],test_wav_path)
            shutil.move(i[1],test_txt_path)
            

        
        if count%5000 == 0:
            print(count)
        count += 1
