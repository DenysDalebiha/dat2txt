# coding=Windows-1251
FLic = open(r"license.dat", "r")
FKey = open(r"key.txt", "w")
Text_Lic = FLic.read()
FKey.write('ED000000;')
FKey.write(Text_Lic[5:Text_Lic.find("==") + 2] + ";")
Text_Lic = Text_Lic[Text_Lic.find("==") + 2:]
for i in range(0,6):
    w = hex(ord(Text_Lic[i]))[2:]
    if len(w) < 2: w = '0' + w
    if i == 2 : w = w + ';'
    FKey.write(w)
Text_Lic = Text_Lic[6:]
FKey.write(';') 
for i in range(0,10):
    if (Text_Lic.find("4")) > 0:
        FKey.write(Text_Lic[:11] + ";")
        Text_Lic = Text_Lic[14:]
        print (Text_Lic)
    else:
        FKey.write(";")
FLic.close()
FKey.close()