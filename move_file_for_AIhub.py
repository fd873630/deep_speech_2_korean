import shutil


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


def filenum_padding_2(filenum):
    """
    AI Hub 데이터셋에서 파일 번호는 '000001', '002545', '612543' 와 같은 형식으로 이루어져 있다.
    이러한 형식에 맞춰주기 위하여 파일 번호를 입력으로 받아 해당 포맷에 맞춰주는 함수를 미리 정의해둔다
    """
    if filenum < 10: 
        return '000' + str(filenum)
    elif filenum < 100: 
        return '00' + str(filenum)
    elif filenum < 1000: 
        return '0' + str(filenum)
    else: 
        return str(filenum)

count = 1
'''
scr = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub/KsponSpeech/"
dir = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub2"

# 622까지는 1000개니까 다음과 같이 이동
for i in range(1, 623):
    num = filenum_padding_2(i)
    src_1 = scr + "KsponSpeech_" + num

    for j in range(1, 1001):
        num_1 = filenum_padding(count)
        src_2 = src_1 + "/KsponSpeech_" + num_1
        count += 1
        #print(src_2 + ".txt")
        shutil.move(src_2 + ".txt", dir)
        shutil.move(src_2 + ".pcm", dir)
        
    print(i)

scr = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub/KsponSpeech/KsponSpeech_0623"
dir = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub2"

for j in range(622001, 622546):
        num_1 = filenum_padding(j)
        src_2 = scr + "/KsponSpeech_" + num_1
        shutil.move(src_2 + ".txt", dir)
        shutil.move(src_2 + ".pcm", dir)   
''' 
scr = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub/"
dir_file_path = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub_pcm"

for j in range(1, 622546):
        num_1 = filenum_padding(j)
        src_2 = scr + "KsponSpeech_" + num_1

        shutil.move(src_2 + ".pcm", dir_file_path) 