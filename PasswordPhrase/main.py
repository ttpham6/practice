import string
import secrets
import json
import math
from string import digits, ascii_letters, punctuation, ascii_uppercase
import argparse

"""
Json Password file downloaded from
https://github.com/matthewreagan/WebstersEnglishDictionary
"""
class LoadDictionaryFile():
    def __init__(self):
        self.WebstersDictionary = None

    def LoadFile(self):

    #   C:\Users\phamt\Documents\source\practice\PasswordPhrase\dictionary.json
    #   C:\Users\phamt\Documents\source\practice\PasswordPhrase\main.py  
        with open("./PasswordPhrase/dictionary.json") as fileHandle:
            self.WebstersDictionary = json.load(fileHandle)
        
        #  result = secrets.choice(list(data.keys()))
        # print(result)


    def RandomCharacters(self, count=1)->string:
        myPassword = str()
        passwordCharacters = digits + ascii_letters + punctuation

        combinations = math.pow(len(passwordCharacters), count)
        print("The number of base2 combinations for random %d characters are %d" % (count, math.log2(combinations)))

        for x in range(count):
            myPassword += secrets.choice(passwordCharacters)
        return myPassword


    def PassWord(self, count=2, insertNumbers=False, insertSpecial=False, insertChars=False, insertUpper=False)->str:
        dictionary_combinations = 0
        separator_combinations = 0
        total_combinations = 0

        myPassword = str()
        iteration = 0
        websters = list(self.WebstersDictionary.keys())
        # print(str(len(webstersDictionary)) + "\n")


        lenDictionary = len(websters)
        dictionary_combinations = math.pow(lenDictionary, count)

        separators = self.AdditionalSeparatorCharacters(insertNumbers, insertSpecial, insertChars, insertUpper)
        lenSep = len(separators)

        if(separators):
            separator_combinations = math.pow(lenSep, count-1)

        if(separators):
            total_combinations = dictionary_combinations * separator_combinations
        else:
            total_combinations = dictionary_combinations

        print("The number of base2 compinations for count of %d are %d" %(count, math.log2(total_combinations)))
        
        for iteration in range(count):
            # iteration += 1
            myPassword += secrets.choice(websters)

            if (count > 1) and (iteration < count-1):
                if insertNumbers or insertSpecial or insertChars or insertUpper:
                    myPassword += secrets.choice(separators)
        
        return myPassword

    def AdditionalSeparatorCharacters(self,insertNumbers=False, insertSpecial=False, insertChars=False, insertUpper=False)->str:
        separatorCharacters = ""

        if(insertChars): separatorCharacters += ascii_letters
        if(insertUpper): separatorCharacters += ascii_uppercase
        if(insertNumbers): separatorCharacters += digits
        if(insertSpecial): separatorCharacters += punctuation
        return separatorCharacters


def main():
    myFile = LoadDictionaryFile() 
    myFile.LoadFile()

    result = myFile.PassWord(4, insertNumbers=True, insertSpecial=True, insertChars=False, insertUpper=False)
    print(result)
    

    result = myFile.PassWord(4, insertNumbers=True, insertSpecial=True, insertChars=False, insertUpper=False)
    print(result)
    
    
    result = myFile.PassWord(4, insertNumbers=True, insertSpecial=True, insertChars=False, insertUpper=False)
    print(result)
    
    
    result = myFile.PassWord(4, insertNumbers=True, insertSpecial=True, insertChars=False, insertUpper=False)
    print(result)
    

    # result = myFile.RandomCharacters(count=12)
    

    # result = myFile.PassWord(4, insertNumbers=True, insertSpecial=False, insertChars=False, insertUpper=False)
    # print(result)
    
    # result = myFile.RandomCharacters(count=12)
    


    # result = myFile.PassWord(3, insertNumbers=True, insertSpecial=False, insertChars=False, insertUpper=False)
    # print(result)
    
    # result = myFile.RandomCharacters(count=10)


if __name__ == "__main__":
    

    main()



