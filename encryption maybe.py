StrToEncrypt = input("Input the text")
EncryptPattern = input("Input the pattern of encryption, with a gap between each number") + " "
valid = False
while valid is False:
    EncryptOrDecrypt = input("Do you want to Encrypt or Decrypt?")
    if EncryptOrDecrypt.lower() == "encrypt" or EncryptOrDecrypt.lower() == "decrypt":
        valid = True
    else:
        print("Invalid input")
EncryptPatternList = []
counter = 0
for x in range(0, len(EncryptPattern)):
    if EncryptPattern[x] == " " and EncryptPattern[(x-counter):(x)] != "":
        EncryptPatternList.append(EncryptPattern[(x-counter):(x)])
        counter = 0
    elif EncryptPattern[x].isdigit():
        counter += 1
    else:
        counter = 0
counter = 0
MaxCounterValue = len(EncryptPatternList)-1
EncryptedStr = []
for x in range(0, len(StrToEncrypt)):
    if StrToEncrypt[x] != " ":
        ChrDigit = ord(StrToEncrypt[x])
        if counter <= MaxCounterValue:
            if EncryptOrDecrypt.lower() == "encrypt":
                ChrDigit += int(EncryptPatternList[counter])
                if ChrDigit > 26:
                    ChrDigit -= 26
            else:
                ChrDigit -= int(EncryptPatternList[counter])
                if ChrDigit < 1:
                    ChrDigit += 26
            counter += 1
        else:
            counter = 0
            if EncryptOrDecrypt.lower() == "encrypt":
                ChrDigit += int(EncryptPatternList[counter])
                if ChrDigit > 26:
                    ChrDigit -= 26
            else:
                ChrDigit -= int(EncryptPatternList[counter])
                if ChrDigit < 1:
                    ChrDigit += 26
            counter += 1
        EncryptedStr.append(chr(ChrDigit))
    else:
        EncryptedStr.append(" ")
EncryptedStr = "".join(EncryptedStr)
print(EncryptedStr)
