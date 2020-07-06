'''
https://m.blog.naver.com/PostView.nhn?blogId=aimldl&logNo=221559323232&proxyReferer=https:%2F%2Fwww.google.com%2F
'''
import wave

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


# The parameters are prerequisite information. More specifically,
# channels, bit_depth, sampling_rate must be known to use this function.
def pcm2wav( pcm_file, wav_file, channels=1, bit_depth=16, sampling_rate=16000 ):

    # Check if the options are valid.
    if bit_depth % 8 != 0:
        raise ValueError("bit_depth "+str(bit_depth)+" must be a multiple of 8.")
        
    # Read the .pcm file as a binary file and store the data to pcm_data
    with open( pcm_file, 'rb') as opened_pcm_file:
        pcm_data = opened_pcm_file.read();
        
        obj2write = wave.open( wav_file, 'wb')
        obj2write.setnchannels( channels )
        obj2write.setsampwidth( bit_depth // 8 )
        obj2write.setframerate( sampling_rate )
        obj2write.writeframes( pcm_data )
        obj2write.close()


scr_file_path = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub_pcm/KsponSpeech_"
dir_file_path = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub_wav/KsponSpeech_"

#622546
for j in range(1, 622546):
        num_1 = filenum_padding(j)
        src_2 = scr_file_path + num_1
        dir_2 = dir_file_path + num_1

        pcm2wav(src_2 + ".pcm", dir_2 + ".wav", 1, 16, 16000 )

        if j%5000==0:
            print(j)
