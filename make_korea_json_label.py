import json

def filenum_padding(filenum):
    """
    AI Hub 데이터셋에서 파일 번호는 '000001', '002545', '612543' 와 같은 형식으로 이루어져 있다.
    이러한 형식에 맞춰주기 위하여 파일 번호를 입력으로 받아 해당 포맷에 맞춰주는 함수를 미리 정의해둔다
    """
    if filenum < 10: 
        return '00000' + str(filenum)
    elif filenum < 100: 
        return '0000' + str(filenum)
    elif filenum < 1000: 
        return '000' + str(filenum)
    elif filenum < 10000: 
        return '00' + str(filenum)
    elif filenum < 100000: 
        return '0' + str(filenum)
    else: 
        return str(filenum)


dir_file_path = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub_txt/"
file_path_2 = "KsponSpeech_"

#622546
label = []
'''
for i in range(1,622546):
    last_num = filenum_padding(i)
    with open(dir_file_path + file_path_2 + last_num + ".txt" , "r") as f:
        txts = f.readline()
    
    for j in range(len(txts)):
        if txts[j] in label:
            pass
        else:
            label.append(txts[j])

    if i%5000 == 0:
        print(i)


print(label)    

with open("labels_korean.json","w", encoding="utf-8") as f:
    json.dump(label,f,ensure_ascii=False, indent="\t")
'''

for i in range(1,622546):
    last_num = filenum_padding(i)
    with open(dir_file_path + file_path_2 + last_num + ".txt" , "r") as f:
        txts = f.readline()
    
    for j in range(len(txts)):      
        if txts[j] == "\n":
            print(dir_file_path + file_path_2 + last_num + ".txt")
        
    if i%5000 == 0:
        print(i)
'''
for i in range(1,622546):
    last_num = filenum_padding(i)
    with open(dir_file_path + file_path_2 + last_num + ".txt" , "r") as f:
        txts = f.readline()
    
    for j in range(len(txts)):      
        if txts[j] == "\n":
            with open(dir_file_path + file_path_2 + last_num + ".txt" , "w") as ff:
                a=txts.rstrip()
                ff.write(a)

            
        
    if i%5000 == 0:
        print(i)
'''