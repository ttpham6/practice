class LEDCharacters():
    def __init__(self, input: str):
        self._Display = ""
        
        if (type(input) == list):
            self.listOfCharacters = input
        elif (type(input) == str):
            self.listOfCharacters = [x for x in input]
        
        self._setDisplay()
            
    def getDisplay(self):
        return self._Display
                    
    def _setDisplay(self):
        result = [self.IndividualCharacters(myChar) for myChar in self.listOfCharacters]
        # numberOfCharacters = self.IndividualCharacters.len()
        numberOfCharacters = len(self.listOfCharacters)
        
        scanLine = ["", "", "", "" , "", ""]
        
        for a in result:
            a = a.strip()
            b = a.rstrip()
            c = b.split("\n")
            scanLine[0] = scanLine[0] + c[0].format(width=12) + "\t"
            scanLine[1] = scanLine[1] + c[1].format(width=12) + "\t" 
            scanLine[2] = scanLine[2] + c[2].format(width=12) + "\t"    
            scanLine[3] = scanLine[3] + c[3].format(width=12) + "\t" 
            scanLine[4] = scanLine[4] + c[4].format(width=12) + "\t"            
        # for line in scanLine:
        #     print(line)
        self._Display = "".join(result)
    
    def IndividualCharacters(self, char: str)->str:
        # digit = number
        digit = int(char)
        
        stringDigit = ""
        
        match(digit):
            case 0: 
                stringDigit = """\n#   #   #\n#       #\n#       #\n#       #\n#   #   #\n"""
                # stringDigit = """\t#   #   #\n#       #\n#       #\n#       #\n#   #   #\t"""
                stringDigit = """
#   #   #
#       #
#       #
#       #
#   #   #
                    """


            case 1:    
                stringDigit = """
#
#
#
#
#
                    """
         #       t1 = stringDigit.strip()
                # t1 = t1.split("\n")
                # t1 = "\n".join(t1)
                # stringDigit = t1
            case 2:
                stringDigit = """
#   #   # 
        #
#   #   #
#        
#   #   #
                    """    
        
            case 3:
                stringDigit = """
#   #   # 
        #
#   #   #
        #
#   #   #
                    """    
            case 4: # revisit: fix
                stringDigit ="""
#       #
#       #
# # # # #
        #
        #
                    """   
            case 5:# revisit: fix
                stringDigit = """
#   #   # 
#       
#   #   #
        #
#   #   #
                    """    
            case 6: # revisit: fix
                stringDigit = """
#   #   #
#            
#   #   #
#       #
#   #   #
                    """    
            case 7: # revisit: fix
                stringDigit = """
#   #   #
        #
        #
        #
        #
                   """    
            case 8:
                stringDigit = """
#   #   # 
#       #
#   #   #
#       #
#   #   #"""
            case 9:
                stringDigit = """#   #   #
#       #
#   #   #
        #
#   #   #"""    
        return stringDigit



def main():
  # myData = input()
    myData = "1 2 3 4 5 6 7 8 9"
    myData = "9081726354"
    myObj = LEDCharacters(myData)

if __name__ == "__main__":
    main()
    