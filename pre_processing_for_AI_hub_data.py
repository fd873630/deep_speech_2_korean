'''
https://github.com/sooftware/KoSpeech/wiki/Preparation-before-Training
'''
import re


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

def get_path(path, fname, filenum, format):
    '''
    텍스트 파일의 경로를 잡아주는 함수를 미리 정의해둔다.
    '''
    return path + fname + filenum + format

def bracket_filter(sentence):
    '''
    (A) / (B) 일 때, B만을 가져와주는 함수이다.
    (철자전사) / (발음전사) 중 발음전사를 선택하기 위해 정의했다.
    '''
    new_sentence = str()
    flag = False
    
    for ch in sentence:
        if ch == '(' and flag == False: 
            flag = True
            continue
        if ch == '(' and flag == True:
            flag = False
            continue
        if ch != ')' and flag == False:
            new_sentence += ch
    return new_sentence

def special_filter(sentence):
    '''
    문자 단위로 특수 문자 및 노이즈 표기 필터링해주는 함수이다.
    특수 문자를 아예 필터링 해버리면 문제가 되는 '#', '%'와 같은 문자를 확인하고, 문제가 되는 특수 문자는 해당 발음으로 바꿔주었다.
    '''
    SENTENCE_MARK = ['?', '!']
    NOISE = ['o', 'n', 'u', 'b', 'l']
    EXCEPT = ['/', '+', '*', '-', '@', '$', '^', '&', '[', ']', '=', ':', ';', '.', ',']
    
    new_sentence = str()
    for idx, ch in enumerate(sentence):
        if ch not in SENTENCE_MARK:
            # o/, n/ 등 처리
            if idx + 1 < len(sentence) and ch in NOISE and sentence[idx+1] == '/': 
                continue 

        if ch == '#': 
            new_sentence += '샾'

        elif ch not in EXCEPT: 
            new_sentence += ch

    pattern = re.compile(r'\s\s+')
    new_sentence = re.sub(pattern, ' ', new_sentence.strip())
    return new_sentence

def sentence_filter(raw_sentence):
    '''
    위에서 정의한 2 함수를 이용해서 문장을 필터링해주는 함수
    '''
    return special_filter(bracket_filter(raw_sentence))

# 위의 과정을 끝내면 < % > 특수문자가 남게되는데, 해당 특수문자는 '프로', '퍼센트' 두 가지 발음이 가능하므로, 
# 직접 확인한 결과 총 8개의 파일에서 등장했고, 4개의 **'프로'**와 4개의 '퍼센트' 이루어지는 것을 확인하고 수작업으로 변환했다.
# -> 087797, 215401, 284574, 397184, 501006, 502173, 542363, 581483

