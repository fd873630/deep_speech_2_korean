import csv
import pre_processing_for_AI_hub_data as pre

wav_file_path = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub_wav/"
txt_file_path = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub_txt/"
fname = "KsponSpeech_"

#622546
with open('AI_hub_all.csv', 'w', encoding='utf-8') as f:
    a = csv.writer(f)

    for i in range(1,622546):
        wav_path = wav_file_path + fname + pre.filenum_padding(i)+ ".wav"
        txt_path = txt_file_path + fname + pre.filenum_padding(i)+ ".txt"
        path_list = [wav_path, txt_path]
        a.writerow(path_list)
        
        if i % 5000 == 0:
            print(i)