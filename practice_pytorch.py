import csv

'''
end_number = 0 

# make AIhub csv for deep speech 2
# /path/to/audio2.wav,/path/to/text2.txt <- this form
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(1,125):
    
        path_name = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub/KsponSpeech_01/KsponSpeech_"
        

        # 앞에 000 표시
        if(len(str(i))==1):
            path_name_number = "000" + str(i)

        elif(len(str(i))==2):
            path_name_number = "00" + str(i)
        
        elif(len(str(i))==3):
            path_name_number = "0" + str(i)
        
        elif(len(str(i))==4):
            path_name_number = str(i)
        
        first_path = path_name+path_name_number
        
        for j in range(1000):
            
            end_number += 1

            if(len(str(end_number))==1):
                path_end_number = "00000" + str(end_number)

            elif(len(str(end_number))==2):
                path_end_number = "0000" + str(end_number)
            
            elif(len(str(end_number))==3):
                path_end_number = "000" + str(end_number)
            
            elif(len(str(end_number))==4):
                path_end_number = "00" + str(end_number)

            elif(len(str(end_number))==5):
                path_end_number = "0" + str(end_number)

            elif(len(str(end_number))==6):
                path_end_number = str(end_number)

            total = first_path + "/KsponSpeech_"+ path_end_number
            # ex) /home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub/KsponSpeech_01/KsponSpeech_0124/KsponSpeech_123017
            
            writer.writerow([total + ".wav", total + ".txt"])
'''


rnns =[]

rnns.append(('0', 1))

print(rnns)