import random
import csv

audio_paths = []
target_paths = []
count =0

with open("AI_hub_all.csv", newline='') as csvfile:
    file_path = csv.reader(csvfile)
    
    for i in file_path:
        
        audio_paths.append(i[0])
        target_paths.append(i[1])
        if count%5000 == 0:
            print(count)
        count += 1

data_paths = list(zip(audio_paths, target_paths))
random.shuffle(data_paths)
audio_paths, target_paths = zip(*data_paths)

with open('AI_hub_all_shuffle.csv', 'w', encoding='utf-8') as f:
    a = csv.writer(f)

    for i in range(0,622545):
        path_list = [audio_paths[i], target_paths[i]]
        a.writerow(path_list)
        
        if i % 5000 == 0:
            print(i)
