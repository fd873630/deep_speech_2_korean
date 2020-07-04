'''
https://github.com/sooftware/KoSpeech/wiki/Preparation-before-Training
'''

#file_path_firtst = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub/KsponSpeech_01/KsponSpeech_0001/KsponSpeech_"

def filenum_padding(filenum):
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

def get_path(path, fname, filenum, format):
    return path + fname + filenum + format


BASE_PATH = "data/AI_hub/KsponSpeech_01/KsponSpeech_0001/KsponSpeech_"
FNAME = 'KsponScript_'
filenum = 1348
format = '.txt'

print(get_path(BASE_PATH,FNAME,filenum_padding(filenum),".txt"))