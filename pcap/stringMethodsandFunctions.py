import unittest
import string


class TestStrings(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def testCap(self):
        t2 = "dog".capitalize()
        self.assertEqual(t2, "Dog", "Capitalize first word")
    
        t3 = "ALL".casefold()
        self.assertEqual(t3, "all", "Casefold is aggrevise ")
    
    
    def testFind(self):
        result = "This is a test of the emergency".find("is", 0)
        self.assertEqual(result, 2, "Finds the first is as part of This")
        result = "This is a test of the emergency".find("is", 5, 10)
        self.assertEqual(result, 5, "Finds the second free standing is since tart at index 5")

        result = "This is a test of the emergency".rfind("is")
        self.assertEqual(result, 5, "Using rfind or find from right")


        myString = "My String is For Experimentation"
        result = myString[50:80]
        self.assertEqual(result, "", "returns empty string because out of index")

        result = myString[-16:-1  ]
        print(result)
        # self.assertEqual(result, "Experimentation")

        result = myString[0:9]
        self.assertEqual(result, "My String")


if __name__ == "__main__":
    unittest.main()