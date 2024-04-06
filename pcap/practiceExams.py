from typing import Any
import unittest


class PCAPPracticeExams(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def testSection3Strings(self):
        result = "Flash Gordon".rfind("ash")
        self.assertEqual(result, 2, "Found ash in starting in second index")
        
        result = "Flash Gordon".index("ash")
        self.assertEqual(result, 2, "Found ash in starting in second index")

        result = "Flash Gordon".find("ash")
        self.assertEqual(result, 2, "Found ash in second starting position ")
           

        letters = 'xyz'
        
        new_string = sorted(letters)
        self.assertListEqual(new_string, ['x', 'y', 'z'], "sorted function converts string to list")

        new_string = sorted(letters, reverse=True)
        self.assertListEqual(new_string, ['z', 'y', 'x'], "sorted with reverse")

        new_string = ''.join(sorted(letters))
        self.assertEqual(new_string, 'xyz')

        10 == '1' + '0'     # Comparing integers to string always returns false
        self.assertFalse(10 == '1' + '0')

        self.assertTrue('9' * 3 < '9' * 9, "'999' is less than '999999999'")


        self.assertFalse('123' in '1-2-3')

        self.assertTrue('a' in  'abc')
        self.assertFalse('a' not in  'abc')
        self.assertTrue(not ('a' not in 'abc'))

        # with self.assertRaises(SyntaxError):
        #     str = '\'
        # with self.assertRaises(SyntaxError):
        #     str = 'All the King's Horses'
        # with self.assertRaises(SyntaxError):
        #     str = "All the King"s Hourses"
        str = "All the King's Horses"
        str = 'All the King"s Horses'
    
  
  
  
        class A():
            pass
        
        class B(A):
            pass
        
        aInst = A()
        bInst = B()
        self.assertTrue(isinstance(bInst, A))
        self.assertTrue(isinstance(aInst, A))
        
        self.assertTrue(issubclass(B,A))
        self.assertTrue(issubclass(B,B))
        self.assertFalse(issubclass(A, B))


        # MRO 
        # Inside the object, bottom to top, left to right
        # with self.assertRaises(TypeError): # , "Inheritnace MRO not support for class C"):        
        #     class A:
        #         pass
        #     class B(A):
        #         pass
        #     class C(A, B):
        #         pass
        #     o = C()


    def testSection4Classes(self):
        class BluePrint:
            __element = 1
            def __init__(self) -> None:
                self.component = 1
            def __action(self): pass
        product = BluePrint()
        
        self.assertEqual(product._BluePrint__element, 1, "Access private property or varbile of class use obj._classname__varabile")        
        self.assertEqual(product.component, 1)
        
        self.assertEqual(BluePrint._BluePrint__element, 1,"Changes class variable")
        
        BluePrint._BluePrint__element = 3
        self.assertEqual(product._BluePrint__element, 3, "Access private property or varbile of class use obj._classname__varabile")        
        self.assertEqual(BluePrint._BluePrint__element, 3,"Changes class variable")
            
            
        class Storage():
            def __init__(self) -> None:
                self.rack = 1
            def get(self):
                return self.rack
            def print(self):
                print(self.get())
                print(Storage.get(self))
                print(super().space)
            
        stuff = Storage()
                     
        # Need to review __base__  
        # https://docs.python.org/3/reference/datamodel.html
        # __bases__
        #     A tuple containing the base classes, in the order of their occurrence in the base class list.
        class A:
            pass
        class B(A):
            pass
        class C(A):
            pass
        
        class D(B,C,A):
            pass
            
        self.assertTrue(A in B.__bases__, "A is in B bases tuple")
        self.assertTrue(A in C.__bases__, "A is in C bases tuple")
        self.assertTrue(A in D.__bases__, 'A is in D bases tuple')
        self.assertFalse(D in A.__bases__, "D is not in A bases tuple")
        # self.assertTrue('__dict__' in D.__dict__)    
        d = D()
        
        class Class:
            class_var = 1
            def __init__(self) -> None:
                self.instance_var = 1
            def method(self):
                pass
        object = Class()
        self.assertTrue('__dict__' in Class.__dict__)    
        self.assertEqual(len(object.__dict__), 1)
        object.newVar = 3
        self.assertEqual(len(object.__dict__), 2)
        self.assertTrue('newVar' in object.__dict__)        
        pass
        
        
                                
                
    def testMisc(self):
        list_x = A = [1, 2, 3]
        B = [4,5,6]
        
        map(lambda x: x * x, list_x)
        result = map(lambda x: x*x, A)
        result = map(lambda x: x*x, range(4))
                
        # for element in result:
        #     print(element, end= ' ')
        # print("")
       
        # result = list(filter(lambda x: x%2 == 0   , range(10)))
        # for element in result:
        #     print(element, end= ' ')
        
        # Closures
        def define_mark(mark):
            opening_mark = mark
            closing_mark = mark.replace("<", "</")
            
            def embed(text):
                return opening_mark + text + closing_mark

            return embed
        bold = define_mark("<b>")
        italic = define_mark("<i>")

        self.assertEqual(bold(italic("The Heading")), "<b><i>The Heading</i></b>")

        foo = [x for x in range(4)]   # foo = [0,1,2,3]
        spam = [x for x in foo[1:-1]]  # spam [1, 2]
        self.assertEqual(spam, [1,2], "Takes only center")
        self.assertEqual(spam[1], 2,)
        
        neg_spam = [x for x in foo[-3:-1]]  # neg_spam [1, 2]
        self.assertEqual(neg_spam, [1,2], "Index from right")
        
    

        def fun(x):
            assert x >= 0
            return x ** 0.5
        
        def mid_level(x):
            try:
                fun(x)
            except Error:  # type: ignore # Error is not defined Generates a NameError
                raise
        
        try:
            x = mid_level(-1)
        except RuntimeError:
            x = -1
        except NameError as ex:
            try:
                print(ex.message)
            except:
                pass
            else:
                print(ex)
            finally:
                print(ex.args)
            
            print(type(ex))
            x = -2
        print(x)
    
        self.assertFalse(10 == '1' + '0', "Equality always returns false between string and int")  
        self.assertFalse(1000 == '5', "Returns False for string versus int comparison")
        self.assertTrue(1000 != '5', "They are not equal")
                
        with self.assertRaises(TypeError, msg="Inequality is not supported between string and int"):
            'g'*1 <= 1*2   
                
        pass
    
        foo = "Mary has 21 little sheep"
        self.assertTrue(foo.split()[2].isdigit(), "Check if[2] element which is 21 is a digit. Which is True since string 21 is a digit") 
        
        # The readlines() method returns a list containing each line in the file as a list item.
        # The readline() method returns one line from the file.
    
    def testFinalExam(self):
        with self.assertRaises(ValueError, msg="Can not initialzie a float with string"):
            float("foo")
            
        # Slicing a string won't cause an assert if the slice is out of bounds
        foo = "This is a string"
        result = foo[3:1000]
        print(result)
        pass 
    
        with self.assertRaises(AttributeError, msg = "String does not have sort method"):
            "321".sort()
        
        myList = ['f', 'c', 'g']
        myList.sort()
        self.assertEqual( myList  , ['c', 'f', 'g'])
    
        self.assertEqual("".join(sorted("321")), "123", msg="Call function sorted and string join")
        self.assertEqual("".join(sorted('abc', reverse=True)), "cba", msg="Call function seroted in reverse order and join ")
    
    
        pairs = [[2, 1], [-2, -1]]
        another_pair = sorted(pairs) # Results in [[-2,-1], [2, 1]]
        self.assertEqual(list(another_pair), [[-2,-1], [2, 1]])
        
        
        new_pairs = map(lambda p: sorted(p), pairs)   # Results in [[1,2], [-1, -2]]
        self.assertEqual(list(new_pairs)[0][0], 1)
        
        self.assertTrue(bool(lambda: False if False else True))
        self.assertTrue(bool(lambda: True if True else True))
        self.assertTrue(bool(lambda: True if False else True))
        self.assertTrue(bool(lambda: False if True else True))
    
    
if __name__ == "__main__":
    unittest.main()