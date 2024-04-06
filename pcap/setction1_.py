import unittest

class TestModuleOne(unittest.TestCase):

    #  1.1.1.6 Importing a module | math
    def testImportingAModule(self):
        import math
        from math import pi
        def sin(x):
            if 2 * x == pi:
                return 0.99999999
        pi = 3.14

        self.assertEqual(sin (pi/2), .99999999, "custom version of pi")
        self.assertEqual(math.sin(math.pi/2), 1.0, "math.sin version of pi")

    # 1.1.1.7 Importing a module | math
    def testImportFrom(self):
        from math import pi, sin
        self.assertEqual(pi, 3.141592653589793, "Use import of pi from math")
        self.assertEqual(sin(pi/2), 1.0, "Use explicit import of math function sin and value pi")

    # 1.1.1.8 Importing a module | math
    def testOverWriteLocal(self):
        pi = 3.14
        def sin(x):
            if 2 * x == pi:
                return 0.99999999
            else:
                return None
    
        self.assertEqual(pi/2, 1.57, "Use custom pi value")
        self.assertEqual(sin(3.14/2), 0.99999999, "Use custom sin function")

        from math import sin, pi
        self.assertEqual(sin(pi / 2), 1.0, "Use math sin function and pi value")

    # # 1.1.1.10 Importing a module
    def testImportAsAlias(self):
        import math as m
        self.assertEqual(m.sin(m.pi/2), 1.0, "Use math pi value, and sin function")

    # #  1.2.1.1 Useful Modules
    def testDirMath(self):
        import math as mathLib
        self.assertEqual(len(dir(mathLib)), 66)
            #  data = dir(mathLib)
   

        


    # # 1.2.1.2 Useful modules | math
    def testMathFunctions(self):
        # from math import pi, radians, degrees, sin, cos, tan, asin
        # ad = 90
        # ar = radians(ad)
        # ad = degrees(ar)

        from math import e, exp, log
        self.assertEqual(pow(2,2), 4, "pow(2,2) is 4")
        self.assertEqual(pow(10,2), 100, "pow(10,2) is 100" )
        self.assertEqual(e, 2.718281828459045, "Math value of e is 2.718281828459045" )
        self.assertEqual(pow(e,1), 2.718281828459045, "e^1 or pow(e,1) is 2.718281828459045")
        self.assertEqual(log(e), 1, "Defaults to natural logarithm of e")
        self.assertEqual(log(e, e), log(e), "Log of e to base e which is 1  log(e)==log(e,e)")
        self.assertEqual(log(8, 2), 3, "log(8,2) is 3")

        self.assertEqual(exp(0), 1, "exp(0) is the same e^0 which is 1")
        self.assertEqual(exp(1), 2.718281828459045, "exp(1) is the same e^1")
        self.assertEqual(exp(2), 7.38905609893065, "exp(2) is the same e^2")
        self.assertEqual(exp(3), 20.085536923187668, "exp(3) is the same e^3")
        self.assertEqual(exp(4), 54.598150033144236, "exp(4) is the same e^4")

        self.assertEqual(log(2), 0.6931471805599453, "log(2) is the same as a ln(2)")
        self.assertEqual(log(2), 0.6931471805599453, "log(e, 2) is the same as a ln(2)")
        
        self.assertEqual(2*log(2), 1.3862943611198906, "2*log(2) = 2*ln(2)")
        self.assertEqual(exp(2 * log(2)), 4, "4")
        self.assertEqual(exp(2 * 0.6931471805599453), 4, "4")
        self.assertAlmostEqual(exp(2*1.3862943611198906), 15.999999999999998,  "Close to 16")

        self.assertAlmostEqual(pow(e, 1.38628), 4, places=3)
        self.assertAlmostEqual(pow(e, 2*1.3862943), 16, places=5)
        self.assertAlmostEqual(pow(e, 2*1.38629436), 16)   # Defrault places = 7
        
        #  1.2.1.3 Useful modules | math
        from math import e, exp, log
        self.assertTrue(pow(e, 1) == exp(log(e)))       # e^1
        self.assertTrue(pow(2, 2) == exp(2 * log(2)))   # 2^2
        self.assertTrue(log(e, e) == exp(0))            # e^0=1

    # Sample ceil, floor, trnc
    # 1.2.1.4 Useful module        
    def testFloorCeilTrunc(self):
        from math import ceil, floor, trunc, hypot, factorial
        x = 1.4
        y = 2.6

        self.assertEqual(floor(x), 1)
        self.assertEqual(floor(y), 2)
        self.assertEqual(floor(-x), -2)
        self.assertEqual(floor(-y), -3)

        self.assertEqual(ceil(x), 2)
        self.assertEqual(ceil(y), 3)
        self.assertEqual(ceil(-x), -1)
        self.assertEqual(ceil(-y), -2)

        self.assertEqual(trunc(x), 1)
        self.assertEqual(trunc(y), 2)
        self.assertEqual(trunc(-x), -1)
        self.assertEqual(trunc(-y), -2)


        self.assertEqual(hypot(3,4), 5)
        self.assertEqual(factorial(5), 120)

    #  1.2.1.5 Useful Modules | random
    def testRandom(self):
        from random import random

        for i in range(5):
            i = random()
            self.assertLess(i, 1)
            self.assertGreater(i, 0)

        # Set seed to constant will get close to same value everytime
        from random import seed
        seed(0)
        self.assertAlmostEqual(random(),0.844421851525)
        self.assertAlmostEqual(random(),0.75795440294)
        self.assertAlmostEqual(random(),0.420571580831)
        self.assertAlmostEqual(random(),0.258916750293)
        self.assertAlmostEqual(random(),0.511274721369)
        
        
        import random
        from datetime import datetime
        random.seed(datetime.now().timestamp())
        from random import randrange, randint
        self.assertEqual(randrange(1), 0)      # Can only be 0 since it ends at 1 
        self.assertEqual(randrange(0, 1), 0)   # Can only be 0, Begins at 0 and ends at 1
        self.assertGreaterEqual(randrange(0, 1, 1), 0)   # Can only be 0, Begins at 0 and ends at 1, increments 0f 1


        from random import choice, sample
        main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        result = choice(main_list)
        self.assertIn(choice(main_list), main_list, "Choose one element from list")


        sublist = sample(main_list, 5)
        self.assertEqual(set(sublist).intersection(set(main_list)), set(sublist), "Choose sublist from main_list")

        sublist1 = sample(main_list, 10)
        self.assertEqual(set(sublist1).intersection(set(main_list)), set(sublist1), "Choose sublist from main_list all elements")
        self.assertRaises(ValueError, sample, main_list, 11) # "Choosing more elements than is available in lists generates ValueError")
       
    # 1.2.1.10 Useful modules | platform
    def testPlatform(self):
        from platform import platform, machine, processor, system, version
        from platform import python_implementation, python_version_tuple, python_version, python_compiler, python_revision
        
        self.assertEqual(platform(aliased=True, terse=True), "Windows-11")
        self.assertEqual(machine(), "AMD64")

        machine_hardware = machine()
        match(machine_hardware):
            case "AMD64":
                self.assertEqual(machine(), "AMD64")
            case "x86_64":
                self.assertEqual(machine(), "x86_64")
            case "armv7l":
                self.assertEqual(machine(), "armv7l")
            case _:
                self.assertTrue(False, f"Hardware does not match expected type, reported as  {machine_hardware}")

        proc = processor()
        match(proc):
            case "arv71":
                self.assertEqual(proc, "arv71")
            case "x86":
                self.assertEqual(proc, "x86")
            case "Intel64 Family 6 Model 186 Stepping 3, GenuineIntel":
                self.assertEqual(proc, "Intel64 Family 6 Model 186 Stepping 3, GenuineIntel")
            case _:
                self.assertTrue(False, f"Processor does not march, reported as {proc}")

        sys = system()
        match(sys):
            case "Windows":
                self.assertEqual(sys, "Windows")
            case "Linux":
                self.assertEqual(sys, "Linux")
            case _:
                self.assertTrue(False, f"system() not recognized, reported as {sys}")

        print(version())

        print(f"python_implementation:{python_implementation()}, python_version_tuple:{python_version_tuple()}")
        print(f"python_version:{python_version()}, python_compiler:{python_compiler()}, python_revision:{python_revision()}")



if __name__ == "__main__":
    unittest.main()