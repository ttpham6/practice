import unittest




class TestComprehensions(unittest.TestCase):
        
    def testGeneral(self):
        from random import randint
        bottomBound = 0
        topBound = 5
        data = [randint(bottomBound,topBound) for x in range(10)]
        data = (randint(bottomBound,topBound) for x in range(10))
        for x in data:
            self.assertGreaterEqual(x, 0, f"Range check {bottomBound}")
            self.assertLessEqual(x, 5, f"Range check {topBound}")

        bottomBound = 0
        topBound = 1000
        data1 = {randint(bottomBound,topBound) for x in range(100)}
        # print(f"({data1} | {len(data1)}"  )
        # print(type(data1))

        data3 = [x for x in range(20)]
        # print(f"{type(data3)} |  {len(data3)} | {data3}")
        pass


        # https://stackoverflow.com/questions/43808180/python-3-x-list-comprehension-vs-tuple-generator

class TestListMethods(unittest.TestCase):
    
    def testAppend(self):
        myList = list(range(1,5))
        self.assertEqual(myList, [1,2,3,4])
        myList.append('A')
        self.assertEqual(myList, [1,2,3,4,'A'])
        self.assertEqual(myList.count(3), 1)
        self.assertEqual(myList.copy().count('A'), 1)
        self.assertEqual(myList.count('A'), 1)

        myList2 = myList.copy()
        myList2.remove(1)
        self.assertEqual(myList2, [2,3,4, 'A'])

        myList.extend(myList2)
        self.assertEqual(myList, [1,2,3,4,'A', 2,3,4,'A'])
    
        self.assertEqual(myList.index('A'), 4)
    
        myList.insert(5, 'B')
        self.assertEqual(myList[5], 'B')

        pass
    
        myList.pop()
        self.assertEqual(myList, [1,2,3,4,'A', 'B', 2,3,4])
        myList.pop(0)
        self.assertEqual(myList, [2,3,4,'A', 'B', 2,3,4])


        # self.assertEqual(myList, [2,2,3,3,4,4,'A','B'])
        myList.remove('A')
        myList.pop()  # Removes 4 at the bottom
        myList.remove('B')
        self.assertEqual(myList, [2,3,4,2,3])
            
        myList.sort(reverse=True)
        self.assertEqual(myList, [4,3,3,2, 2])
                      
        import string
        myList1 = list(string.ascii_lowercase)
        pass 



if __name__ == "__main__":
    unittest.main()