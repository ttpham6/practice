import unittest
import keyword


class TestKeyWords(unittest.TestCase):
    def testKeyWordList(self):
        print(len(keyword.kwlist))
        print(keyword.kwlist)
        print(len(keyword.softkwlist))
        print(keyword.softkwlist)


    def testIf(self):
        if (True):
            pass

    def testMatchCaseStatement(self):
        # https://www.geeksforgeeks.org/python-match-case-statement/
        import keyword
        input = ("Bill", "Sara", "Jane", "Test")
        input = "Sara"

        match input:
            case "Bill":
                print("Bill")
            case "Sara":
                print("Sara")
            case "Jane":
                print("Jane")
            case "Test":
                print("Test")
            case _:
                print("Invalid user")







if __name__ == "__main__":
    unittest.main()
