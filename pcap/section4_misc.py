import unittest

import warnings

def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ResourceWarning)
            test_func(self, *args, **kwargs)
    return do_test


class Section4MiscPythonFeatures(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
            
    # def testDecorator(self):
    #     def my_decorator_func(func):

    #         def wrapper_func():
    #             # Do something before the function.
    #             func()
    #             # Do something after the function.
    #             return wrapper_func
            
    #     from datetime import datetime
    #     def log_datetime(func):
    #         '''Log the date and time of a function'''

    #         def wrapper():
    #             print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
    #             print(f'{"-"*30}')
    #             func()
    #         return wrapper

    #     @log_datetime
    #     def daily_backup():

    #         print('Daily backup job has finished.')   

            
    #     daily_backup()
    def testFibonacciIterator(self):
        class Fib:
            def __init__(self, nn):
                print("__init__")
                self.__n = nn
                self.__i = 0
                self.__p1 = self.__p2 = 1

            def __iter__(self):
                print("__iter__")
                return self

            def __next__(self):
                print("__next__")				
                self.__i += 1
                if self.__i > self.__n:
                    raise StopIteration
                if self.__i in [1, 2]:
                    return 1
                ret = self.__p1 + self.__p2
                self.__p1, self.__p2 = self.__p2, ret
                return ret

        # for i in Fib(10):
        #     print(i)

    def testFibonacciClass(self):
        class Fib:
            def __init__(self, nn):
                self.__n = nn
                self.__i = 0
                self.__p1 = self.__p2 = 1

            def __iter__(self):
                print("Fib iter")
                return self

            def __next__(self):
                self.__i += 1
                if self.__i > self.__n:
                    raise StopIteration
                if self.__i in [1, 2]:
                    return 1
                ret = self.__p1 + self.__p2
                self.__p1, self.__p2 = self.__p2, ret
                return ret

        class Class:
            def __init__(self, n):
                self.__iter = Fib(n)

            def __iter__(self):
                print("Class iter")
                return self.__iter;

        object = Class(8)

        # for i in object:
        #     print(i)

    def testYield(self):
        def fun(n):
            for i in range(n):
                yield i

        # for v in fun(5):
        #     print(v)

    def testGeneratorsClosures(self):
        def powers_of_2(n):
            power = 1
            for i in range(n):
                yield power
                power *= 2

        # for v in powers_of_2(8):
        #     print(v)

        # data = list(powers_of_2(8))
        # print(data)
        def powers_of_2(n):
            power = 1
            for i in range(n):
                yield power
                power *= 2

        # for i in range(20):
            # if i in powers_of_2(4):
            #     print(i)

        def fibonacci(n):
            p = pp = 1
            for i in range(n):
                if i in [0, 1]:
                    yield 1
                else:
                    n = p + pp
                    pp, p = p, n
                    yield n

        fibs = list(fibonacci(10))
        # print(fibs)

    def testListComprehension(self):
        list_1 = []

        for ex in range(6):
            list_1.append(10 ** ex)

        list_2 = [10 ** ex for ex in range(6)]

        self.assertEqual(list_1, list_2, "Creating a list with list comprehension")
        # print(list_1)

        the_list = []
        for x in range(10):
            the_list.append(1 if x % 2 == 0 else 0)
       
        self.assertEqual(the_list, [1, 0, 1, 0, 1, 0, 1, 0, 1, 0])
       
       
        the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
        the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

        # for v in the_list:
        #     print(v, end=" ")
    
        from types import GeneratorType
        self.assertIsInstance(the_generator, GeneratorType)
    
        self.assertEqual(the_list, list(the_generator), "Generator creates same content as list comprehension")
        # for v in the_generator:
        #     print(v, end=" ")
    
    def testLambdas(self):
        two = lambda: 2
        sqr = lambda x: x * x
        pwr = lambda x, y: x ** y

        self.assertEqual(two(), 2)
        self.assertEqual(sqr(2), 4)
        self.assertEqual(pwr(2,3), 8)

        # for a in range(-2, 3):
        #     print(sqr(a), end=" ")
        #     print(pwr(a, two()))


        def print_function(args, fun):
            for x in args:
                print('f(', x,')=', fun(x), sep='')


        def poly(x):
            return 2 * x**2 - 4 * x + 2


        # print_function([x for x in range(-2, 3)], poly)
        lambda x: 2 * x**2 - 4 * x + 2
        # print_function([x for x in range(-2,3)], lambda x: 2 * x**2 - 4 * x + 2)
        result = [lambda x: 2 * x**2 - 4 * x + 2 for x in range(3)]
        
        
        list_1 = [x for x in range(5)]
        list_2 = list(map(lambda x: 2 ** x, list_1))
        self.assertEqual(list_2, [1, 2, 4, 8, 16], "# Map functions return a generator from inputs of function and list")

        #filteredData = (filter(lambda x: x%2) for x in range(20))
        # filteredData = filter(lambda x: x%2 is 0, range(20))
        # for x in filteredData:
        #     print(x, end=" ")
            
            
        a = "Hello"
        b = "Hello"
        self.assertEqual(id(a), id(b))
        
        a = a + " Phil!"
        self.assertNotEqual(id(a), id(b))

        inc = 0
    
    def testClsoures(self):    
         # Closures
        def outer(par):
            loc = par

            def inner():
                return loc
            return inner

        var = 1
        fun = outer(var)
        self.assertEqual(fun(), 1, "Inner function stores variable loc.")

        def make_closure(par):
            loc = par

            def power(p):
                return p ** loc
            return power

        fsqr = make_closure(2)
        fcub = make_closure(3)

        for i in range(5):
            self.assertEqual(fsqr(i), i**2, "Closure calls loc = 2 for p^2")
            self.assertEqual(fcub(i), i**3, "Clsoures call loc = 3 for p^3")
            # print(i, fsqr(i), fcub(i))
            # 0 0 0
            # 1 1 1
            # 2 4 8
            # 3 9 27
            # 4 16 64
        
        # Write a lambda function, setting the least significant bit of its integer argument,
        # and apply it to the map() function to produce the string 1 3 3 5 on the console.
        any_list = [1, 2, 3, 4]
        # Expected 1, 3 ,3 ,5
        generated_list = list( map(lambda x: x|1, any_list))
        self.assertEqual(generated_list, [1, 3, 3, 5], "Used a lambda with or operation to create a generator for a list")

        def replace_spaces(replacement='*'):
            def new_replacement(text):
                return text.replace(' ', replacement)
            return new_replacement

        # self.assertEqual(replace_spaces, )
        stars = replace_spaces()
        self.assertEqual(stars("And Now for Something Completely Different"),
                         "And*Now*for*Something*Completely*Different",
                         "Enclosure initializes * for spaces as replacement")
        # print(stars("And Now for Something Completely Different"))


    # @ignore_warnings
    def testfileOperations(self):
            # Text mode 	Binary mode 	Description
            #         rt 	    rb       	read  Can only read File must exist 
            #         wt 	    wb       	write Can only write. File does not need to exist. Will over write
            #         at 	    ab       	append. Does not need to exist Open set to end of file
            #         r+t   	r+b      	read and update,  must exist and be writable
            #         w+t 	    w+b 	    write and update, Does not need to exsist, will append

            # errno.EBADF → Bad file number.
            # errno.EEXIST → File exists.
            # errno.EFBIG → File too large.
            # errno.EISDIR → Is a directory.
            # errno.EMFILE → Too many open files.
            # errno.ENOENT → No such file or directory.
            # errno.ENOSPC → No space left on device.


        
        try:
            pass
        # Some stream operations.
        except IOError as exc:
            print(exc.errno)
            print(exc.errno.EISDIR)

        import errno
        from os import strerror

        with self.assertRaises(TypeError):
            try:
                s = open("c:/users/user/Desktop/file.txt", "rt")
                # Actual processing goes here.
                s.close()
            except Exception as exc:
                if exc.errno == errno.ENOENT:
                    self.assertTrue("We are heree due to file not found error")
    #                print("The file doesn't exist.")
                elif exc.errno == errno.EMFILE:
                    print("You've opened too many files.")
                else:
                    print("The error number is:", exc.errno)
                raise()

        try:
            s = open("c:/users/user/Desktop/file.txt", "rt")
            # Actual processing goes here.
            s.close()
        except Exception as exc:
            # print("The file could not be opened:", strerror(exc.errno))
            pass

        # Opening tzop.txt in read mode, returning it as a file object:
        try: 
            stream = None
            stream = open("tzop.txt", "rt", encoding = "utf-8")
            # print(stream.read()) # printing the content of the file
        except Exception as exc:
            print("The file could not be opened:", strerror(exc.errno))
            print("The file could not be opended with errorcode {}->{}".format(exc.errno, strerror(exc.errno)))
            # if exc.errno == errno.ENOENT:
            #     print("The file doesn't exist.")
            # elif exc.errno == errno.EMFILE:
            #     print("You've opened too many files.")
            # else:
            #     print("The error number is:", exc.errno)
        finally:
            if stream:
                stream.close()
    
    # @ignore_warnings
    def testReadingFile(self):
        # Using read to lone 1 character at a time
        from os import strerror
        try:
            cnt = 0
            s = open('text.txt', "rt")
            ch = s.read(1)
            while ch != '':
                # print(ch, end='')
                cnt += 1
                ch = s.read(1)
            s.close()
            # print("\n\nCharacters in file:", cnt)
            self.assertEqual(cnt, 131, "Via read load one character at a time/ There are 131 characters in file from the count.")
        except IOError as e:
            print("I/O error occurred: ", strerror(e.errno))
        finally:
            if s:
                s.close()

        # Using read to load entire file
        from os import strerror
        try:
            cnt = 0
            s = open('text.txt', "rt")
            content = s.read()
            for ch in content:
                # print(ch, end='')
                cnt += 1
            s.close()
            # print("\n\nCharacters in file:", cnt)
            self.assertEqual(cnt, 131, "Via read, load entire file into memory with 131 characters")
        except IOError as e:
            print("I/O error occurred: ", strerror(e.errno))

        # Using readline
        from os import strerror
        try:
            ccnt = lcnt = 0
            s = open('text.txt', 'rt')
            line = s.readline()
            while line != '':
                lcnt += 1
                for ch in line:
                    # print(ch, end='')
                    ccnt += 1
                line = s.readline()
            s.close()
            self.assertEqual(ccnt, 131, "Read file via readline into memory with 131 characters")
            self.assertEqual(lcnt, 4, "4 lines in file")
        except IOError as e:
            print("I/O error occurred:", strerror(e.errno))

        # Using readlines
        from os import strerror
        try:
            ccnt = lcnt = 0
            s = open('text.txt', 'rt')
            lines = s.readlines(20)
            while len(lines) != 0:
                for line in lines:
                    lcnt += 1
                    for ch in line:
                        # print(ch, end='')
                        ccnt += 1
                lines = s.readlines(10)
            s.close()
            self.assertEqual(ccnt, 131, "Read file via readline into memory with 131 characters")
            self.assertEqual(lcnt, 4, "4 lines in file")
        except IOError as e:
            print("I/O error occurred:", strerror(e.errno))

        # Using for line in open causes a resource warning that we are not properly closing the file.
        # I would not use this method. Prefer contaxt manager instead of this method
        # from os import strerror
        # try:
        #     ccnt = lcnt = 0
        #     for line in open('text.txt', 'rt'):   # Open returns an iterable
        #         lcnt += 1
        #         for ch in line:
        #             # print(ch, end='')
        #             ccnt += 1
        #     self.assertEqual(ccnt, 131, "Using iteration from open causes a resource warning. ")
        #     self.assertEqual(lcnt, 4, "4 lines in file")     
        # except IOError as e:
        #     print("I/O error occurred: ", strerror(e.errno))

    def testWritingFiles(self):
        from os import strerror, remove
        from os.path import exists
   
        # Use open and write one character at a time
        try:
            fo = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
            for i in range(10):
                s = "line #" + str(i+1) + "\n"
                for ch in s:
                    fo.write(ch)
            fo.close()
            self.assertTrue(exists('newtext.txt'), "Writing one character at a timeFile exists")            
        except IOError as e:
            print("I/O error occurred: ", strerror(e.errno))
        else:
            remove("newtext.txt")
        finally:
            pass

        # Use open and write one link at a time
        from os import strerror
        try:
            fo = open('newtext.txt', 'wt')
            for i in range(10):
                fo.write("line #" + str(i+1) + "\n")
            self.assertTrue(exists('newtext.txt'), "Writing one line at a timeFile exists")            
            fo.close()
        except IOError as e:
            print("I/O error occurred: ", strerror(e.errno))
        else:
            remove("newtext.txt")
        finally:
            pass

    def testByteArray(self):
        data = bytearray(10)
        self.assertTrue(len(data), 10)
        for i in range(len(data)):
            data[i] = 10 - i

        for index, element in zip(range(10, 1, -1), data):
            self.assertEqual(element, index)            

      
        from os import strerror, remove
        from os.path import exists, getsize
        data = bytearray(10)
        for i in range(len(data)):
            data[i] = 10 + i

        #  4.3.1.11 Working with real files
        # Write Data for readinto below
        bf = None
        try:
            bf = open('file.bin', 'wb')
            bf.write(data)
            bf.close()
            self.assertTrue(exists("file.bin"), "Used write to write data to file from byteArray")
            self.assertEqual(getsize("file.bin"), 10)

        except IOError as e:
            print("I/O error occurred:", strerror(e.errno))
            if bf is not None:
                bf.close()

        data = bytearray(10)

        #  4.3.1.11 Working with real files
        # Using readinto to write into 
        try:
            bf = open('file.bin', 'rb')
            bf.readinto(data)
            bf.close()

            listData = [b for b in data]
            self.assertEqual(listData, [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], "Uses readinto to read to bytearray" )
            # for b in data:
            #     print(hex(b), end=' ')
        except IOError as e:
            print("I/O error occurred:", strerror(e.errno))
        else:
            remove("file.bin")

        #  4.3.1.12 Working with real files
        # Creating data for read() for data below
        from os import strerror

        data = bytearray(10)
        for i in range(len(data)):
            data[i] = 10 + i

        try:
            bf = open('file.bin', 'wb')
            bf.write(data)
            bf.close()
        except IOError as e:
            print("I/O error occurred:", strerror(e.errno))

         # 4.3.1.12 Working with real files
        # Your code that reads bytes from the stream should go here.
        from os import strerror
        try:
            bf = open('file.bin', 'rb')
            data = bytearray(bf.read())
            bf.close()
            
            listData = [b for b in data]
            self.assertEqual(listData, [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], "Uses read() to read to bytearray" )
            # for b in data:
            #     print(hex(b), end=' ')
        except IOError as e:
            print("I/O error occurred:", strerror(e.errno))
        else:
            remove("file.bin")


        # 4.3.1.13 Write of data for read(5) below
        from os import strerror
        data = bytearray(10)
        for i in range(len(data)):
            data[i] = 10 + i
        try:
            bf = open('file.bin', 'wb')
            bf.write(data)
            bf.close()
        except IOError as e:
            print("I/O error occurred:", strerror(e.errno))
        
        # 4.3.1.13 Specifies the number of bytes from read  
        # Using read to read 5 bytes of data
        # Your code that reads bytes from the stream should go here.
        try:
            bf = open('file.bin', 'rb')
            data = bytearray(bf.read(5))
            bf.close()
            # for b in data:
            #     print(hex(b), end=' ')
            listData = [b for b in data]    
            self.assertEqual(listData, [10, 11, 12, 13, 14], "Uses read(5) to read from bytearray" )
        except IOError as e:
            print("I/O error occurred:", strerror(e.errno))
        else:
            remove("file.bin")
        
    def testCopyingFiles(self):
        from os import strerror, remove
        from os.path import exists
        import filecmp

        # srcname = input("Enter the source file name: ")
        srcname = "text.txt"
        try:
            src = open(srcname, 'rb')
        except IOError as e:
            print("Cannot open the source file: ", strerror(e.errno))
            exit(e.errno)	

        # dstname = input("Enter the destination file name: ")
        dstname = "dstname.txt"
        
        try:
            dst = open(dstname, 'wb')
        except Exception as e:
            print("Cannot create the destination file: ", strerror(e.errno))
            dst.close()
            exit(e.errno)	
            
    
        buffer = bytearray(65536)
        total  = 0
        try:
            readin = src.readinto(buffer)
            while readin > 0:
                written = dst.write(buffer[:readin])
                total += written
                readin = src.readinto(buffer)
            src.close()
            dst.close()
            self.assertTrue(exists(srcname))
            self.assertTrue(exists(dstname))
            self.assertTrue(filecmp.cmp(srcname, dstname))
            
        except IOError as e:
            print("Cannot create the destination file: ", strerror(e.errno))
            exit(e.errno)	
        else:
            dst.close()    
            remove(dstname)
            self.assertEqual(total, 134)
       
        
        
        
    """
    4.3.1.15 LAB: Character frequency histogram
    
    Estimated time
    30-60 minutes
    Level of difficulty
    Medium
    Objectives
        improving the student's skills in operating with files (reading)
        using data collections for counting numerous data.

    Scenario
    A text file contains some text (nothing unusual) but we need to know how often (or how rare) each letter appears in the text. Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.
    Your task is to write a program which:
        asks the user for the input file's name;
        reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
        prints a simple histogram in alphabetical order (only non-zero counts should be presented)

    Create a test file for the code, and check if your histogram contains valid results.
    Assuming that the test file contains just one line filled with:
    aBc

    samplefile.txt
    the expected output should look as follows:
    a -> 1
    b -> 1
    c -> 1

    output
    Tip: We think that a dictionary is a perfect data collection medium for storing the counts. The letters may be keys while the counters can be values.
    """
    def testCreateHistogram(self):
        from os import strerror
        import errno
        
        class Histogram():
            def __init__(self, fileName) -> None:
                pass
                self.fileName = fileName
                self.characterDict = {}
                # self.fileData = self.__loadFileRead0()
                # self.evaluateConents1()
                self.fileData = self.__loadFileRead1()
                self.evaluateConents0()

            """Uses read to input whole file at once, could run out of memory"""            
            def __loadFileRead0(self) -> str:
                try:
                    stream = None
                    stream = open(self.fileName, "rt", encoding = "utf-8")

                    fileData = stream.read()
                    # for ch in fileData:
                    #     print(ch)
                        
                    stream.close()    
                except IOError as exc:
                    raise(f"IOError with error no:{exc.errorno} descripton {strerror(exc.errorno)}")
                return fileData
                
            "Uses read to read 10 "
            def __loadFileRead1(self) -> str:
                try:
                    stream = open(self.fileName, "rt", encoding = "utf-8")
                    fileData = result = str()
                    # Want to read 10 bytes at a time
                    while(True):
                        result = stream.read(10)
                        if(len(result) == 0):
                            break
                        fileData += result
                        # print(result)

                    stream.close()    
                except IOError as exc:
                    raise(f"IOError with error no:{exc.errorno} descripton {strerror(exc.errorno)}")
                else:
                    stream.close()
                return fileData
                
                
            def evaluateConents0(self):
                for ch in self.fileData:
                    if ch not in self.characterDict.keys():
                        # print(f"{ch} not in dictionary adding")
                        self.characterDict.update({ch: 1})
                    else:
                        value = self.characterDict.get(ch)
                        # print(f"{ch} in dictionary increment {value} by 1")
                        value += 1
                        self.characterDict.update({ch: value})
                    
            def evaluateConents1(self):
                for ch in self.fileData:
                    if ch in self.characterDict:
                        value = self.characterDict.get(ch)
                        # print(f"{ch} in dictionary increment {value} by 1")
                        value += 1
                        self.characterDict.update({ch: value})
                    else:
                        result = self.characterDict.setdefault(ch, 1)
                        # print(f"{ch} not in dictionary add {ch}:{result}")
                
                
                    result = self.characterDict.get(ch)
                    print(f'{ch}:{result}')
                print(self.characterDict.items())
                print(self.fileData)
                
            def getCharDict(self) -> dict:
                return self.characterDict
            
            # Resolves  4.3.1.16 LAB: Sorted character frequency histogram 
            def getSortedCharDictValue(self) -> list:
                result = sorted(self.characterDict.items(), key=lambda item: item[1])
                return result
                
            def getSortedCharDictKey(self) -> list:
                result = sorted(self.characterDict.items(), key=lambda item: item[0])
                return result
                
        histo = Histogram("text.txt")
        dictCompare = {'B': 1, 'e': 13, 'a': 6, 'u': 3, 't': 16, 'i': 12, 'f': 1, 'l': 8, ' ': 16, 's': 4,
                       'b': 4, 'r': 4, 'h': 4, 'n': 4, 'g': 1, 'y': 1, '.': 4, '\n': 3, 'E': 1, 'x': 3,
                       'p': 6, 'c': 5, 'm': 5, 'S': 1, 'o': 3, 'C': 1, 'd': 1}
        
        self.assertEqual(histo.characterDict, dictCompare)
        

        self.assertEqual(histo.getSortedCharDictValue(), 
                        [('B', 1), ('f', 1), ('g', 1), ('y', 1), ('E', 1), ('S', 1), ('C', 1), ('d', 1), ('u', 3), ('\n', 3), 
                         ('x', 3), ('o', 3), ('s', 4), ('b', 4), ('r', 4), ('h', 4), ('n', 4), ('.', 4), ('c', 5), ('m', 5), 
                         ('a', 6), ('p', 6), ('l', 8), ('i', 12), ('e', 13), ('t', 16), (' ', 16)], "Dictory sorted by value via lambda")
        
        
        self.assertEqual(histo.getSortedCharDictKey(),
                        [('\n', 3), (' ', 16), ('.', 4), ('B', 1), ('C', 1), ('E', 1), ('S', 1), ('a', 6), ('b', 4), ('c', 5),
                         ('d', 1), ('e', 13), ('f', 1), ('g', 1), ('h', 4), ('i', 12), ('l', 8), ('m', 5), ('n', 4), ('o', 3), 
                         ('p', 6), ('r', 4), ('s', 4), ('t', 16), ('u', 3), ('x', 3), ('y', 1)], "Dictionary sorted by key via lambda")
        
        
    """
    4.3.1.16 LAB: Sorted character frequency histogram 
    
    Estimated time
    15-30 minutes

    Level of difficulty
    Medium

    Prerequisites
        4.3.1.15
        Objectives

            improve the student's skills in operating with files (reading/writing)
            using lambdas to change the sort order.

    Scenario

    The previous code needs to be improved. It's okay, but it has to be better.

    Your task is to make some amendments, which generate the following results:

        the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
        the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' (it should be concatenated to the original name)

    Assuming that the input file contains just one line filled with:
    cBabAa

    samplefile.txt

    the expected output should look as follows:
    a -> 3
    b -> 2
    c -> 1
    Tip: Use a lambda to change the sort order.
    """
    
    """
     4.3.1.17 LAB: Evaluating students' results
    Estimated time
    30-90 minutes

    Level of difficulty
    Medium

    Objectives
        improve the student's skills in operating with files (reading)
        perfecting the student's abilities in defining and using self-defined exceptions and dictionaries.

    Scenario
        Prof. Jekyll conducts classes with students and regularly makes notes in a text file. Each line of the file contains three elements: the student's first name, the student's last name, and the number of point the student received during certain classes.
        The elements are separated with white spaces. Each student may appear more than once inside Prof. Jekyll's file.

        The file may look as follows:
        John	Smith	5
        Anna	Boleyn	4.5
        John	Smith	2
        Anna	Boleyn	11
        Andrew	Cox	1.5

        samplefile.txt

        Your task is to write a program which:

            asks the user for Prof. Jekyll's file name;
            reads the file contents and counts the sum of the received points for each student;
            prints a simple (but sorted) report, just like this one:

        Ouutput
            Andrew Cox 	 1.5
            Anna Boleyn 	 15.5
            John Smith 	 7.0
    Note:
        your program must be fully protected against all possible failures: the file's non-existence, the file's emptiness, or any input data failures; encountering any data error should cause immediate program termination, and the erroneous should be presented to the user;
        implement and use your own exceptions hierarchy - we've presented it in the editor; the second exception should be raised when a bad line is detect, and the third when the source file exists but is empty.

    Tip: Use a dictionary to store the students' data.
    """
    def testEvaluateStudentResults(self):
        import errno
        from os import strerror
        from os.path import exists
        
        class StudentResults():
            def __init__(self, fileName=None) -> None:
                self._fileName = fileName
                self._fileData = ""
                self._formattedData = list()
                self._orderedData = list()
                
            # Uses read()
            def LoadFile0(self, fileName) -> str:
                stream = None
                result = ""
                
                try: 
                    stream = open(fileName, 'rt')
                    print(type(stream))
                    result = stream.read()
                    print(result)
                    stream.close()
                                
                except FileNotFoundError as exc:
                    print(f'{exc.errno}:{strerror(exc.errno)}')
                except IOError as exc:
                    print(exc.errno)
                    print(strerror(exc.errno))            
                    raise
                
                return result
                    
            def LoadFile1(self, fileName) -> str:
                stream = None
                data = ""
                
                try:
                    data = ''
                    stream = open(fileName, 'rt+')
                    result = stream.readline()
                    
                    while result != "":
                        data +=result
                        result = stream.readline()
                    stream.close()
                
                except FileNotFoundError as exc:
                    print(f'{exc.errno}:{strerror(exc.errno)}')
                
                except IOError as exc:
                    print(exc.errno)
                    print(strerror(exc.errno))            
                    raise
                
                self._fileData = data
                return data
            
            def LoadData(self):
                myList = list()
                
                for line in self._fileData.splitlines():
                    intermediate = line.split( "\t", maxsplit=5)
                    formatted = [intermediate[0], intermediate[1], float(intermediate[2])]
                    
                    myList.append(formatted)
                self._formattedData = myList
                
                return myList 
            
            def SortByScore(self):
                myList = list()
                myList = sorted(self._formattedData, key = lambda x: x[2], reverse=False )  # Uses sorted and key of score
                self._orderedData = myList
                return self._orderedData
       
            def SortByFirstName(self):
                myList = list()
                myList = sorted(self._formattedData, key = lambda x: x[0] )  # Uses sorted and key of first name
                self._orderedData = myList
                return self._orderedData
            
            def SortListByScore(self):
                myList = self._formattedData.copy()
                myList.sort(key=lambda x: x[2] )
                self._orderedData = myList
                return self._orderedData
            
       
        obj = StudentResults()

        self.assertEqual(obj.LoadFile1("studentResults.txt"), 
                          "John\tSmith\t5\nAnna\tBoleyn\t4.5\nJohn\tSmith\t2\nAnna\tBoleyn\t11\nAndrew\tCox\t1.5\n")
        self.assertEqual(obj.LoadData(), [['John', 'Smith', 5.0], 
                               ['Anna', 'Boleyn', 4.5], 
                               ['John', 'Smith', 2.0], 
                               ['Anna', 'Boleyn', 11.0], 
                               ['Andrew', 'Cox', 1.5]])
        

        self.assertEqual(obj.SortByScore(), [['Andrew', 'Cox', 1.5],
                                             ['John', 'Smith', 2.0], 
                                             ['Anna', 'Boleyn', 4.5], 
                                             ['John', 'Smith', 5.0], 
                                             ['Anna', 'Boleyn', 11.0]])
        self.assertEqual(obj.SortByFirstName(), [['Andrew', 'Cox', 1.5], 
                                                 ['Anna', 'Boleyn', 4.5], 
                                                 ['Anna', 'Boleyn', 11.0],
                                                 ['John', 'Smith', 5.0],
                                                 ['John', 'Smith', 2.0]])
        self.assertEqual(obj.SortListByScore(), [['Andrew', 'Cox', 1.5], 
                                                  ['John', 'Smith', 2.0], 
                                                  ['Anna', 'Boleyn', 4.5], 
                                                  ['John', 'Smith', 5.0], 
                                                  ['Anna', 'Boleyn', 11.0]])

        
        
    def testOSCommands(self):
        import os
        
        if os.name == 'posix':
            from os import uname, makedirs, mkdir
        elif os.name == 'nt':       
            from platform import uname
            
        
        # result = uname()
        # for description in result:
        #     print(description)
        
        import tempfile
        tempDir = tempfile.gettempdir()
        
        myDir = tempDir + os.sep + "myDir"
        try:
            os.mkdir(myDir)
        except FileExistsError as exc:
            print("You have already created the file")
        finally: 
            # pathforTestDirectory = tempDir + os.sep + "myDir" + os.sep + "myDir2" + os.sep + "myDir3"
            # os.removedirs(pathforTestDirectory)
            # os.removedirs(tempDir + os.sep + "myDir" + os.sep + "myDir2")
            # os.removedirs(tempDir + os.sep + "myDir")
            os.removedirs(myDir)



        self.assertFalse(hasattr(os, 'MakeDir'), "Expected failure no os.MakeDir")
        self.assertTrue(hasattr(os, 'mkdir'), "os.mkdir exists")
        self.assertTrue(hasattr(os, 'makedirs'), "os.makekdirs exists")

        pathforTestDirectory = tempDir + os.sep + "myDir" + os.sep + "myDir2" + os.sep + "myDir3"
        try:
            os.makedirs(pathforTestDirectory)
            
        except FileExistsError as exc:
            print("You have already created the file")
        except AttributeError as exc:
            print("os.makedirs does not exist")
        except Exception as e:
            print(e)
            raise
        finally: 
            os.removedirs(pathforTestDirectory)
    
        import os
        import os.path
        from pathlib import Path
 
            
            
        if(os.path.isdir(tempDir + os.sep + "myDir" + os.sep + "myDir2")):
            os.removedirs(tempDir + os.sep + "myDir" + os.sep + "myDir2")
        if(os.path.isdir(tempDir + os.sep + "myDir")):
            os.removedirs(tempDir + os.sep + "myDir")
    

        # Does not work
        # https://stackoverflow.com/questions/23488924/how-to-delete-recursively-empty-folders-in-python3
        # for p in Path(pathforTestDirectory).glob('**/*'):
        #     if p.is_dir() and len(list(p.iterdir())) == 0:
        #         os.removedirs(p)
        # self.assertTrue(os.path.isdir(pathforTestDirectory))
       
        
        # testDir = os.getcwd()
        # os.chdir(tempDir)
        # print(os.listdir())
        # os.chdir(testDir)
        # print(os.listdir())
        
        
        
        
    # systemname — stores the name of the operating system;
    # nodename — stores the machine name on the network;
    # release — stores the operating system release;
    # version — stores the operating system version;
    # machine — stores the hardware identifier, e.g., x86_64.

        import os
        import os.path
        returned_value = os.system("mkdir my_first_directory")
        
        self.assertEqual(returned_value, 0, "os.system command successful")
        self.assertTrue(os.path.isdir("my_first_directory"), "Directory was created and exists")
        returned_value = os.system("rmdir my_first_directory")
        self.assertEqual(returned_value, 0, "os.system command successful")
        self.assertFalse(os.path.isdir("my_first_directory"), "Directory was deketed and no longer exists")
        pass

    """  4.4.1.8 LAB: The os module
    Finding a directory
    Estimated time
    15-30 min

    Level of difficulty
    Easy

    Objectives
        improving the student's skills in interacting with the operating system;
        practical use of known functions provided by the os module.

    Scenario
        It goes without saying that operating systems allow you to search for files and directories. While studying this part of the course, you learned about the functions of the os module, which have everything you need to write a program that will search for directories in a given location.

    To make your task easier, we have prepared a test directory structure for you:

    Directory structure
    Your program should meet the following requirements:

    Write a function or method called find that takes two arguments called path and dir. The path argument should accept a relative or absolute path to a directory where the search should start, while the dir argument should be the name of a directory that you want to find in the given path. Your program should display the absolute paths if it finds a directory with the given name.
    The directory search should be done recursively. This means that the search should also include all subdirectories in the given path.

    Example input:
    path="./tree", dir="python"

    Example output:
    .../tree/python
    .../tree/cpp/other_courses/python
    .../tree/c/other_courses/python
    """   
    def testFindDirectory(self):
        import os
        import os.path
        from os.path import isdir
        from os import makedirs, mkdir, listdir, sep, getcwd
        from pathlib import Path
        from tempfile import gettempdir, gettempdirb
        
        # Define directory structure to be made
        # Directory structure
        # /tree
        # /tree/c
        # /tree/c/other_courses
        # /tree/c/other_courses/cpp
        # /tree/c/other_courses/python
        # /tree/cpp
        # /tree/cpp/other_courses
        # /tree/cpp/other_course/python
        # /tree/cpp/other_courses/c
        # /tree/python
        # /tree/python/other_courses
        # /tree/python/other_courses/c
        # /tree/python/other_courses/cpp
        
        cwd = getcwd()
        tempDir = gettempdir()
        dot = "."
        tree = "tree"
        other_courses = "other_courses"
        python = "python"
        cpp = "cpp"
        c = "c"
        baseDirectories = (tempDir, cwd, dot)

        for baseDir in baseDirectories:
            treeDirectory   = baseDir + sep + tree
            tree_c          = baseDir + sep + tree + sep + c
            tree_cpp        = baseDir + sep + tree + sep + cpp
            tree_python     = baseDir + sep + tree + sep + python

            c_other_cpp     = tree_c                              + sep + other_courses + sep + cpp
            c_other_python  = tree_c                              + sep + other_courses + sep + python
            cpp_other_c     = tree_cpp                            + sep + other_courses + sep + c 
            cpp_other_p     = tree_cpp                            + sep + other_courses + sep + python
            python_other_c  = tree_python                         + sep + other_courses + sep + c
            pyton_other_cpp = tree_python                         + sep + other_courses + sep + cpp
            
            
            # c_other_cpp     = baseDir + sep + tree + sep + c      + sep + other_courses + sep + cpp
            # c_other_python  = baseDir + sep + tree + sep + c      + sep + other_courses + sep + python
            # cpp_other_c     = baseDir + sep + tree + sep + cpp    + sep + other_courses + sep + c 
            # cpp_other_p     = baseDir + sep + tree + sep + cpp    + sep + other_courses + sep + python
            # python_other_c  = baseDir + sep + tree + sep + python + sep + other_courses + sep + c
            # pyton_other_cpp = baseDir + sep + tree + sep + python + sep + other_courses + sep + cpp
            
            try:
                makedirs(c_other_cpp)
                makedirs(c_other_python)
                makedirs(cpp_other_c)
                makedirs(cpp_other_p)
                makedirs(python_other_c)
                makedirs(pyton_other_cpp)
            except:
                print("Not able to make the required directories")
            
            p = Path(baseDir)
            
            # Note you can use a print statement of the search results to confirm the found directories
            searchPython = list(p.glob("**"+ sep + "python"))
            
            result = str(searchPython)
            
            result = [ repr(path) for path in searchPython]
            
            pass
            
            # for path in searchPython:
            #     print(path)
# C:\Users\ttpha\AppData\Local\Temp\tree\python
# C:\Users\ttpha\AppData\Local\Temp\tree\c\other_courses\python
# C:\Users\ttpha\AppData\Local\Temp\tree\cpp\other_courses\python
# C:\Users\ttpha\source\repos\practice\pcap\tree\python
# C:\Users\ttpha\source\repos\practice\pcap\tree\c\other_courses\python
# C:\Users\ttpha\source\repos\practice\pcap\tree\cpp\other_courses\python
# tree\python
# tree\c\other_courses\python
# tree\cpp\other_courses\python
            
            # print(searchPython)
            searchCPP = list(p.glob("**"+ sep + "cpp"))
            
            
#             .......C:\Users\ttpha\AppData\Local\Temp\tree\cpp
# C:\Users\ttpha\AppData\Local\Temp\tree\c\other_courses\cpp
# C:\Users\ttpha\AppData\Local\Temp\tree\python\other_courses\cpp
# C:\Users\ttpha\source\repos\practice\pcap\tree\cpp
# C:\Users\ttpha\source\repos\practice\pcap\tree\c\other_courses\cpp
# C:\Users\ttpha\source\repos\practice\pcap\tree\python\other_courses\cpp
# tree\cpp
# tree\c\other_courses\cpp
# tree\python\other_courses\cpp
            
            # print(searchCPP)
            searchC = list(p.glob("**"+ sep + "c"))
              
#             C:\Users\ttpha\AppData\Local\Temp\tree\c
# C:\Users\ttpha\AppData\Local\Temp\tree\cpp\other_courses\c
# C:\Users\ttpha\AppData\Local\Temp\tree\python\other_courses\c
# C:\Users\ttpha\source\repos\practice\pcap\tree\c
# C:\Users\ttpha\source\repos\practice\pcap\tree\cpp\other_courses\c
# C:\Users\ttpha\source\repos\practice\pcap\tree\python\other_courses\c
# tree\c
# tree\cpp\other_courses\c
# tree\python\other_courses\c

            
            self.assertTrue(os.path.isdir(treeDirectory))
            self.assertTrue(isdir(c_other_cpp))
            self.assertTrue(isdir(c_other_python))
            self.assertTrue(isdir(cpp_other_c))
            self.assertTrue(isdir(cpp_other_p))
            self.assertTrue(isdir(python_other_c))
            self.assertTrue(isdir(pyton_other_cpp))
            
            
            
            
            # [os.removedirs(p) for p in Path(treeDirectory).glob('**/*') if p.is_dir() and len(list(p.iterdir())) == 0]
            if os.path.isdir(treeDirectory):
                 for p in Path(treeDirectory).glob('**/*'):
                    if p.is_dir() and len(list(p.iterdir())) == 0:
                        os.removedirs(p)
            self.assertFalse(os.path.isdir(treeDirectory))
            
        
    def testDateTime(self):
        from datetime import date
        today = date.today()
        # print("Today:", today)
        # print("Year:", today.year)
        # print("Month:", today.month)
        # print("Day:", today.day)


        earliestDate = date(1,1,1)
        self.assertEqual(str(earliestDate), "0001-01-01")
        latestDate = date(9999, 12, 31)
        self.assertEqual(str(latestDate), "9999-12-31")

        import datetime
 
        nineteenSeventy = datetime.datetime(1970, 1, 1)
        twoThousand = datetime.datetime(2000, 1, 1)
        
        timeFromTwoThousandtoNineteenSeventy = twoThousand - nineteenSeventy
        secondsFromTwoThousandtoNineteenSeventy = timeFromTwoThousandtoNineteenSeventy.total_seconds()
        self.assertEqual(secondsFromTwoThousandtoNineteenSeventy, 946684800.0)

        from datetime import date
        import time

        timestamp = time.time()
        self.assertGreater(time.time(), 1710000000, "More than number of seconds from 3/25/2024")

        d = date.fromtimestamp(timestamp)

        from datetime import date
        d = date.fromisoformat('2019-11-04')
        self.assertEqual(str(d), '2019-11-04',"ISO 8601 is YEAR-MONTH-DAY ")

        from datetime import date
        d = date(1991, 2, 5)
        self.assertEqual(str(d), "1991-02-05", "Set at this date")
        d = d.replace(year=1992, month=1, day=16)
        self.assertEqual(str(d), "1992-01-16", "Used replace to update the date")

        from datetime import date
        d = date(2019, 11, 4)
        # print(d.weekday())

        from datetime import date
        d = date(2019, 11, 4)
        self.assertEqual(d.weekday(), 0, "Follows ISO 85601 It is a Monday numeric 0")
        d = date(2019, 11, 10)
        self.assertEqual(d.weekday(), 6, "It is a Sunday numeric 6")

        from datetime import time

        t = time(14, 53, 20, 1)     # Defaults to military time. 
        self.assertEqual(str(t), "14:53:20.000001", "Time Format Hours:Minutes:Seconds:Microseconds")

        import time
        class Student:
            def take_nap(self, seconds):
                time.sleep(seconds)
                
        student = Student()
        # Sample of sleep function from tme
        student.take_nap(.00000001)

        import time
        timestamp = 1572879180
        self.assertEqual(str(time.ctime(timestamp)), "Mon Nov  4 06:53:00 2019", "Passing time in seconds from 1970 creates a date and time")
        # Passing with no time stamp generates current time. 
        # print(time.ctime())
        
        
        import time
        timestamp = 1572879180
        self.assertEqual(str(time.gmtime(timestamp)), 
                        "time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)")
        self.assertEqual(str(time.localtime(timestamp)),
                        "time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=6, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)")                   
        
        import time
        timestamp = 1572879180
        st = time.gmtime(timestamp)
        self.assertIsInstance(st, time.struct_time, "gmtime returns a struct time object> If seconds not provided uses current ")
        self.assertEqual(st.tm_year, 2019)
        self.assertEqual(st.tm_mon, 11)
        self.assertEqual(st.tm_mday, 4)
        self.assertEqual(st.tm_hour, 14)
        self.assertEqual(st.tm_min, 53)
        self.assertEqual(st.tm_sec, 0)
        self.assertEqual(st.tm_wday, 0)
        self.assertEqual(st.tm_yday, 308)
        self.assertEqual(st.tm_isdst, 0 )
    

        timestamp = 1572879180
        stLocalTime = time.localtime(timestamp)
        self.assertIsInstance(stLocalTime, time.struct_time, "localtime returns a struct time object")
        # time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=6, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)
        self.assertEqual(stLocalTime.tm_year, 2019)
        self.assertEqual(stLocalTime.tm_mon, 11)
        self.assertEqual(stLocalTime.tm_mday, 4)
        self.assertEqual(stLocalTime.tm_hour, 6)
        self.assertEqual(stLocalTime.tm_min, 53)
        self.assertEqual(stLocalTime.tm_sec, 0)
        self.assertEqual(stLocalTime.tm_wday, 0)
        self.assertEqual(stLocalTime.tm_yday, 308)
        self.assertEqual(stLocalTime.tm_isdst, 0 )
        self.assertEqual(stLocalTime.tm_zone, 'Pacific Standard Time')
        self.assertEqual(stLocalTime.tm_gmtoff, -28800, 'GMT is 8 hours away from PST in seconds ')

 
        # time.struct_time:
        # tm_year   # specifies the year
        # tm_mon    # specifies the month (value from 1 to 12)
        # tm_mday   # specifies the day of the month (value from 1 to 31)
        # tm_hour   # specifies the hour (value from 0 to 23)
        # tm_min    # specifies the minute (value from 0 to 59)
        # tm_sec    # specifies the second (value from 0 to 61 )
        # tm_wday   # specifies the weekday (value from 0 to 6)
        # tm_yday   # specifies the year day (value from 1 to 366)
        # tm_isdst  # specifies whether daylight saving time applies (1 – yes, 0 – no, -1 – it isn't known)
        # tm_zone   # specifies the timezone name (value in an abbreviated form)
        # tm_gmtoff # specifies the offset east of UTC (value in seconds)
        self.assertEqual( str(time.asctime(st)), "Mon Nov  4 14:53:00 2019", "Used to create a date time string from timestamp")
        self.assertEqual( time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)), 1572907980.0, "Used to create time string from tuple or struct time object")

    def testCreateDateTimeObjects(self):
        from datetime import datetime
        dt = datetime(2019, 11, 4, 14, 53)

  

        self.assertEqual(str(dt), "2019-11-04 14:53:00")
        # print(dt.date(), "2019-11-04")
        # print(dt.time(), "14:53:00")
        self.assertEqual(str(dt), "2019-11-04 14:53:00")

        # ts constructor accepts the following parameters:
        # Parameter 	Restrictions
        # year 	        The year parameter must be greater than or equal to 1 (MINYEAR constant) 
        #               and less than or equal to 9999 (MAXYEAR constant).
        #
        # month         The month parameter must be greater than or equal to 1 and less than or equal to 12.
        # 
        # day           The day parameter must be greater than or equal to 1 and less than or equal to the last day of the given month 
        #               and year.
        #
        # hour          The hour parameter must be greater than or equal to 0 and less than 23. 
        #
        # minute 	    The minute parameter must be greater than or equal to 0 and less than 59.
        #
        # second 	    The second parameter must be greater than or equal to 0 and less than 59.
        # microsecond   The microsecond parameter must be greater than or equal to 0 and less than 1000000.
        
        # tzinfo 	     The tzinfo parameter must be a tzinfo subclass object or None (default).
        # fold 	         The fold parameter must be 0 or 1 (default 0).
        fullDateTime = datetime(2024,
                                12,
                                30,
                                23,
                                59,
                                59,
                                999999)
       # print(fullDateTime.tzinfo)
    
        # https://docs.python.org/3/library/zoneinfo.html#module-zoneinfo
        # Use zoneinfo to help in making tzinfo
        from zoneinfo import ZoneInfo
        from datetime import datetime, timedelta

        # Print out current date time    
        from datetime import datetime, UTC
      #  print("today:", datetime.today())
      #  print("now:", datetime.now())
        # print("utcnow:", datetime.utcnow())  # utcnow is deprecated use now(UTC) below
     #   print(datetime.now(UTC))

        from datetime import datetime
        dt = datetime(2020, 10, 4, 14, 55)
        # print("Timestamp:", dt.timestamp())
        # print("TimeTuple", dt.timetuple())
        # print("timeTZ", dt.timetz())
        # print("timeTZ", dt.astimezone())
        self.assertEqual(dt.timestamp(), 1601848500.0, "Seconds from 1970 for this date")
        
        
        import time
        # print(str(time.ctime(750000000)))
    
        from datetime import date
        d = date(2020, 1, 4)
        # print(d.strftime('%Y/%m/%d'))
        self.assertEqual(d.strftime('%Y/%m/%d'), '2020/01/04', "Use strftime to create formatted date and times")
        # print(d.strftime('%Y/%m/%d/%H:%M:%S'))
        self.assertEqual(d.strftime('%Y/%m/%d/%H:%M:%S:%f'), "2020/01/04/00:00:00:000000", "Reference link for more formatting options")
        # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
        
        from datetime import time
        from datetime import datetime
        t = time(14, 53)
        dt = datetime(2020, 11, 4, 14, 53)
        self.assertEqual(dt.strftime("%y/%B/%d %H:%M:%S"), "20/November/04 14:53:00")
        self.assertEqual(dt.strftime("%Y/%B/%d %H:%M:%S"), "2020/November/04 14:53:00")

        import time

        timestamp = 1572879180
        st = time.gmtime(timestamp)

        # print(time.strftime("%Y/%m/%d %H:%M:%S", st))   # Uses time object to format the time
        # print(time.strftime("%Y/%m/%d %H:%M:%S"))       # Uses current time and formats it

        self.assertEqual(time.strftime("%Y/%m/%d %H:%M:%S", st), "2019/11/04 14:53:00", "# Uses time object to format the time")
        # self.assertEqual(time.strftime("%Y/%m/%d 8"))
    
        # Create a string using strptime
        from datetime import datetime
        # print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
        self.assertEqual(str(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S")), "2019-11-04 14:53:00")

        with self.assertRaises(ValueError):   # Have to catch asset because passed bad formatting of strptime
            str(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S  aDFAf"))


        # Date and time operations
        from datetime import date
        from datetime import datetime

        d1 = date(2020, 11, 4)
        d2 = date(2019, 11, 4)

        self.assertEqual(str(d1-d2), "366 days, 0:00:00", "Calculating days")
        dt1 = datetime(2020, 11, 4, 0, 0, 0)
        dt2 = datetime(2019, 11, 4, 14, 53, 0)
        self.assertEqual(str(dt1 - dt2), "365 days, 9:07:00", "Calculating days and time")
        
        # timedelta constructor accepts:  days, seconds, microseconds, milliseconds, minutes, hours, and weeks.
        from datetime import timedelta  
        delta = timedelta(weeks=2, days=2, hours=3)
        self.assertEqual(str(delta), "16 days, 3:00:00")
        self.assertEqual(str(delta.days), "16")
        self.assertEqual(str(delta.seconds), "10800")
        self.assertEqual(str(delta.microseconds), "0")

        # Using timedelta and dates 
        from datetime import timedelta
        from datetime import date
        from datetime import datetime

        delta = timedelta(weeks=2, days=2, hours=2)
        self.assertEqual(str(delta), "16 days, 2:00:00", "Current time delta object")
        delta2 = delta * 2
        self.assertEqual(str(delta2), "32 days, 4:00:00", "You multiplied the time delta object by two")
  
        d = date(2019, 10, 4) + delta2
        self.assertEqual(str(d), "2019-11-05", "Create a date object and added the delta2 to it")

        dt = datetime(2019, 10, 4, 14, 53) + delta2
        self.assertEqual(str(dt), "2019-11-05 18:53:00", "Created a date time object and added delta2 to it")


        """ 4.5.1.22 LAB: 
        Estimated time
        15-45 min

        Level of difficulty
        Easy

        Objectives
            improving the student's skills in date and time formatting;
            improving the student's skills in using the strftime method.

        Scenario
        During this course, you learned about the strftime method, which requires knowledge of directives to create a format. It's time to put the known directives into practice.

        By the way, you'll have the opportunity to practice working with documentation, because you'll have to find directives that you don't yet know.
        Here's your task:

        Write a program that creates a datetime object for November 4, 2020 , 14:53:00. The object created should call the strftime method 
        with the appropriate format to display the following result:
        
        2020/11/04 14:53:00
        20/November/04 14:53:00 PM
        Wed, 2020 Nov 04
        Wednesday, 2020 November 04
        Weekday: 3
        Day of the year: 309
        Week number of the year: 44

        expected output
            2020/11/04 14:53:00
            20/November/04 14:53:00 PM
            Wed, 2020 Nov 04
            Wednesday, 2020 November 04
            Weekday: 3
            Day of the year: 309
            Week number of the year: 44

        Note: Each result line should be created by calling the strftime method with at least one directive in the format argument.
    """
    def testLabStrFTime(self):
        from datetime import datetime
        dt = datetime(2020, 11, 4, 14, 53, 0)
        self.assertEqual(str(dt), "2020-11-04 14:53:00", "Default formatting of datetime formatting")
        
        self.assertEqual(dt.strftime("%Y/%m/%d %H:%M:%S"), "2020/11/04 14:53:00")
        self.assertEqual(dt.strftime("%y/%B/%d %H:%M:%S %p"), "20/November/04 14:53:00 PM")
        self.assertEqual(dt.strftime("%a, %Y %b %d"), "Wed, 2020 Nov 04")
        self.assertEqual(dt.strftime("%A, %Y %B %d"), "Wednesday, 2020 November 04")
        self.assertEqual(dt.strftime("Weekday: %w"),"Weekday: 3")

        self.assertEqual(dt.strftime("Day of the year: %j"),"Day of the year: 309")
        self.assertEqual(dt.strftime("Week number of the year: %U"), "Week number of the year: 44")

    def testReviewQuizandEndModule(self):
        # Review
        from datetime import datetime
        self.assertEqual(str(datetime(2020, 1, 1)), "2020-01-01 00:00:00", "Datetime object requires at least year, month, day")
        
        from datetime import date
        # print("Today:", date.today()) # Displays: Today: 2020-09-29
        self.assertIsInstance(date.today(), date, "The today method returns a date object representing the current local date")
   
   
        from datetime import date, datetime
        import time
        baseTime = date(1970, 1, 1)
        today = date.today()
        delta = today - baseTime
        delta.total_seconds
        # print(delta.total_seconds()) 
        
        timestamp = time.time()
        d = date.fromtimestamp(timestamp)
        self.assertIsInstance(date.fromtimestamp(timestamp), date, "Using a timestamp you can create a date. Timestamps are seconds from 1970")
        
        # print(d)

        from datetime import time
        t = time(14, 53)
        # print(t.strftime("%H:%M:%S"))
        
    def testCalendar(self):
        import calendar
        # print(calendar.weekday(2020, 12, 24))
        self.assertEqual(calendar.weekday(2020, 12, 21), calendar.MONDAY, "calendar.MONDAY starting at 0")
        self.assertEqual(calendar.weekday(2020, 12, 24), calendar.THURSDAY , "Thursday is 3")
    

        import calendar
        # print(calendar.isleap(2020))
        self.assertEqual(calendar.leapdays(2010, 2025), 4, "4 leapday years 2012, 2016, 2020, 2024. Range does not include last year")  
        # print(calendar.leapdays(1900, 2025))

    """
    
    Estimated time
    30-60 minutes

    Level of difficulty
    Easy

    Objectives
        Improving the student's skills in using the Calendar class.

    Scenario
    During this course, we looked at the Calendar class a bit. 
    Your task is to extend its functionality with a new method called count_weekday_in_year, 
    which takes a year and a weekday as parameters, and then returns the number of occurrences of a specific weekday in the year.

    Use the following tips:
        Create a class called MyCalendar that extends the Calendar class;
        create the count_weekday_in_year method with the year and weekday parameters. 
        The weekday parameter should be a value between 0-6, where 0 is Monday and 6 is Sunday. 
        The method should return the number of days as an integer;
        in your implementation, use the monthdays2calendar method of the Calendar class.

    The following are the expected results:
    Sample arguments

    year=2019, weekday=0

    Expected output

    52

    Sample arguments
    year=2000, weekday=6

    Expected output
    53
    
    """
    def testCalendarLab(self):
        pass
        import calendar
        from calendar import Calendar   
        class MyCalendar(Calendar):
            def __init__(self, *args, **kwargs) -> None:
                super().__init__(*args, **kwargs)
                # self.mycal = Calendar(*args, **kwargs)
            
            # Use for loop to generate sum
            def count_weekday_in_year(self, year, weekday) -> int:
                self.firstweekday = weekday
                tupleOfMonthDays = [self.monthdays2calendar(year, month) for month in range(1,13)]
                sum = 0
                for tupleWeek in tupleOfMonthDays:
                    for myTuple in tupleWeek:
                        if myTuple[0][0] == 0:
                            pass
                        else:
                            print(f"{len(myTuple)}{myTuple}")
                            sum += 1
                data = sum        
                return data
            
            # Use a generator to parse the 2 D calendar
            # https://www.geeksforgeeks.org/python-ways-to-flatten-a-2d-list/
            def count_weekday_in_year1(self, year, weekday) -> int:
                self.firstweekday = weekday
                weeksInMonthDays = (self.monthdays2calendar(year, month) for month in range(1,13))
                week = ( week for month in weeksInMonthDays for week in month)
                specificWeek = (specificWeek for specificWeek in week if specificWeek[0][0] != 0) 
                initial_count = (1 for count in specificWeek) 
                length = len(list(initial_count))
                return length
        
            # Use a generator to parse the 2 D calendar
            # https://www.geeksforgeeks.org/python-ways-to-flatten-a-2d-list/
            def count_weekday_in_year2(self, year, weekday) -> int:
                self.firstweekday = weekday
                weeksInMonthDays = (self.monthdays2calendar(year, month) for month in range(1,13))
                week = (week for month in weeksInMonthDays for week in month)
                specificWeek = (specificWeek for specificWeek in week if specificWeek[0][0] != 0) 
                initial_count = (1 for count in specificWeek) 
                length = len(list(initial_count))
                return length
        
        
        obj = MyCalendar(3)
        # print(obj.firstweekday)
        
        # sum = obj.count_weekday_in_year(2020, calendar.SATURDAY)
        # print(sum)
        
        
        obj.count_weekday_in_year2(2020, calendar.SATURDAY)
        
        # calendar.JANUARY
        # # import calendar  

        # c = calendar.Calendar()
        
        # the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
        # the_generator = (1 if x % 2 == 0 else 0 for x in range(10))
        
        # for month in range(1, 13):
        #     print(len(c.monthdays2calendar(2020, month)))
            
        # tupleOfMonthDays = [c.monthdays2calendar(2020, month) for month in range(1,13)]
        # print(len(tupleOfMonthDays))
        # sum = 0
        # for tupleWeek in tupleOfMonthDays:
        #     for myTuple in tupleWeek:
        #         # print(myTuple)
        #         if myTuple[0][0] == 0:
        #             pass
        #         else:
        #             print(f"{len(myTuple)}{myTuple}")
        #             sum += 1
        
      #  print(sum)
        # tupleWeek =        [lambda tupleWeek: week in tupleWeek in tupleWeek for tupleWeek in tupleOfMonthDays] #[len(myTupleWeek) for myTupleWeek in tupleOfMonthDays if myTupleWeek[0][0][0] != 0]
        # weeksLen = [len(week) for week in tupleWeek]
        # formattedWeek = [week for week in tupleWeek if tupleWeek[0][0][0] != 0]

        # resultA =          [myTupleWeek for myTupleWeek in tupleOfMonthDays]
        
        
        # result1 = (len(data) for data in )
        # result2 = sum(result1)
        # print(result2)
        
        # data = (for myTuple in c.monthdays2calendar(2020, month))
        
        # print(len(c.monthdays2calendar(2020, 1))
        # c.firstweekday = calendar.TUESDAY
        # for data in c.monthdays2calendar(2020, calendar.FEBRUARY):
        #      print(f"{len(data)}:{data}")

        # tCal = calendar.TextCalendar(2020)
        # print(tCal.itermonthdays2)
        # tCal.firstweekday = calendar.TUESDAY
        
        # for mDays in tCal.itermonthdays2(2020, 12):
        #     print(mDays)

    # PE2 Module4 Test
    def testSection4Test(self):
        pass
        import calendar
        self.assertEqual(str(calendar.weekheader(3)), "Mon Tue Wed Thu Fri Sat Sun")
        self.assertEqual(str(calendar.weekheader(1)), "M T W T F S S")
        
        
        # Lambda functions can evaluate only one expression but can have multiple arguments
        my_list = [1, 2, 3]
        myTuple =tuple(map (lambda x: x**x, my_list))  # Function and multiple iterables
        self.assertEqual(myTuple, (1, 4, 27))
        


        # Need to review formatting codes
        from datetime import datetime
        datetime = datetime(2019, 11, 27, 11, 27, 22)
        #  print(datetime.strftime('%y/%B/%d %H:%M:%S'))
        result = datetime.strftime('%y/%B/%d %H:%M:%S')
        self.assertEqual(result, '19/November/27 11:27:22')

        # bytearray initializes to x00
        b = bytearray(3)
        self.assertEqual(b, b"\x00\x00\x00")
        
        # Review read write operations for read and understand different modes
        # Filter goes throught elements and takes those that are true
        my_tuple = (0, 1, 2, 3, 4, 5, 6)
        foo = list(filter(lambda x: x-0 and x-1, my_tuple))  # 0-0 and 0-1 is false, 1-0 and 1-1 is false

        # This will print out ***
        def o(p):
            def q():
                return '*' * p
            return q
        r = o(1)
        s = o(2) 
        self.assertEqual(r()+ s(), "***")
 
 
        def I():
            s = 'abcdef'
            for c in s[::2]:   # Range starts default at 0 and indexes by two. ace
                yield  c
        result = [x for x in I()]
        self.assertEqual(result, ['a', 'c', 'e'])
                                
                                  
        def fun(n):
            s = '+'
            for i in range (n):
                s += s
                # print(s)
                yield s
          
        
        myStr = ""       
        for x in fun(2): # x=0 adds ++ and x=1 adds ++++
        #     print(x, end='')  
            myStr += x
        self.assertEqual(myStr, '++++++')
        
 
        
    def testPCAPPracticeTest(self):
        # Create a filter to get a list with 1,9
        numbers = [i*i for i in range(5)]   # Creates [0, 1,4,9, 16]
        result = list(filter(lambda x: x%2, numbers))
        self.assertEqual(result, [1,9])
        
        result = list(filter(lambda x: x/2, numbers))
        self.assertEqual(result, [1, 4, 9, 16])
        

        from datetime import datetime
        datetime_1 = datetime(2019, 11, 27, 11, 27, 22)
        datetime_2 = datetime(2019, 11, 27, 0, 0, 0 )
        self.assertEqual(str(datetime_1 - datetime_2), "11:27:22")
        # print(datetime_1 - datetime_2)
 
        datetime_1 = datetime(2019, 11, 30, 11, 27, 22)
        datetime_2 = datetime(2019, 11, 27, 0, 0, 0 )
        self.assertEqual(str(datetime_1 - datetime_2), "3 days, 11:27:22")
 

        from datetime import timedelta, datetime
        d = timedelta(days=2)
        day = datetime(2019, 11, 27, 0, 0, 0 )
        self.assertEqual( str(day+d), "2019-11-29 00:00:00")
 
        import random
        # What can produce 6, 82, 0

        #    def randrange(self, start, stop=None, step=_ONE):
        #     def randrange(self, start, stop=None, step=_ONE):
        # """Choose a random item from range(stop) or range(start, stop[, step]).
        
        #     def randint(self, a, b):
        # """Return random integer in range [a, b], including both end points.
        
        #         """Choose a random element from a non-empty sequence."""
        success = False

        for x in range(10000):
            a = random.randint(0, 100)
            b = random.randrange( 10, 100, 3)
            c = random.choice((0, 100, 3))
        
            # print(f"a:{a} b:{b} c:{c}")
            # What can produce 6, 82, 0
            
            if (a==6 and b==82 and c==0):
                success = True
                self.assertTrue(result, f"Successful after {x} tries")
                #  print(f"a:{a} b:{b} c:{c} after {x} tries")
                break
            else:
                continue
        
        if success is False:
            self.assertFalse(success, "Unable to find random match")
        

        class A:
            def __init__(self) -> None:
                pass
            
        # Type errors are thrown due to invalid types 
        # In this case passing a parameter to init without support
        with self.assertRaises(TypeError): 
                            #    "You can not pass a parameter to init if it is not specified in arguments list."):
            a = A(1)
        a = A()
        self.assertFalse(hasattr(a, 'A'))
        self.assertFalse(hasattr(A, 'a'))
        
        self.assertIsInstance(a, A)
            
        # pip commands
        # pip install package 
        # pip uinstall package
        # pip --version
        # pip3 --version
 
 
        # https://docs.python.org/3/library/exceptions.html       
#         aseException
# BaseException
#  ├── BaseExceptionGroup
#  ├── GeneratorExit
#  ├── KeyboardInterrupt
#  ├── SystemExit
#  └── Exception
#       ├── ArithmeticError
#       │    ├── FloatingPointError
#       │    ├── OverflowError
#       │    └── ZeroDivisionError
#       ├── AssertionError
#       ├── AttributeError
#       ├── BufferError
#       ├── EOFError
#       ├── ExceptionGroup [BaseExceptionGroup]
#       ├── ImportError
#       ├── LookupError
#       │    ├── IndexError
#       │    └── KeyError
#       ├── MemoryError
#       ├── NameError
#       ├── OSError
#       ├── ReferenceError
#       ├── RuntimeError
#       ├── StopAsyncIteration
#       ├── StopIteration
#       ├── SyntaxError
#       ├── SystemError
#       ├── TypeError
#       ├── ValueError
#       └── Warning
#  
    
        try:
            raise Exception
        except BaseException:
            self.assertTrue(True, "This is where we will hit")
        except Exception:
            self.assertTrue(False, "Will never get here")
            print("Exception")
        except:
            self.assertTrue(False, "Will never be here")
            print("except")
                
                    
        class A:
            A = 1
            def __init__(self) -> None:
                    self.a = 0
    
        self.assertFalse(hasattr(A, 'a'), 
                         "self.a does not exist in class A. It is an instance object")

        self.assertTrue(hasattr(A, 'A'), "class property A exists in class A ")                        
        obj = A()
        self.assertTrue(hasattr(obj, 'a'), "instance property a exists in instance obj")
        self.assertTrue(hasattr(obj, 'A'), "Class property can be accessed and exists in object")
        
        class A:
            def __init__(self, v = 2) -> None:
                self.v = v
            def set(self, v=1):
                self.v += v
                return self.v
        
        a = A()  # v=2
        b = a    # same object id
        self.assertEqual(id(a), id(b))    
        b.set()  # Adds default one to instance variable self.v
        self.assertEqual(a.v, 3, "Default set to two. Callng set adds 1 to instance variable self.v")
            
            
        
 
if __name__ == "__main__":
    unittest.main(), 