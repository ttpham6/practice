# https://docs.python.org/3/library/functions.html


import unittest

class TestBuiltIns(unittest.TestCase):

    def testAbs(self):
        self.assertEqual(7, abs(-7))
        self.assertEqual(7, abs(7))
        with self.assertRaises(TypeError):
             abs("string")

    def testAll(self):
        data = (True,True, True)
        data1 = (True, False)
        self.assertTrue(all(data))
        self.assertFalse(all(data1))
       
    def testAny(self):
        data = (True,True, True)
        data1 = (True, False)
        data2 = (False, False)
        self.assertTrue(any(data))
        self.assertTrue(any(data1))
        self.assertFalse(any(data2))
        self.assertFalse(any(list()))

    def testSum(self):
        data = list(x for x in range(1,6))
        self.assertEqual(sum(data), 15)
        
    def testFrozenSet(self):
        data = frozenset(x for x in range(1,6))
        with self.assertRaises(TypeError):
            data[3] = 3
            
    def testAscii(self):
        self.assertEqual(type(ascii(3)), str, msg="Show str representation of object similar to repr")
              
    def testMinMaxOrdChr(self):
        from string import ascii_lowercase, ascii_uppercase
    
        result = [ord(char) for char in ascii_uppercase]
        
        self.assertEqual(max(result), 0x5A, "ord Z hex value")
        self.assertEqual(max(result), 90,"ord Z decimal value")
        self.assertEqual(min(result), 0x41, "Order A hex value")
        self.assertEqual(min(result), 65, "Ord A decimal value")
       
        # Use list comprehension
        result = [ord(char) for char in ascii_lowercase]
        self.assertEqual(max(result), 0x7A, "ord z hex value")
        self.assertEqual(max(result), 122, "ord z decimal value")
        self.assertEqual(min(result), 0x61, "ord a hex value")
        self.assertEqual(min(result), 97, "ord a decimal value")

        # Use map with lambda function
        result = list(map(lambda x: ord(x), ascii_lowercase))
        self.assertEqual(max(result), 0x7A, "ord z hex value")
        self.assertEqual(max(result), 122, "ord z decimal value")
        self.assertEqual(min(result), 0x61, "ord a hex value")
        self.assertEqual(min(result), 97, "ord a decimal value")


        # Using generators to generate ascii representation 0-9
        # Pointless conversion from  number, to character number, back to number via ord 
        result = (n for n in range(0x30, 0x3A))
        result1 = (chr(num) for num in result)
        result2 = list((ord(char) for char in result1))
        self.assertEqual(min(result2), 0x30, "ord 0 hex value")
        self.assertEqual(min(result2), 48, "ord 0 decimal value")

        # Go from string to ord number
        from string import digits
        result = [ord(char) for char in digits]
        self.assertEqual(max(result), 0x39, "Ord 9 hex value")
        self.assertEqual(max(result), 57, "Ord 9 digital value")
        self.assertEqual(min(result), 0x30, "Ord 0 hex value")
        self.assertEqual(min(result), 48, "Ord 9 digital value")



    def testdir(self):
        # print(dir())
        # print(dir(int))
        import struct
        # print(dir())
        print(dir(struct))

        import zipfile
        print(zipfile)
        print(dir(zipfile))
        # pass
        # print(dir(str))
        # pass
        # import math
        # print(dir(math))
        # print(math.__doc__)
        # print(math.__annotations__)
        pass
        # dir(float)

# The principal built-in types are numerics, sequences, 
# mappings, classes, instances and exceptions.
# There are 6 sequence data types in Python, 
# namely strings, byte sequences, byte arrays, 
# lists, tuples, and range objects.

def main():
    unittest.main()


if __name__ == "__main__":
    main()