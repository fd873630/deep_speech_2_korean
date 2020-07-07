import csv

train_wav_path = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub_dataset/train/wav/"
train_txt_path = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub_dataset/train/txt/"
val_wav_path = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub_dataset/val/wav/"
val_txt_path = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub_dataset/val/txt/"
test_wav_path = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub_dataset/test/wav/"
test_txt_path = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub_dataset/test/txt/"

'''
with open("AI_hub_test.csv", newline='') as csvfile:
    file_path = csv.reader(csvfile)
    
    for i in file_path:
        change_wav_path = test_wav_path + i[0][59:]
        change_txt_path = test_txt_path + i[1][59:]
        
        with open('AI_hub_test_chage.csv', 'a', encoding='utf-8') as f:
            a = csv.writer(f)
            path_list = [change_wav_path, change_txt_path]
            a.writerow(path_list)

with open("AI_hub_val.csv", newline='') as csvfile:
    file_path = csv.reader(csvfile)
    
    for i in file_path:
        change_wav_path = val_wav_path + i[0][59:]
        change_txt_path = val_txt_path + i[1][59:]
    
        with open('AI_hub_val_chage.csv', 'a', encoding='utf-8') as f:
            a = csv.writer(f)
            path_list = [change_wav_path, change_txt_path]
            a.writerow(path_list)


with open("AI_hub_train.csv", newline='') as csvfile:
    file_path = csv.reader(csvfile)
    
    for i in file_path:
        change_wav_path = train_wav_path + i[0][59:]
        change_txt_path = train_txt_path + i[1][59:]
        
        with open('AI_hub_train_chage.csv', 'a', encoding='utf-8') as f:
            a = csv.writer(f)
            path_list = [change_wav_path, change_txt_path]
            a.writerow(path_list)
'''        