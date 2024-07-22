import string
import secrets
import json
import math
from string import digits, ascii_letters, punctuation


"""
Json Password file downloaded from
https://github.com/matthewreagan/WebstersEnglishDictionary
"""
class LoadDictionaryFile():
    def __init__(self):
        self.data = None

    def LoadFile(self):
        data = None
        with open("C:\\Users\\phamt\\Documents\\source\\practice\\PasswordPhrase\\dictionary.json") as fileHandle:
            self.data = json.load(fileHandle)
        
        #  result = secrets.choice(list(data.keys()))
        # print(result)


    def RandomCharacters(self, count=1)->string:
        myPassword = str()
        passwordCharacters = digits + ascii_letters + punctuation

        combinations = math.pow(len(passwordCharacters), count)
        print("The number of compinations are %d" %math.log2(combinations))

        for x in range(count):
            myPassword += secrets.choice(passwordCharacters)
        return myPassword

    def PassWord(self, count=1)->string:

        
        # bilimbingciceronecomplacentlyadam

        myPassword = str()
        iteration = 0
        webstersDictionary = list(self.data.keys())
        # print(str(len(webstersDictionary)) + "\n")
        
        value = self.data["bilimbing"]
        print(value + "\n")


        lenDictionary = len(webstersDictionary)

        combinations = math.pow(lenDictionary, count)
        print("The number of compinations are %d" %math.log2(combinations))
        
        for x in range(count):
            iteration += 1
            myPassword += secrets.choice(webstersDictionary)
        
        return myPassword


def main():
    myFile = LoadDictionaryFile() 
    myFile.LoadFile()

    result = myFile.PassWord(count=4)
    print(result)
    
    result = myFile.RandomCharacters(count=10)
    


if __name__ == "__main__":
    main()



