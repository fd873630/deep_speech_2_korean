
file_path_firtst = "/home/jhjeong/jiho_deep/deepspeech.pytorch/data/AI_hub/KsponSpeech_01/KsponSpeech_0001/KsponSpeech_"


end_number= 0
a=0                    
            
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

            file_path = file_path_firtst + path_end_number + ".txt"
            
            
            with open(file_path, 'rt', encoding='CP949') as MyFile:

                MyString = MyFile.readlines()
                
                for line in MyString:
                    
                    print(line)
                    if(a==0):
                        with open("total.txt", 'w') as f:
                            f.write(line)
                            a+=1
                    else:
                        with open("total.txt", 'a') as f:
                            f.write(line)