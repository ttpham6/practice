import unittest
import logging, sys


class TestClass(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(stream=sys.stderr, level=logging.INFO, format="")
        self.logger = logging.getLogger('TestClass')
        return super().tearDown()
        
    def tearDown(self) -> None:
        logging.basicConfig(stream=sys.stderr, level=logging.CRITICAL)
        return super().tearDown()

    def testAsciTable(self):
        display = ""
        for x in range(256):
            char = chr(x)               # Convert to char
            num = ord(char)             # Convert to number


            if self.logger.isEnabledFor(logging.DEBUG):            
                # I'd like to know the difference (with examples if possible) between CR LF (Windows), LF (Unix) and CR (Macintosh) line break types.
                # Special cases to prevent misformatting
                match(x):
                    case 9:     # Horizontal Tab
                        char = "HT"
                    case 10:    # Line Feed
                        char = "LF"
                    case 11:   # Vertical Tab
                        char = "VT"  
                    case 12:   # Form Feed to next page
                        char = "FF"
                    case 13:   # Carriage Return 
                        char = "CR"
                    case 27:   # Escape
                        char = "ES"
                display += f'{num:3} | {hex(num):3} | {char}\t'
                if (x+1) %6==0: # and x!=0: 
                    self.logger.debug(f"{display}")
                    display = ""
            self.assertEqual(num, x)    # Compare
           
            
    def testSimpleStringLen(self):
        # Example 1
        self.assertEqual(len('by'), 2)

        # Example 2
        self.assertEqual(len(""), 0)

        # Example 3
        self.assertEqual(len('I\'m'), 3) 

    def testMultiLine(self):
        
        multiline = '''Line #1
            Line #2'''
        self.assertEqual(len(multiline), 27)
    
        multiline1 = """Line #1
            Line #2"""
        self.assertEqual(len(multiline1), 27)


        # Demonstrating the ord() function.
        # 2.2.1.4 
        char_1 = 'a'
        char_2 = ' '  # space
        self.assertEqual(ord(char_1), 97)
        self.assertEqual(ord(char_2), 32)

        self.assertEqual(chr(97), 'a')
        self.assertEqual(chr(49), '1')
        self.assertEqual(chr(945), 'α')
        self.assertEqual(chr(10), "\n")
        self.assertEqual(chr(13), "\r")

        # 2.2.1.7 Slices
        alpha = "abdefg"
        self.assertEqual(alpha[1:3], "bd")
        self.assertEqual(alpha[3:], "efg")
        self.assertEqual(alpha[:3], "abd")
        self.assertEqual(alpha[3:-2], "e")
        self.assertEqual(alpha[-3:4], "e")
        self.assertEqual(alpha[0:4], "abde")
        self.assertEqual(alpha[-3:5], "ef")
        self.assertEqual(alpha[-3:6], "efg")
        
        self.assertEqual(alpha[::2], "adf")
        self.assertEqual(alpha[::3], "ae")
        self.assertEqual(alpha[::4], "af")
        self.assertEqual(alpha[::5], "ag")
        self.assertEqual(alpha[::6], "a")
        self.assertEqual(alpha[::7], "a")
        self.assertEqual(alpha[1::2], "beg")

        # 2.2.1.8 in, not operators
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.assertIn("f", alphabet)
        self.assertTrue("f" in alphabet)        
        self.assertFalse("F" in alphabet)
        self.assertFalse("1" in alphabet)
        self.assertTrue("ghi" in alphabet)
        self.assertFalse("Xyz" in alphabet)

        
        self.assertFalse("f" not in alphabet)
        self.assertTrue("F" not in alphabet)
        self.assertTrue("1" not in alphabet)
        self.assertFalse("ghi" not in alphabet)
        self.assertTrue("Xyz" not in alphabet)

        with self.assertRaises(AttributeError):
            alphabet.append()
           
    def testStringOperations(self):
        # 2.2.1.11
        constructedString = "aAbBuUzz"
        # for number, char in zip(range(len(constructedString)), constructedString):
        #     print(f"{char}:{ord(char)}", end = "\t")
        #     if not((number+1)%4):                
        #         print("\n")        
        # a:97    A:65    b:98    B:66
        # u:117   U:85    z:122   z:90


        self.assertEqual(min(constructedString), "A")
        self.assertEqual(max(constructedString), "z")

        knights = 'The Knights Who Say "Ni!"'
        
        # if self.logger.isEnabledFor(logging.DEBUG):     
        #     for number, char in zip(range(len(knights)), knights):
        #         self.logger.debug(f"{char}:{ord(char)}\t")
        #             #  if not((number+1)%4):                
        #             #      print("\n")
                
        self.assertEqual(min(knights), " ")
        self.assertEqual(max(knights), "y")
                
        # a:97    A:65    b:98    B:66
        # u:117   U:85    z:122   z:122
        # T:84    h:104   e:101    :32
        # K:75    n:110   i:105   g:103
        # h:104   t:116   s:115    :32
        # W:87    h:104   o:111    :32
        # S:83    a:97    y:121    :32
        # :34    N:78    i:105   !:33
        # :34    .
        
        
        # 2.2.1.13 Demonstrating the index() method:
     
        stringToIndex = "aAbByYzZaA"
        self.assertEqual(stringToIndex.index("b"), 2)
        self.assertEqual(stringToIndex.index("z"), 6)       
        
        self.assertEqual(stringToIndex.index("A"), 1)

        # V does not exist in string will generate ValueError
        with(self.assertRaises(ValueError)):
            self.assertEqual(stringToIndex.index("V"), 1)
        
        # 2.2.1.14 conversion string to list and usage count
        countString = "abcabc"
        self.assertEqual(countString.count("b"), 2)
        self.assertEqual(countString.count("d"), 0)

    # String methods 2.3
    def testStringMethods(self):
        self.assertEqual('abCD'.capitalize(), 'Abcd')
        self.assertEqual('ALPHA'.capitalize(), 'Alpha')
        self.assertEqual(' Alpha'.capitalize(), ' alpha')
        self.assertEqual('123'.capitalize(), '123')
        self.assertEqual("αβγδ".capitalize(), 'Αβγδ')
        self.assertEqual("γδ".capitalize(), 'Γδ')
        self.assertEqual('Alpha'.capitalize(), 'Alpha')
        
        beta = 'Beta'
        self.assertEqual(beta.center(2), 'Beta')
        self.assertEqual(beta.center(6), ' Beta ')
        self.assertEqual(beta.center(8, '#'), '##Beta##')
        
        zeta = 'zeta'
        self.assertTrue(zeta.endswith('a'))
        self.assertFalse(zeta.endswith('A'))
        self.assertTrue(zeta.endswith('ta'))
        self.assertFalse(zeta.endswith('et'))
        self.assertTrue(zeta.endswith('eta'))

        # find() returns position of character from 0 found in index otherwise -1
        eta = 'eta'
        self.assertTrue(eta.find('ta'))
        self.assertEqual(eta.find('ta'), 1)
        self.assertEqual(eta.find('a'), 2)
        self.assertEqual(eta.find('mma'), -1)       # Returns -1 not in index
   
        self.assertEqual("Long brown fox jumped over the lazy dog".find("fox"), 11)
        
        theta = 'theta'
        self.assertEqual(theta.find('eta'), 2)
        self.assertEqual(theta.find('et'), 2)
        self.assertEqual(theta.find('the'), 0)
        self.assertEqual(theta.find('ha'), -1)      # Returns -1 on not in index


        self.assertTrue('lambda30'.isalnum())
        self.assertTrue('lambda'.isalnum())
        self.assertTrue('30'.isalnum())
        self.assertFalse('@'.isalnum())
        self.assertFalse('lambda_30'.isalnum())
        self.assertFalse(''.isalnum())
        self.assertFalse('Six lambdas'.isalnum())
        self.assertTrue('ΑβΓδ'.isalnum())
        self.assertTrue('20E1'.isalnum())

        # Example 1: Demonstrating the isapha() method:
        self.assertTrue("Moooo".isalpha())
        self.assertFalse('Mu40'.isalpha())

        # Example 2: Demonstrating the isdigit() method:
        self.assertTrue('2018'.isdigit())
        self.assertFalse("Year2019".isdigit())

        # Example 1: Demonstrating the islower() method:
        self.assertFalse("Moooo".islower())
        self.assertTrue('moooo'.islower())

        # Example 2: Demonstrating the isspace() method:
        self.assertTrue(' \n '.isspace())
        self.assertTrue(" ".isspace())
        self.assertFalse("mooo mooo mooo".isspace())

        # Example 3: Demonstrating the isupper() method:
        self.assertFalse("Moooo".isupper())
        self.assertFalse('moooo'.isupper())
        self.assertTrue('MOOOO'.isupper())

        # Demonstrating the join() method:
        self.assertEqual(",".join(["omicron", "pi", "rho"]), "omicron,pi,rho")
        self.assertEqual(" ".join(["omicron", "pi", "rho"]), "omicron pi rho")

        with self.assertRaises(TypeError):      # Will raise a TypeError requires a string in list
            " ".join(["omicron", 5 , "rho"])

        # Demonstrating the lower() method:
        self.assertEqual("SiGmA=60".lower(), 'sigma=60' )
        self.assertEqual("Γαβγδ".lower(), 'γαβγδ')

        # Demonstrating the lstrip() method:
        self.assertEqual(" tau ".lstrip(), "tau " )
        self.assertEqual(" tau ".rstrip(),  " tau")
        self.assertEqual("www.google.com".lstrip('w'), '.google.com')
        self.assertEqual("www.google.com".rstrip('m'), 'www.google.co')
        
        # Demonstrating the replace() method:
        self.assertEqual("www.netacad.com".replace("netacad.com", "pythoninstitute.org"), "www.pythoninstitute.org" )
        self.assertEqual("This is it!".replace("is", "are"), "Thare are it!")  # Replaces all instances of is with are
        self.assertEqual("This is it!".replace("is", "are", 1), "Thare is it!")  # Replaces only first instance of is with are
        self.assertEqual("Apple juice".replace("juice", ""), "Apple ")

        # Demonstrating the rfind() method, returns position on finding otherwise -1
        self.assertEqual("tau tau tau".rfind("ta"), 8)
        self.assertEqual("tau tau tau".rfind("ta", 9), -1)
        self.assertEqual("tau tau tau".rfind("ta", 3, 9), 4)
        self.assertEqual("tau tau tau".rfind("ta", 6, 9), -1)       # End here at char 8 stops at 9 excludes character a
        self.assertEqual("tau tau tau".rfind("ta", 6, 10), 8)       # Ends here at char 9 which includes ta at position 8

        # Demonstrating the rstrip() method:  Returns character if strip not successful
        # The chars argument is not a suffix; rather, all combinations of its values are stripped:
        self.assertEqual(" upsilon ".rstrip(), " upsilon")          # Defaults to removing white space from right
        self.assertEqual("cisco.com".rstrip(".com"), "cis")         
        self.assertEqual("cisco.com".rstrip("om"), "cisco.c")
        self.assertEqual("cisco.com".rstrip("o.com"), "cis")
        self.assertEqual("cisco.com".rstrip("c"), "cisco.com")
                
        self.assertEqual("mississippi".rstrip('ipz'), "mississ")
        
        # See str.removesuffix() for a method that will remove a single suffix string rather than all of a set of characters. For example:
        self.assertEqual("Monty Python".rstrip(" Python"), "M")
        self.assertEqual("Monty Pyton".removesuffix(" Pyton"), "Monty")
        
        # Demonstrating the split() method:
        self.assertListEqual("phi       chi\npsi".split(), ["phi", "chi", "psi"])
        self.assertEqual( " ".join(["phi", "chi", "psi"]), "phi chi psi")       # join is the opposite of split
        
        # Demonstrating the startswith() method:
        self.assertFalse("omega".startswith("meg"))
        self.assertTrue("omega".startswith("om"))
        # Demonstrating the strip() method: it makes a new string lacking all the leading and trailing whitespaces.
        self.assertEqual("   aleph   ".strip(), "aleph")

        # 
        # 2.3.1.16
        # Demonstrating the swapcase() method:
        self.assertEqual("I know that I know nothing.".swapcase(), "i KNOW THAT i KNOW NOTHING.")
        # Demonstrating the title() method:
        self.assertEqual("I know that I know nothing. Part 1.".title(), "I Know That I Know Nothing. Part 1.")
        # Demonstrating the upper() method:
        self.assertEqual("I know that I know nothing. Part 2.".upper(), "I KNOW THAT I KNOW NOTHING. PART 2.")

    """Section 2.3.1.18"""
    def testDevelopYourOwnSplit(self):
      
        def getChar(char = str()):
            if char.isprintable() and not char.isspace():
                return char
            else:
                return ""   
    
        """Check if string is a word"""
        def parseWords(phrase: str)->list:
            phraseAsList = list()
            word = str()
            for letter in phrase:
                initialResult = getChar(letter)
                if( len(initialResult)==0 and len(word)==0):
                    continue
                elif( len(initialResult)==0 and len(word)>0):
                    phraseAsList.append(word)
                    word = ""
                else:
                    word += initialResult
            if(len(word) > 0 ):
                phraseAsList.append(word)
            return phraseAsList
             
        
        romeo = "To be or not to be, that is the question"            
        # print(parseWords(romeo))
        mysplit = parseWords 
        
        self.assertListEqual(mysplit("To be or not to be, that is the question"), ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question'] )
        self.assertListEqual(mysplit("To be or not to be,that is the question"), ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question'])
        self.assertListEqual(mysplit("   "), [] )
        self.assertListEqual(mysplit(" abc "), ['abc'])
        self.assertListEqual(mysplit(""), [])

    """2.4.1 Comparing, sorting"""        
    def testStringComparison(self):
        # 2.4.1.1    
        self.assertTrue('alpha' == 'alpha')
        self.assertTrue('alpha' != 'Alpha') 
        self.assertTrue('alpha' < 'alphabet') 
        self.assertTrue('beta' > 'Beta')


        # 2.4.1.2 Do not do string comparison of numbers
        self.assertFalse('10' == '010')
        self.assertTrue('10' > '010')
        self.assertFalse('10' > '8')
        self.assertTrue('20' < '8')
        self.assertTrue('20' < '80')
        
        
        
        self.assertFalse('10' == 10, "A string == number is always False.")
        self.assertTrue('10' != 10, "A string != number is always True;")
        self.assertFalse('10' == 1,  "A string == number is always False.")
        self.assertTrue('10' != 1, "A string != number is always True;")
        with self.assertRaises(TypeError):  '10' > 10 # # string >= number always raises an exception.
           
    
        # 2.4.1.3 Sorting 
        first_greek = ['omega', 'alpha', 'pi', 'gamma']
        self.assertListEqual(sorted(first_greek), ['alpha', 'gamma', 'omega', 'pi'], "Use function to return sorted list.")
        
        first_greek.sort()
        self.assertListEqual(first_greek, ['alpha', 'gamma', 'omega', 'pi'], "Use string method to sort original list")

        self.assertEqual(str(13) + " " + str("1.3"), "13 1.3")

        self.assertEqual(int("13"), 13)
        self.assertEqual(float("1.3"), 1.3)
        
        with self.assertRaises(ValueError):
            int("foo")
        
        # 2.4.1.5 Section Summary
        self.assertTrue('smith' > 'Smith', "s > S in ascii" )
        self.assertFalse('Smiths' < 'Smith', "Last character compare s versus empty string. Emtpy is less")
        self.assertFalse("s" < "", "Empty should be character than string")
        self.assertTrue('Smith' > '1000', "Capial S bigger than string 1")
        self.assertTrue('11' < '8', "Ascii 1 is less than 8")
        self.assertTrue('1' < '8', "Ascii 1 is less than 8")
        self.assertTrue('12345' < '13467', "Ascii 2 is less than 3")
        self.assertTrue('52345' < '7', "Ascii 5 is less than 7")
        
        # s1 = 'Where are the snows of yesteryear?'
        # s2 = s1.split()
        # s3 = sorted(s2)
        # print(s3)
        # print(s3[1])
        
        # s1 = '12.8'
        # with self.assertRaises(ValueError):
        #     i = int(s1)         # Conversion causes ValueError 
        #     s2 = str(i)
        #     f = float(s2)
        # print(s1)
        # print(s2)
        # print(s1 == s2)
        
    """  2.4.1.6 LAB: A LED Display"""
    def testLEDDisplay(self):
        pass
        
    def testEuropeanBankStrings(self):
        # IBAN Validator.

        # British: GB72 HBZU 7006 7212 1253 00
        # French: FR76 30003 03620 00020216907 50
        # German: DE02100100100152517108
        
        def testEuro(input: str) -> bool:
            result = False
            # iban = input("Enter IBAN, please: ")
            iban = input
            iban = iban.replace(' ','')

            if not iban.isalnum():
                print("You have entered invalid characters.")
            elif len(iban) < 15:
                print("IBAN entered is too short.")
            elif len(iban) > 31:
                print("IBAN entered is too long.")
            else:
                iban = (iban[4:] + iban[0:4]).upper()
                iban2 = ''
                for ch in iban:
                    if ch.isdigit():
                        iban2 += ch
                    else:
                        iban2 += str(10 + ord(ch) - ord('A'))
                iban = int(iban2)
                if iban % 97 == 1:
                    # print("IBAN entered is valid.")
                    result = True
                else:
                    result = False
                    # print("IBAN entered is invalid.")

                return result

        self.assertTrue(testEuro("GB72 HBZU 7006 7212 1253 00"))
        self.assertTrue(testEuro("FR76 30003 03620 00020216907 50"))
        self.assertTrue(testEuro("GB72 HBZU 7006 7212 1253 00"))
    
    def testPalindrome(self):
        """_summary_
        Your task is to write a program which:

        asks the user for some text;
        checks whether the entered text is a palindrome, and prints result.
        Note:
            assume that an empty string isn't a palindrome;
            treat upper- and lower-case letters as equal;
            spaces are not taken into account during the check - treat them as non-existent;
            there are more than a few correct solutions - try to find more than one.
        """
        class Palindrome():
            def __init__(self, input: str) -> None:
                if type(input)==str:
                    self.inputString = self._simplifyString(input)
                    
                elif input is None:
                    self.inputString = ""
            
            def _simplifyString(self, input) -> str:
                return input.lower().replace(" ", "")
                        
            @property
            def palString(self):
                return self.inputString
            
            @palString.setter
            def palString(self, input: str):
                self.inputString = self._simplifyString(input)
            
            
            """Uses range decrementing and"""
            @property            
            def reversedString(self) -> str:
                newString = ""
                for x in range (len(self.inputString), 0,  -1):
                    newString += self.inputString[x-1]
                    
                newString = newString.lower()
                return newString   
            
            """Uses generator and format."""
            @property
            def reversedString1(self) -> str:
                endString = ""
                result = (x for x in self.inputString if x.isalnum() )
                print(result)
                

            """_summary_
            Uses generator
            revisit: tampham does not currently work

            Returns:
                _type_: _description_
            """
            @property
            def reversedString2(self) -> str:
                endString = ""
                result = (c.upper() for c in self.inputString if c.isalnum() )
                string = "{}".format(c.upper() for c in self.inputString if c.isalnum() )
                print(string)
                
                for c in result:
                    print(c, end = " ")
                return result


            """_summary_
            Uses reversed and join
            
            https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/

            Returns:
                _type_: _description_
            """
            @property
            def reversedString3(self) -> str:
                result =  "".join(reversed(self.inputString))
                return result
            7
            """
            Reverse a Python String: String Indexing
            """
            @property
            def reversedString4(self) -> str:
                result = self.inputString[::-1]
                return result
                                           
            def isPalindrome(self) -> bool:
                return( self.reversedString == self.inputString)
                           
        civic = "civic civic"
        level = "level"
        boot = "Too bad I hid a boot"
        palindromes = (civic, level, boot)
        for item in palindromes:
            pal = Palindrome(None)
            pal.palString = item
            self.assertTrue(pal.isPalindrome(), f"This is supposed to be a palindromes {pal.palString}: {pal.reversedString}")
        
        fox = "The long brown fox jumped over the lazy dog"
        cat = "The cat likes to sit around"
        hidden = "hide"
        notPalindromes = (fox, cat, hidden)
        for item in notPalindromes:
            pal = Palindrome(None)
            pal.palString = item
            self.assertFalse(pal.isPalindrome(), f"This is not supposed to be a palindromes {pal.palString}: {pal.reversedString}")
        
        pal = Palindrome("String of Characters")
        
    def testAnagram(self):
        
        # Anagram class with init that takes two inputs
        # Method that returns boolean isAnagram
        # private class that reorders, lowers case, each input
        # four? private variables that tracks original, and new inputs
        
        class Anagram():
            def __init__(self, input: str, input1: str) -> None:
                self._input = input
                self._input1 = input1
                self._formattedInput = ""
                self._formattedInput1 = ""


                if type(input)!= str or type(input1)!= str:
                    ValueError(f"Checkinputs {input} : {input1}")
        
                self._cleanInput1()
        
                """_summary_: Cleaning input here uses lower, replace, sorted, and string join
                Note that lower and replace are chained functions 
                Sorted and join are encapsulated functed calls one after the lower
                """
            def _cleanInput(self):
                self._formattedInput = "".join(sorted(self._input.lower().replace(" ", "")))
                self._formattedInput1 = "".join(sorted(self._input1.lower().replace(" ", "")))
        
            def _inputPipeline(self, input: str) -> str:
                b = (a for a in input)
                d = (c.lower() for c in b)
                f = (e.replace(" ", "") for e in d )
                g = sorted(f)
                finalResult = "".join(g)
                return finalResult
        
            """_summary_: Generator solution using 3 generators sorted and join
            """
            
            def _cleanInput1(self):
                self._formattedInput = self._inputPipeline(self._input)
                self._formattedInput1 = self._inputPipeline(self._input1)
                        
            def isAnagram(self) -> bool:
                return (self._formattedInput == self._formattedInput1)
                        
        ana = Anagram("input", "tupin")
        self.assertTrue(ana.isAnagram())
        
        ana = Anagram("foo", 'awful')
        self.assertFalse(ana.isAnagram())
        
        ana = Anagram("listen", " Sil ENt ")
        self.assertTrue(ana.isAnagram())
        
    
    """
    Scenario
        Some say that the Digit of Life is a digit evaluated using somebody's birthday. It's simple - you just need to sum all the digits of the date. If the result contains more than one digit, you have to repeat the addition until you get exactly one digit. For example:
        1 January 2017 = 2017 01 01
        2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
        1 + 2 = 3
        3 is the digit we searched for and found.

        Your task is to write a program which:

        asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY - actually, the order of the digits doesn't matter)
        outputs the Digit of Life for the date.

    Test your code using the data we've provided.
        19991229
        20000101
    # Class DigitOfLife
    # constructor takes string in data format
    # property lifeNumber getter and setter, getter will do calculation?, 
    # private string input
    # private string convertString
    # private integer _lifeNumber
    """
    
    def testDigitOfLife(self):
        class DigitOfLife():
            def __init__(self, input: str) -> None:
                self._lifeNumber = input

            def _conversion(self) -> int:
                inputData = self._lifeNumber   # Comes in as string
       
                
                while(len(inputData) >1):                
                    inputData = (int(x) for x in inputData)
                    inputData = (sum(inputData))                    
                    inputData = str(inputData)
                    # print(f"{inputData}:{len(inputData)}")
        
                return(int(inputData))

            @property
            def lifeNumber(self):
                result = self._conversion()
                return result
                
        lifeObject = DigitOfLife("20000101")
        self.assertEqual(lifeObject.lifeNumber, 4)
        lifeObject = DigitOfLife("19700128")
        self.assertEqual(lifeObject.lifeNumber, 1)
        lifeObject = DigitOfLife("19991229")
        self.assertEqual(lifeObject.lifeNumber, 6)
    
        
        
        
        
    """
    Objectives
    improving the student's skills in operating with strings;
    using the find() method for searching strings.

    Scenario
        Let's play a game. We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any characters.
        Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside the second string?

    For example:
        if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
        if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as there are neither the letters "d", "o", or "g", in this order)

    Hints:
        you should use the two-argument variants of the pos() functions inside your code;
        don't worry about case sensitivity.
    
    Test Data:
        donor
        Nabucodonosor
        yes
        
        donut
        Nabucodonosor
        no`
    
    """

    def testFindData(self):
        class FindData():
            def __init__(self, subString: str, largeString: str) -> None:
                self._originalSubString = subString
                self._originalLargeString = largeString
                self._cleanInput()
                self._order()    
            
            def _order(self):
                self.subString = self._inputPipeline(self.subString)
                self.largeString = self._inputPipeline(self.largeString)
                pass
                
            def isSubset(self) -> bool:
                setLarge = set(self.largeString)
                setSmall = set(self.subString)
                return setLarge.issuperset(setSmall)
            
            def _cleanInput(self):
                self.subString = "".join(sorted(self._originalSubString.lower().replace(" ", "")))
                self.largeString = "".join(sorted(self._originalLargeString.lower().replace(" ", "")))
                        
            def _inputPipeline(self, input: str) -> str:
                b = (a for a in input)
                d = (c.lower() for c in b)
                f = (e.replace(" ", "") for e in d )
                g = sorted(f)
                h = set(g)
                finalResult = "".join(h)
                return finalResult
        
        obj = FindData("donor", "Nabucodonosor")
        self.assertTrue(obj.isSubset())
        obj = FindData("donut", "Nabucodonosor")
        self.assertFalse(obj.isSubset())
        
    """
    Estimated time
    60-90 minutes
    
    Level of difficulty
    Hard

    Objectives
        improving the student's skills in operating with strings and lists;
        converting strings into lists.

    Scenario
    As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

        each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
        each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
        each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.

    If you need more details, you can find them here.
    Your task is to write a program which:
        reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
        outputs Yes if the Sudoku is valid, and No otherwise.

    Test your code using the data we've provided.
    Test data

    Sample input:

    295743861
    431865927
    876192543
    387459216
    612387495
    549216738
    763524189
    928671354
    154938672

    Sample output:
    Yes


    Sample input:

    195743862
    431865927
    876192543
    387459216
    612387495
    549216738
    763524189
    928671354
    254938671


    1 9 5 7 4 3 8 6 2
    4 3 1 8 6 5 9 2 7
    8 7 6 1 9 2 5 4 3
    3 8 7 4 5 9 2 1 6
    6 1 2 3 8 7 4 9 5
    5 4 9 2 1 6 7 3 8
    7 6 3 5 2 4 1 8 9
    9 2 8 6 7 1 3 5 4
    2 5 4 9 3 8 6 7 1


    Sample output:
    No
    
    ClassDesign
    Soduku Puzzle takes a list of 9x9 list of numbers
    It will convert it to a list of list numbers
    
    Class SodukuPuzzle
    init will take list
    _convert will convert list to two dimensional
    _originalList
    _formattedList
    
    isSolution will return valid soduku
        
    """
    def testSoduku(self):        

        class SodukuPuzzle():
            def __init__(self, input: list):
                self._originalList = input
                self._convert()
                
            def _convert(self):
                295743861
            
            def isSolution(self) -> bool:
                vertical = False
                horizontal = False
                threeByThree = False

                self.verticalValues = (self._createVertical())
                for val in self.verticalValues:
                    if len(val) != 9:
                        vertical = False
                        break
                    else:
                        vertical = True
                        continue
                    
                self.horizontalValues = (self._createHorizontal())
                
                for val in self.horizontalValues:
                    if len(val) != 9:
                        horizontal = False
                        break
                    else:
                        horizontal = True
                        continue
                
                self.threeByThreeValues = self._createThreeByThree()
                
                for val in self.threeByThreeValues:
                    myInt = int(val)
                    sumOfGroup = sum(self._digits(myInt))
                    if len(val) != 9 or sumOfGroup != 45:
                        threeByThree = False
                        break
                    else:
                        threeByThree = True
                        continue
                
                
                if (horizontal and vertical and threeByThree):
                    return True
                else:
                    return False
            
            def _createHorizontal(self):    
                gen = (self._digits(val) for val in self._originalList)
                horizontalValues =  [list(val) for val in gen]
                self._unorderedHorizontalValues = horizontalValues
                self._unorderedHorizontalTotals = [sum(val) for val in self._unorderedHorizontalValues]
             
                gen = (self._digits(val) for val in self._originalList)
                list2d =  [set(val) for val in gen]
                
                return list2d
           
            """generator which returns digits in left to right order"""
            def _digits(self, n):
                from math import floor, log10
                k = floor(log10(n))
                for e in range(k,-1,-1):
                    d,n = divmod(n,10**e)
                    yield d    
                    
            def _elementsOfList(self, myList, n):
                for whichList in range(9):
                    number = myList[whichList][n]
                    yield number

            def _createVertical(self):
                list1d = [list(self._digits(val)) for val in self._originalList]
                list2d = list()
          
                for inc in range(9):
                    list2d.append(set(self._elementsOfList(list1d, inc)))
                                
                self._unorderedVerticalValues = list()
                for inc in range(9):
                    self._unorderedVerticalValues.append(list(self._elementsOfList(list1d, inc)))
                self.unorderedVerticalTotals = list()
                for inc in range(9):
                    self.unorderedVerticalTotals.append(sum(list(self._elementsOfList(list1d, inc))))
                return list2d

            def _loadThreebyThree(self, myList, n):
                for whichList in myList:
                    number = myList[whichList][n]
                    yield number                

            def _createThreeByThree(self):
                list1d = [str(val) for val in self._originalList]
                self._ThreeByThree = set()
                self._ThreeByThree.add(list1d[0][0:3] + list1d[1][0:3] + list1d[2][0:3])
                self._ThreeByThree.add(list1d[0][3:6] + list1d[1][3:6] + list1d[2][3:6])
                self._ThreeByThree.add(list1d[0][6:9] + list1d[1][6:9] + list1d[2][6:9])
 
                self._ThreeByThree.add(list1d[3][0:3] + list1d[4][0:3] + list1d[5][0:3])
                self._ThreeByThree.add(list1d[3][3:6] + list1d[4][3:6] + list1d[5][3:6])
                self._ThreeByThree.add(list1d[3][6:9] + list1d[4][6:9] + list1d[5][6:9])
  
                self._ThreeByThree.add(list1d[6][0:3] + list1d[7][0:3] + list1d[8][0:3])
                self._ThreeByThree.add(list1d[6][3:6] + list1d[7][3:6] + list1d[8][3:6])
                self._ThreeByThree.add(list1d[6][6:9] + list1d[7][6:9] + list1d[8][6:9])
                
                mySet = set(self._ThreeByThree)
                
                return self._ThreeByThree

        goodSudoku = [295743861,
                      431865927,
                      876192543,
                      387459216,
                      612387495,
                      549216738,
                      763524189,
                      928671354,
                      154938672]
        obj = SodukuPuzzle(goodSudoku)
        self.assertTrue(obj.isSolution())

        badSudoku = [195743862,
                     431865927,
                     876192543,
                     387459216,
                     612387495,
                     549216738,
                     763524189,
                     928671354,
                     254938671]
        obj = SodukuPuzzle(badSudoku)
        self.assertFalse(obj.isSolution())
    
    """  
    2.6.1.1 Errors - the programmer's daily bread
    """
    def testErrors(self):
        with (self.assertRaises(TypeError)):
            from math import sqrt
            sqrt("s")
            
        with (self.assertRaises(ZeroDivisionError)):
            3/0 
        
        with (self.assertRaises(IndexError)):
            myList = list()
            x = myList[0]
        
        try:
            val = "s"
            from math import sqrt
            sqrt(val)
        except TypeError:
            self.assertTrue("Caught TypeError")
            # Tr to convert to ord
            self.assertAlmostEqual(sqrt (ord(val)), 10.7238052, places=5)
                               
        try:
            x = int("3")
            y = 1 / x    # success
            3/0          # ZeroDivisionError
        except ZeroDivisionError:
            self.assertTrue(True, "Hit here due to 3/0")
    
        with (self.assertRaises(NameError)):
            raise NameError("Generate error")

        with (self.assertRaises(ZeroDivisionError)):
            "alpha"[1/0]            # Division occurs first before index into string
    

        with (self.assertRaises(BaseException)):        # General exception
            1/0
        with (self.assertRaises(ArithmeticError)):      # Inherits from base
            1/0
        with (self.assertRaises(ZeroDivisionError)):    # Specific and inherits from ArithmeticError
            1/0
        
        with self.assertRaises((BaseException, ArithmeticError, ZeroDivisionError)):    # Specific and inherits from ArithmeticError
            1/0
        
        try:
            result = list(1,2,3,4)
            result[10]
            1/0
        except (ZeroDivisionError, TypeError):
            self.assertTrue("Captures either error")
        
        with self.assertRaises(ArithmeticError):
            raise(ArithmeticError)
      
      
        """
        ArithmeticError
        Location: BaseException ← Exception ← ArithmeticError
        Description: an abstract exception including all exceptions caused by arithmetic operations like zero division or an argument's invalid domain
        """  
        
        with self.assertRaises(AssertionError):
            assert ""     # Assert on empty string
        
        with self.assertRaises(AssertionError):
            assert False  # Assert on False
                
        with self.assertRaises(AssertionError):
            assert None   # Assert on None
        
        from math import tan, radians

        """
        AssertionError

        Location: BaseException ← Exception ← AssertionError

        Description: a concrete exception raised by the assert instruction when its argument evaluates to False, None, 0, or an empty string
        """
        with (self.assertRaises(AssertionError)):
            angle = 270
            assert angle % 180 != 90     # We must be sure that angle != 90 + k * 180
            # print(tan(radians(angle)))



        """
        BaseException
        Location: BaseException
        Description: the most general (abstract) of all Python exceptions - all other exceptions are included in this one;
        it can be said that the following two except branches are equivalent: except: and except BaseException:.
        """

        """
        IndexError
        Location: BaseException ← Exception ← LookupError ← IndexError
        Description: a concrete exception raised when you try to access a non-existent sequence's element (e.g., a list's element)
        """
        with (self.assertRaises(IndexError)):
            myData = (32, 10, 12)
            myData[4]
    
        """
        KeyboardInterrupt
        Location: BaseException ← KeyboardInterrupt
        Description: a concrete exception raised when the user uses a keyboard shortcut designed to terminate a 
        program's execution (Ctrl-C in most OSs); if handling this exception doesn't lead to program termination, 
        the program continues its execution.
        Note: this exception is not derived from the Exception class. Run the program in IDLE.
        """
    
        # with (self.assertRaises(KeyboardInterrupt)):
        #     import sys
        #     from subprocess import call
        #     try:
        #         call([sys.executable, 'process.py'], start_new_session=True)
        #     except KeyboardInterrupt:
        #         print('[Ctrl C],KeyboardInterrupt exception occured.')
        #     else:
        #         print('No exception')


        """
        LookupError
        Location: BaseException ← Exception ← LookupError
        Description: an abstract exception including all exceptions caused by errors resulting from invalid references to 
        different collections (lists, dictionaries, tuples, etc.)
        """

        """
        MemoryError
        Location: BaseException ← Exception ← MemoryError
        Description: a concrete exception raised when an operation cannot be completed due to a lack of free memory. 
        """
        # with (self.assertRaises(MemoryError)):
        #     # This code causes the MemoryError exception.
        #     # Warning: executing this code may affect your OS.
        #     # Don't run it in production environments!
        #     string = 'x'
        #     try:
        #         while True:
        #             string = string + string
        #             print(len(string))
        #     except MemoryError:
        #         print('This is not funny!')

        """
        OverflowError
        Location: BaseException ← Exception ← ArithmeticError ← OverflowError
        Description: a concrete exception raised when an operation produces a number too big to be successfully stored
        """
        with (self.assertRaises(OverflowError)):
            # The code prints subsequent
            # values of exp(k), k = 1, 2, 4, 8, 16, ...
            
            from math import exp
            
            from io import StringIO
            from contextlib import redirect_stdout   # Redirect print output
            ex = 1
            while True:
                text_trap = StringIO()
                with redirect_stdout(text_trap):
                    print(exp(ex))
                    ex *= 2

        """
        ImportError
        Location: BaseException ← Exception ← StandardError ← ImportError
        Description: a concrete exception raised when an import operation fails
        """
        with (self.assertRaises(ImportError)):
            # One of these imports will fail - which one?
            import math
            import time
            from math import invalidFunction
            
            
        """
        KeyError
        Location: BaseException ← Exception ← LookupError ← KeyError
        Description: a concrete exception raised when you try to access a collection's non-existent element (e.g., a dictionary's element)
        """
        # How to abuse the dictionary
        # and how to deal with it?
        with (self.assertRaises(KeyError)):
            dictionary = { 'a': 'b', 'b': 'c', 'c': 'd' }
            ch = 'a'
            while True:
                ch = dictionary[ch]
                # print(ch)



    """
    Section:  2.8.1.4 Reading ints safely
    
    Estimated time
        15-25 minutes

    Level of difficulty
        Medium

    Objectives
        improving the student's skills in defining functions;
        using exceptions in order to provide a safe input environment.

    Scenario
        Your task is to write a function able to input integer values and to check if they are within a specified range.

        The function should:

            accept three arguments: a prompt, a low acceptable limit, and a high acceptable limit;
            if the user enters a string that is not an integer value, the function should emit the message Error: wrong input, 
                and ask the user to input the value again;
            if the user enters a number which falls outside the specified range, 
                the function should emit the message Error: the value is not within permitted range (min..max) 
                and ask the user to input the value again;
            if the input value is valid, return it as a result.

    Test data
        Test your code carefully.

        This is how the function should react to the user's input:
        Enter a number from -10 to 10: 100
        Error: the value is not within permitted range (-10..10)
        Enter a number from -10 to 10: asd
        Error: wrong input
        Enter number from -10 to 10: 1
        The number is: 1

    Class Design
        IntegerInput
        __init__ integer, min range, max range
        
        function to check range
            _checkRange
            _checkMainValue
            
            Return valueError 
        
    """
    def testReadIntHandleExceptions(self):
        
        class IntegerInput():
            def __init__(self, inputNumber: str, min: str, max: str) -> None:
                self._inputNumber = inputNumber
                self._inputMin = min
                self._inputMax = max
                self._validNumber = self._strIntConversion(inputNumber)
                self._min = self._strIntConversion(min)
                self._max = self._strIntConversion(max)
                return None

            def _checkRange(self) -> bool:
                result = False
                try: 
                    assert (self._validNumber > self._min)
                    result = True
                except AssertionError:
                    # print(f"Number below range {self._validNumber} < {self._min}")
                    result = False
                except TypeError:
                    # print(f"This is not a valid number: {self._validNumber}")
                    result = False
                                             
                try:
                    assert (self._validNumber < self._max)
                    result = True
                except AssertionError:
                    # print(f"Number above range {self._validNumber} > {self._max}")
                    result = False
                except TypeError:
                    # print(f"This is not a valid number: {self._validNumber}")
                    result = False
                return result
            
            def _strIntConversion(self, input) -> int:
                result = None
                
                try:
                    number = int(input)
                    result = number                    
                except ValueError:
                    # print("Invalid entry for number")
                    result = None
                return result
        
            def isNumber(self) -> bool:
                result = False
                try:
                    if(type(self._validNumber) == int):
                        result = True
                except ValueError:
                    # print("Invalid entry for number")
                    result = False
                return result
        
        obj = IntegerInput("10", "0", "100")
        # self.assertIsNone(IntegerInput("10", "0", "100"))
        self.assertTrue(obj.isNumber())
        self.assertTrue(obj._checkRange())
        
        obj = IntegerInput("s", "0", "100")
        self.assertFalse(obj._checkRange())
        
    def testSection2(self):
        self.assertEqual(len("\'"), 1, "String here is only one since backslash escapes the quote")
     
        
if __name__ == "__main__":
    unittest.main()
    
    