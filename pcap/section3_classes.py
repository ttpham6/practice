import unittest
from io import StringIO
from contextlib import redirect_stdout   # Redirect print output

class TestSection3(unittest.TestCase):
    def printToVar(self, obj) -> str:
        text_trap = StringIO()
        with redirect_stdout(text_trap):
            print(obj, end="")
            return text_trap.getvalue()

    def printFunction(self, *args) -> str:
        text_trap = StringIO()
        global func, input

        if len(args) == 0:
            raise ValueError("Need a function to call")
        else:
            func = args[0]
        if len(args) > 1:
            input = args[1: len(args)]

        with redirect_stdout(text_trap):
            if len(args) == 1:
                func()
            else:
                func(*input)
            return text_trap.getvalue()


    """
    a noun – you probably define the object's name;
    an adjective – you probably define the object's property;
    a verb – you probably define the object's activity.

    """
    def testClassCreation(self):
        class SampleClass():
            pass
            def testMethod():
                pass


        obj = SampleClass()



        self.assertIsInstance(obj, SampleClass)
        with self.assertRaises(AttributeError):
            obj.Fake()


    """_summary_: stack - lifo last in first out
    """
    def testStackPractice(self):
        stack = []

        def push(val):
            stack.append(val)

        def pop():
            val = stack[-1]
            del stack[-1]
            return val

        [push(x) for x in range(0, 20, 2)]
        self.assertEqual((pop()), 18)

        class Stack:
            def __init__(self):
                self.__stack_list = []


            def push(self, val):
                self.__stack_list.append(val)

            def pop(self):
                val = self.__stack_list[-1]
                del self.__stack_list[-1]
                return val

        stack_object = Stack()
        stack_object.push(3)
        stack_object.push(2)
        stack_object.push(1)
        self.assertEqual(stack_object.pop(), 1)
        self.assertEqual(stack_object.pop(), 2)
        self.assertEqual(stack_object.pop(), 3)

        # Can not access privat attribute
        with self.assertRaises(AttributeError):
            (len(stack_object.__stack_list))

        stack_object_1 = Stack()
        stack_object_2 = Stack()

        stack_object_1.push(3)
        stack_object_2.push(stack_object_1.pop())

        self.assertTrue(stack_object_2.pop(), 3)

        little_stack = Stack()
        another_stack = Stack()
        funny_stack = Stack()

        little_stack.push(1)
        another_stack.push(little_stack.pop() + 1)
        funny_stack.push(another_stack.pop() - 2)
        self.assertEqual(funny_stack.pop(), 0)

        class AddingStack(Stack):
            def __init__(self):
                super().__init__()
                self.__sum = 0

            def push(self, val):
                self.__sum += val
                Stack.push(self, val)

            def pop(self):
                val = Stack.pop(self)
                self.__sum -= val
                return val

            def get_sum(self):
                return self.__sum

        stack_object = AddingStack()
        for i in range(5):
            stack_object.push(i)
        self.assertEqual(stack_object.get_sum(), 10)

        for i in range(4, -1, -1):
            self.assertEqual(stack_object.pop(), i)


        class CountingStack(Stack):
            def __init__(self):
                super().__init__()
                self.__counter = 0

            def get_counter(self):
                return self.__counter

            def pop(self):
                Stack.pop(self)
                self.__counter += 1

            def push(self, i):
                Stack.push(self, i )
                self.__counter += 1

        stk = CountingStack()
        for i in range(100):
            stk.push(i)
            stk.pop()
        self.assertEqual(stk.get_counter(), 200)

        class QueueError(AttributeError):
            pass

        # FIFO
        class Queue():
            def __init__(self) -> None:
                self.__queue_list = []

            def put(self, val):
                self.__queue_list.append(val)

            def __repr__(self) -> str:
                return (f"{self.__class__.__name__}{id(self)}")

                return "Queue"

            def get(self):
                try:
                    val = self.__queue_list[0]       # First in First Out Get the first element in the list
                    del self.__queue_list[0]

                    return val
                except:
                    raise QueueError(f"There are no more values in the Queue object:{self}:len {len(self.__queue_list)}")


        q = Queue()
        for i in range(11):
            q.put(i)

        for i in range(0, 11):
            self.assertEqual(q.get(), i)

        with self.assertRaises(QueueError):
            q.get()

        """
        Objectives
        improving the student's skills in defining subclasses;
        adding a new functionality to an existing class.

        Scenario
        Your task is to slightly extend the Queue class' capabilities. We want it to have a parameterless method that returns True if the queue is empty and False otherwise.
        Complete the code we've provided in the editor. Run it to check whether it outputs a similar result to ours.
        Below you can copy the code we used in the previous lab:
        """
        class SuperQueue(Queue):
            def __init__(self) -> None:
                super().__init__()

            # revisit: tampham Understand why self.__queue_list does not work here
            def __len__(self) -> int:
                return len(self._Queue__queue_list)

            def isempty(self) -> bool:
                result = False
                if(len(self._Queue__queue_list) == 0):
                    result = True
                else:
                    result = False
                return result

        q1 = SuperQueue()
        for i in range(11):
            q1.put(i)
        self.assertEqual(len(q1), 11)
        self.assertFalse(q1.isempty())

    def testProperties(self):
        class ExampleClass:
            def __init__(self, val = 1):
                self.first = val

            def set_second(self, val):
                self.second = val

        example_object_1 = ExampleClass()
        example_object_2 = ExampleClass(2)

        example_object_2.set_second(3)

        example_object_3 = ExampleClass(4)
        example_object_3.third = 5

        # Three types of instance variables
        self.assertDictEqual(example_object_1.__dict__, {'first': 1}, "Property created bot __init__." )
        self.assertDictEqual(example_object_2.__dict__, {'first': 2, "second": 3}, "Property created by object method.")
        self.assertDictEqual(example_object_3.__dict__, {'first': 4, "third": 5}, "New property created by object assignment.")

        class ExampleClass1:
            def __init__(self, val = 1):
                self.__first = val

            def set_second(self, val = 2):
                self.__second = val

        example_object_1 = ExampleClass1()
        example_object_2 = ExampleClass1(2)

        example_object_2.set_second(3)

        example_object_3 = ExampleClass1(4)
        example_object_3.__third = 5

        self.assertDictEqual(example_object_1.__dict__, {"_ExampleClass1__first": 1}, "Name managed added underscore and class name.")
        self.assertDictEqual(example_object_2.__dict__, {"_ExampleClass1__first": 2, "_ExampleClass1__second": 3},  "Name managed added underscore and class name.")

        # This is different than in tutorial which shows __third.  For this example we are creating the new property as part of the class TestSection3
        self.assertDictEqual(example_object_3.__dict__, {"_ExampleClass1__first": 4, "_TestSection3__third": 5}, "In this case class _TestSection3 is the test class name. ")


        # Class variables
        class ExampleClass3:
            counter = 0

            def __init__(self, val = 1):
                self.__first = val
                ExampleClass3.counter += 1

        example_object_a = ExampleClass3()
        example_object_b = ExampleClass3(2)
        example_object_c = ExampleClass3(4)

        # Note that class variable is not in object dictionary
        self.assertDictEqual(example_object_a.__dict__, {"_ExampleClass3__first": 1})
        self.assertDictEqual(example_object_b.__dict__, {"_ExampleClass3__first": 2})
        self.assertDictEqual(example_object_c.__dict__, {"_ExampleClass3__first": 4})

        # Class variable counter can be accessed by prepending class name
        # Three instances created tracked by counter.
        self.assertEqual(ExampleClass3.counter, 3)

        # Class variable can also be accessed via object instance
        self.assertEqual(example_object_a.counter, 3)
        self.assertEqual(example_object_b.counter, 3)
        self.assertEqual(example_object_c.counter, 3)

        # "_ExampleClass3__counter": 1})
        # print(example_object_a.__dict__, example_object_a.counter)
        # print(example_object_b.__dict__, example_object_b.counter)
        # print(example_object_c.__dict__, example_object_c.counter)

        class ExampleClass4:
            __counter = 0
            def __init__(self, val = 1):
                self.__first = val
                ExampleClass4.__counter += 1

        example_object_x = ExampleClass4()
        example_object_y = ExampleClass4(2)
        example_object_z = ExampleClass4(4)

        # Note that class variable is not in object dictionary
        self.assertDictEqual(example_object_x.__dict__, {"_ExampleClass4__first": 1})
        self.assertDictEqual(example_object_y.__dict__, {"_ExampleClass4__first": 2})
        self.assertDictEqual(example_object_z.__dict__, {"_ExampleClass4__first": 4})

        self.assertEqual(example_object_x._ExampleClass4__counter, 3)

        # Difference beteen class variable and instance varaible
        class ExampleClass5:
            varia = 1
            def __init__(self, val):
                ExampleClass5.varia = val

        #self.assertEqual(ExampleClass5.__dict__, {"varia": 1})

        self.assertEqual(ExampleClass5.__dict__.get("varia"), 1, "Class variable varia var exists in class dict")
        example_objectw = ExampleClass5(2)
        self.assertEqual(ExampleClass5.__dict__.get("varia"), 2, "Class variable set to 2 init")
        self.assertEqual(example_objectw.varia, 2, "Class variable int varia can be accessed via object" )
        self.assertDictEqual(example_objectw.__dict__, {}, "Object dictionary is empty since no variables have been created")


        # Instance variables on a or b can exist
        class Example6Class:
            def __init__(self, val):
                if val % 2 != 0:
                    self.a = 1
                else:
                    self.b = 1

        example_objectv = Example6Class(1)
        self.assertDictEqual(example_objectv.__dict__, {"a": 1})
        self.assertIsNone(example_objectv.__dict__.get("b"), "Variable b does not exist in dictionary return None" )

        # We can check for the existence of an attribute via hasattr
        self.assertTrue(hasattr(example_objectv, "a"), "Object has variable a")
        self.assertFalse(hasattr(example_objectv, "b"), "Object does not have variable b")


        class Example7Class:
            a = 1
            def __init__(self):
                self.b = 2


        example_objectu = Example7Class()
        # We can check for class variables as well
        self.assertTrue(hasattr(Example7Class, "a"), "Class has variable a")
        self.assertTrue(hasattr(example_objectu, "a"), "Object has variable a as well since we can access i")
        self.assertFalse(hasattr(example_objectu, "z"), "Object does not have variable z")

    """Section 3.4"""
    def testClasses(self):
        class Classy:
            pass

        obj = Classy()
        self.assertEqual(Classy.__name__, "Classy", "Class name can be accessed via __name__")
        with self.assertRaises(AttributeError):  # Can not access __name__ of class directly
            print(obj.__name__)
        self.assertIsInstance(obj, Classy)
        # Note this examples generates class name as subset of TestSection3 class
        self.assertTrue(type(obj).__name__.endswith("Classy"), "Can find class name via type function")


        if __name__ == "__main__":
            self.assertEqual(obj.__module__, "__main__", "Module will be main if run as a standalone program")

        class SuperOne:
            pass
        class SuperTwo:
            pass
        class Sub(SuperOne, SuperTwo):
            pass

        def printBases(cls):
            print('( ', end='')

            for x in cls.__bases__:
                print(x.__name__, end=' ')
            print(')')

        # printBases(SuperOne)
        # printBases(SuperTwo)
        # printBases(Sub)
        self.assertTupleEqual(SuperOne.__bases__, (object,), "Class has default object parent")
        self.assertTupleEqual(SuperTwo.__bases__, (object,), "Class has default object parent")
        self.assertTupleEqual(Sub.__bases__, (SuperOne, SuperTwo), "Sub is a child of SuperOne and SuperTwo")

    def testReflectionIntrospection(self):
        class MyClass:
            pass

        obj = MyClass()
        obj.a = 1
        obj.b = 2
        obj.i = 3
        obj.ireal = 3.5
        obj.integer = 4
        obj.z = 5

        def incIntsI(obj):
            for name in obj.__dict__.keys():
                if name.startswith('i'):
                    val = getattr(obj, name)
                    if isinstance(val, int):
                        setattr(obj, name, val + 1)


        # print(obj.__dict__)
        incIntsI(obj)
        # print(obj.__dict__)
        self.assertEqual(obj.__dict__.get('i'), 4, "Incremented by one since it is an integer starting with i")
        self.assertEqual(obj.__dict__.get('ireal'), 3.5, "Stays the same since it is a real number")
        self.assertEqual(obj.__dict__.get('integer'), 5, )
        setattr(obj, "ireal", 7)
        # print(obj.__dict__)

    """
    3.4.1.12 The Timer class
    Estimated time
        30-60 minutes

    Level of difficulty
        Easy/Medium

    Objectives
        improving the student's skills in defining classes from scratch;
        defining and using instance variables;
        defining and using methods.

Scenario
We need a class able to count seconds. Easy? Not as much as you may think as we're going to have some specific expectations.
Read them carefully as the class you're about write will be used to launch rockets carrying international missions to Mars. It's a great responsibility. We're counting on you!
Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from range [0..23] - we will be using the military time), minutes (from range [0..59]) and seconds (from range [0..59]).
Zero is the default value for all of the above parameters. There is no need to perform any validation checks.

The class itself should provide the following facilities:

    objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10;
    the class should be equipped with parameterless methods called next_second() and previous_second(), incrementing the time stored inside objects by +1/-1 second respectively.

Use the following hints:

    all object's properties should be private;
    consider writing a separate function (not method!) to format the time string.

Complete the template we've provided in the editor. Run your code and check whether the output looks the same as ours.
Expected output

23:59:59
00:00:00
23:59:59

    Class called time
    Methods
    __init__, __str__, next_second, prev_second, __repr (as needed )
    init takes hours (military), minutes, seconds

    Properties are private

    Function to format time string
    formatTime from military to civilian

    """
    def testTimeClass(self):
        class Timer():
            def __init__(self, hours, minutes, seconds, militaryTime = True) -> None:
                self.__hours = hours
                self.__minutes = minutes
                self.__seconds = seconds

                self._militaryTime = militaryTime
                if self._militaryTime:
                    self.maxHours = 23
                else:
                    self.maxHours = 12

            def __str__(self) -> str:
                if self.__hours < 10:
                    hourString = f"0{self.__hours}"
                else:
                    hourString = str(self.__hours)
                if self.__minutes < 10:
                    minuteString = f"0{self.__minutes}"
                else:
                    minuteString = str(self.__minutes)
                if self.__seconds < 10:
                    secondString = f"0{self.__seconds}"
                else:
                    secondString = str(self.__seconds)

                return "{}:{}:{}".format(hourString, minuteString, secondString )

            def __repr__(self) -> str:
                return self.__str__

            def next_second(self):
                if self.__seconds < 59:
                    self.__seconds +=1
                elif self.__seconds == 59:
                    self.__seconds = 0
                    if self.__minutes < 59:
                        self.__minutes += 1
                    elif self.__minutes == 59:
                        self.__minutes = 0
                        if self.__hours < self.maxHours:
                            self.__hours += 1
                        elif self.__hours == self.maxHours:
                            self.__hours = 0
                            if not self._militaryTime:
                                self.__hours = 1


            def prev_second(self):
                if self.__seconds > 0:
                    self.__seconds -=1
                elif self.__seconds == 0:
                    self.__seconds = 59
                    if self.__minutes > 0:
                        self.__minutes -= 59
                    elif self.__minutes == 0:
                        self.__minutes = 59
                        if self.__hours > 0:
                            self.__hours -= 1
                        elif self.__hours == 0:
                            self.__hours = self.maxHours

            def militaryTime(self, state: bool):
                if state:
                    self._militaryTime = True
                    self.maxHours = 24
                else:
                    self._militaryTime = False
                    self.maxHours = 12


        obj = Timer(23, 59, 59)
        self.assertEqual(str(obj), "23:59:59")
        obj.next_second()
        self.assertEqual(str(obj), "00:00:00")
        obj.next_second()
        self.assertEqual(str(obj), "00:00:01")

        obj = Timer(0, 0, 1)
        self.assertEqual(str(obj), "00:00:01")
        obj.prev_second()
        self.assertEqual(str(obj), "00:00:00")
        obj.prev_second()
        self.assertEqual(str(obj), "23:59:59")

        def formatTime(obj, militaryTime: bool):
            if isinstance(obj, Timer):
                obj.militaryTime(False)

        formatTime(obj, False)

        obj = Timer(11, 59, 59)
        self.assertEqual(str(obj), "11:59:59")
        obj.next_second()
        self.assertEqual(str(obj), "12:00:00")
        obj.next_second()
        self.assertEqual(str(obj), "12:00:01")

        obj = Timer(12, 59, 59)
        formatTime(obj, False)
        self.assertEqual(str(obj), "12:59:59")
        obj.next_second()
        self.assertEqual(str(obj), "01:00:00")
        obj.next_second()
        self.assertEqual(str(obj), "01:00:01")


        obj = Timer(12, 0, 1)
        self.assertEqual(str(obj), "12:00:01")
        obj.prev_second()
        self.assertEqual(str(obj), "12:00:00")
        obj.prev_second()
        self.assertEqual(str(obj), "11:59:59")

    """  3.4.1.13 LAB: Days of the week
    Estimated time
    30-60 minutes

    Level of difficulty
    Easy/Medium

    Objectives
        improving the student's skills in defining classes from scratch;
        defining and using instance variables;
        defining and using methods.

    Scenario
    Your task is to implement a class called Weeker. Yes, your eyes don't deceive you – this name comes from the fact that objects of that class will be able to store and to manipulate the days of the week.
    The class constructor accepts one argument – a string. The string represents the name of the day of the week and the only acceptable values must come from the following set:

    Mon Tue Wed Thu Fri Sat Sun

    Invoking the constructor with an argument from outside this set should raise the WeekDayError exception (define it yourself; don't worry, we'll talk about the objective nature of exceptions soon). The class should provide the following facilities:
        objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the same form as the constructor arguments;
        the class should be equipped with one-parameter methods called add_days(n) and subtract_days(n), with n being an integer number and updating the day of week stored inside the object in the way reflecting the change of date by the indicated number of days, forward or backward.
        all object's properties should be private;

    Complete the template we've provided in the editor and run your code and check whether your output looks the same as ours.

    Expected output
        Mon
        Tue
        Sun
        Sorry, I can't serve your request.

    """
    def testWeeker(self):
        class WeekDayError(AttributeError):
            pass

        class Weeker:
            __ValidDayOfWeek = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

            def __init__(self, day):
                if day in Weeker.__ValidDayOfWeek:
                   self.__day = day
                else:
                    raise WeekDayError(f"Invalid day entered: {day}. Please enter ValidDayOfWeek {Weeker.__ValidDayOfWeek}")

            def __str__(self):
                return self.__day

            def __repr__(self):
                return f'Weeker("{self.__day}")'

            def add_days(self, n):
                lengthOfWeek = len(Weeker.__ValidDayOfWeek)
                updated_index = Weeker.__ValidDayOfWeek.index(self.__day) + n
                new_index = updated_index % lengthOfWeek
                self.__day = Weeker.__ValidDayOfWeek[new_index]

            def subtract_days(self, n):
                self.add_days(-n)


        weekday = Weeker('Mon')
        self.assertEqual(str(weekday), "Mon")
        weekday.add_days(15)
        self.assertEqual(str(weekday), "Tue")
        weekday.subtract_days(23)
        self.assertEqual(str(weekday), "Sun")
        with self.assertRaises(WeekDayError):
            weekday = Weeker('Monday')

        # revisit: tampham examples for working with __repr__ and f string versus format
        # print(repr(weekday))
        # obj1 = repr(weekday)
        # print(type(obj1))
        # test = "example"
        # outuputString = f'Weeker("{test}")'
        # print(outuputString)
        # outuputString = "Weeker/(/"/{}/"/)".format(test)
        # print(outuputString)

    # """  3.4.1.14 Points on a plane
    # Estimated time
    # 30-60 minutes

    # Level of difficulty
    # Easy/Medium
    # Objectives

    #     improving the student's skills in defining classes from scratch;
    #     defining and using instance variables;
    #     defining and using methods.

    # Scenario
    # Let's visit a very special place - a plane with the Cartesian coordinate system (you can learn more about this concept here: https://en.wikipedia.org/wiki/Cartesian_coordinate_system).
    # Each point located on the plane can be described as a pair of coordinates customarily called x and y. We expect that you are able to write a Python class which stores both coordinates as float numbers. Moreover, we want the objects of this class to evaluate the distances between any of the two points situated on the plane.
    # The task is rather easy if you employ the function named hypot() (available through the math module) which evaluates the length of the hypotenuse of a right triangle (more details here: https://en.wikipedia.org/wiki/Hypotenuse) and here: https://docs.python.org/3.7/library/math.html#trigonometric-functions.
    # This is how we imagine the class:
    #     it's called Point;
    #     its constructor accepts two arguments (x and y respectively), both default to zero;
    #     all the properties should be private;
    #     the class contains two parameterless methods called getx() and gety(), which return each of the two coordinates (the coordinates are stored privately, so they cannot be accessed directly from within the object);
    #     the class provides a method called distance_from_xy(x,y), which calculates and returns the distance between the point stored inside the object and the other point given as a pair of floats;
    #     the class provides a method called distance_from_point(point), which calculates the distance (like the previous method), but the other point's location is given as another Point class object;

    # Complete the template we've provided in the editor and run your code and check whether your output looks the same as ours.
    # Expected output

    # 1.4142135623730951
    # 1.4142135623730951


    def testPointsOnAPlane(self):

        from math import hypot
        class Point:
            def __init__(self, x=0.0, y=0.0):
                self.__x = x
                self.__y = y

            def getx(self) -> float:
                return self.__x

            def gety(self) -> float:
                return self.__y

            def distance_from_xy(self, x: float, y: float) -> float:
                return hypot(self.__x, self.__y, x, y)

            def distance_from_point(self, point: float) -> float:
                if not isinstance(point, Point):
                    return None
                else:
                    x = point.getx()
                    y = point.gety()
                    return hypot(self.__x, self.__x, x, y)

        zeroPoint = Point(0, 0)
        trianglePoint = Point(3,4)
        self.assertEqual(zeroPoint.distance_from_xy(3,4), 5)
        self.assertEqual(zeroPoint.distance_from_point(trianglePoint), 5)

        point1 = Point(0, 0)
        point2 = Point(1, 1)
        self.assertEqual(point1.distance_from_point(point2), 1.4142135623730951 )
        self.assertEqual(point1.distance_from_xy(1,1), 1.4142135623730951  )


    # """ 3.4.1.15 Triangle
    # Estimated time
    # 30-60 minutes

    # Level of difficulty
    # Medium

    # Objectives
    #     improving the student's skills in defining classes from scratch;
    #     using composition.

    # Scenario
    # Now we're going to embed the Point class (see Lab 3.4.1.14) inside another class. Also, we're going to put three points into one class, which will let us define a triangle. How can we do it?

    # The new class will be called Triangle and this is the list of our expectations:

    #     the constructor accepts three arguments - all of them are objects of the Point class;
    #     the points are stored inside the object as a private list;
    #     the class provides a parameterless method called perimeter(), which calculates the perimeter of the triangle described by the three points; the perimeter is a sum of all legs' lengths (we mention it for the record, although we are sure that you know it perfectly yourself.)

    # Complete the template we've provided in the editor. Run your code and check whether the evaluated perimeter is the same as ours.

    # Below you can copy the Point class code we used in the previous lab:


    # Expected output
    # 3.414213562373095
    # """
    def testTriangle(self):

        from math import hypot
        class Point:
            def __init__(self, x=0.0, y=0.0):
                self.__x = x
                self.__y = y

            @property
            def x(self):
                return self.__x

            @property
            def y(self):
                return self.__y

            def distance_from_xy(self, x: float, y: float) -> float:
                return hypot(self.__x, self.__y, x, y)

            def distance_from_point(self, point: float) -> float:
                if not isinstance(point, Point):
                    return None
                else:
                    x = point.x
                    y = point.y
                    return hypot(self.__x, self.__x, x, y)


        zeroPoint = Point(0, 0)
        trianglePoint = Point(3,4)
        self.assertEqual(zeroPoint.distance_from_xy(3,4), 5)
        self.assertEqual(zeroPoint.distance_from_point(trianglePoint), 5)

        point1 = Point(0, 0)
        point2 = Point(1, 1)
        self.assertEqual(point1.distance_from_point(point2), 1.4142135623730951 )
        self.assertEqual(point1.distance_from_xy(1,1), 1.4142135623730951  )

        class Triangle:
            def __init__(self, vertice1, vertice2, vertice3):
                self.__point0 = vertice1
                self.__point1 = vertice2
                self.__point2 = vertice3

            def perimeter(self):
                distanceVertexV0toV1 = hypot(self.__point0.x, self.__point0.y, self.__point1.x, self.__point1.y)
                distanceVertexV0toV2 = hypot(self.__point0.x, self.__point0.y, self.__point2.x, self.__point2.y)
                distanceVertexV1toV3 = hypot(self.__point1.x, self.__point1.y, self.__point2.x, self.__point2.y)
                totalPerimeter = distanceVertexV0toV1 + distanceVertexV0toV2 + distanceVertexV1toV3
                return totalPerimeter

        triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
        self.assertEqual(triangle.perimeter(), 3.414213562373095)


    def test_str(self):
        class Star:
            def __init__(self, name, galaxy):
                self.name = name
                self.galaxy = galaxy

            def __str__(self):
                return self.name + ' in ' + self.galaxy

            def __repr__(self) -> str:
                return self.name + ' in ' + self.galaxy

        sun = Star("Sun", "Milky Way")
        from io import StringIO
        from contextlib import redirect_stdout   # Redirect print output
        text_trap = StringIO()
        with redirect_stdout(text_trap):
            print(sun, end="")
            self.assertEqual( text_trap.getvalue(), "Sun in Milky Way")

        self.assertEqual(repr(sun), "Sun in Milky Way" )

        # from math import exp
        # ex = 1
        # while True:
        #     text_trap = StringIO()
        #     with redirect_stdout(text_trap):
        #         print(exp(ex))
        #         print(text_trap.getvalue())
        #         ex *= 2

    def testInheritance(self):
        class Vehicle:
            pass

        class LandVehicle(Vehicle):
            pass


        class TrackedVehicle(LandVehicle):
            class Vehicle:
                pass

        # for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
        #     for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        #         print(issubclass(cls1, cls2), end="\t")
        #     print()

        # For issubclass: There is one important observation to make: each class is considered to be a subclass of itself.
        self.assertTrue(issubclass(Vehicle, Vehicle), "".format("{}:{} is a subclass", (Vehicle, Vehicle)))
        self.assertFalse(issubclass(Vehicle, LandVehicle), "".format("{}:{} is a NOT subclass", (Vehicle, LandVehicle)))
        self.assertFalse(issubclass(Vehicle, TrackedVehicle), "".format("{}:{} is NOT a subclass", (Vehicle, TrackedVehicle)))
        self.assertTrue(issubclass(LandVehicle, Vehicle), "".format("{}:{} is a subclass", (LandVehicle, Vehicle)))
        self.assertTrue(issubclass(LandVehicle, LandVehicle), "".format("{}:{} is a subclass", (LandVehicle, LandVehicle)))
        self.assertFalse(issubclass(LandVehicle, TrackedVehicle), "".format("{}:{} is a subclass", (LandVehicle, TrackedVehicle)))
        self.assertTrue(issubclass(TrackedVehicle, Vehicle), "".format("{}:{} is a subclass", (TrackedVehicle, Vehicle)))
        self.assertTrue(issubclass(TrackedVehicle, LandVehicle), "".format("{}:{} is a subclass", (TrackedVehicle, LandVehicle)))
        self.assertTrue(issubclass(TrackedVehicle, TrackedVehicle), "".format("{}:{} is a subclass", (TrackedVehicle, TrackedVehicle)))

        class Vehicle:
            pass

        class LandVehicle(Vehicle):
            pass

        class TrackedVehicle(LandVehicle):
            pass

        my_vehicle = Vehicle()
        my_land_vehicle = LandVehicle()
        my_tracked_vehicle = TrackedVehicle()

        # for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
        #     for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        #         print(isinstance(obj, cls), end="\t")
        #     print()

        # Testing is instance
        self.assertTrue(isinstance(my_vehicle, Vehicle), f'{my_vehicle} is an instance of {Vehicle}')
        self.assertFalse(isinstance(my_vehicle, LandVehicle), f'{my_vehicle} is not an instance of {LandVehicle}')
        self.assertFalse(isinstance(my_vehicle, TrackedVehicle), f'{my_vehicle} is not an instance of {TrackedVehicle}')
        self.assertTrue(isinstance(my_land_vehicle, Vehicle), f'{my_land_vehicle} is an instance of {Vehicle}')
        self.assertTrue(isinstance(my_land_vehicle, LandVehicle), f'{my_land_vehicle} is an instance of {LandVehicle}')
        self.assertFalse(isinstance(my_land_vehicle, TrackedVehicle), f'{my_land_vehicle} is not an instance of {TrackedVehicle}')
        self.assertTrue(isinstance(my_tracked_vehicle, Vehicle), f'{my_tracked_vehicle} is an instance of {Vehicle}')
        self.assertTrue(isinstance(my_tracked_vehicle, LandVehicle), f'{my_tracked_vehicle} is an instance of {LandVehicle}')
        self.assertTrue(isinstance(my_tracked_vehicle, TrackedVehicle), f'{my_tracked_vehicle} is an instance of {TrackedVehicle}')


        # Testring is
        class SampleClass:
            def __init__(self, val):
                self.val = val

        object_1 = SampleClass(0)
        object_2 = SampleClass(2)
        object_3 = object_1
        object_3.val += 1

        self.assertFalse(object_1 is object_2, f"Different objects {id(object_1)}: {id(object_1)}")
        self.assertFalse(object_2 is object_3, f"Different objects {id(object_2)}: {id(object_3)}")
        self.assertTrue(object_3 is object_1, f"Same objects {id(object_3)}: {id(object_1)}")

        self.assertTrue(object_1.val == 1, msg = "object_1.val is the same as object_3.val since they are same objects")
        self.assertTrue(object_2.val == 2, msg = "object_2 val is different since it is a differnt object")
        self.assertTrue(object_3.val == 1, msg = "object_1.val is the same as object_3.val since they are same objects")

        string_1 = "Mary had a little "
        string_2 = "Mary had a little lamb"
        string_1 += "lamb"

        self.assertFalse(string_1 is string_2)

        class Super:
            def __init__(self, name):
                self.name = name

            def __str__(self):
                return "My name is " + self.name + "."

        class Sub(Super):
            def __init__(self, name):
                Super.__init__(self, name)  # Calls directly to parent class Super
        obj = Sub("Andy")
        self.assertEqual(self.printToVar(obj), "My name is Andy.", msg="Calls Super to access __init__ of parent class" )


        class Super:
            def __init__(self, name):
                self.name = name

            def __str__(self):
                return "My name is " + self.name + "."
        class Sub(Super):
            def __init__(self, name):
                super().__init__(name)    # Calls to init of parent class

        obj = Sub("Andy")
        self.assertEqual(self.printToVar(obj), "My name is Andy.", msg="Calls parent via super to access __init__ of parent class" )


        # Testing properties: class variables.
        class Super:
            supVar = 1
        class Sub(Super):
            subVar = 2
        obj = Sub()
        self.assertEqual(obj.subVar, 2)
        self.assertEqual(obj.supVar, 1)

        # Testing properties: instance variables.
        class Super:
            supVar = 1
            def __init__(self):
                self.supVar = 11
        class Sub(Super):
            def __init__(self):
                super().__init__()
                self.subVar = 12
        obj = Sub()

        self.assertEqual(obj.subVar, 12)
        self.assertEqual(obj.supVar, 11)
        self.assertEqual(Super.supVar, 1)
        self.assertEqual(obj.__class__.supVar, 1)

        # Three level inheritance
        class Level1:
            variable_1 = 100
            def __init__(self):
                self.var_1 = 101

            def fun_1(self):
                return 102

        class Level2(Level1):
            variable_2 = 200
            def __init__(self):
                super().__init__()
                self.var_2 = 201

            def fun_2(self):
                return 202

        class Level3(Level2):
            variable_3 = 300
            def __init__(self):
                super().__init__()
                self.var_3 = 301

            def fun_3(self):
                return 302

        obj = Level3()

        self.assertEqual(obj.variable_1, 100)
        self.assertEqual(obj.var_1, 101)
        self.assertEqual(obj.fun_1(), 102)

        self.assertEqual(obj.variable_2, 200)
        self.assertEqual(obj.var_2, 201)
        self.assertEqual(obj.fun_2(), 202)

        self.assertEqual(obj.variable_3, 300)
        self.assertEqual(obj.var_3, 301)
        self.assertEqual(obj.fun_3(), 302)
        # print(obj.variable_1, obj.var_1, obj.fun_1())
        # print(obj.variable_2, obj.var_2, obj.fun_2())
        # print(obj.variable_3, obj.var_3, obj.fun_3())


        # Multiple Inheritance
        class SuperA:
            var_a = 10
            def fun_a(self):
                return 11

        class SuperB:
            var_b = 20
            def fun_b(self):
                return 21

        class Sub(SuperA, SuperB):
            pass

        obj = Sub()
        # print(obj.var_a, obj.fun_a())
        # print(obj.var_b, obj.fun_b())

        self.assertEqual(obj.var_a, 10)
        self.assertEqual(obj.fun_a(), 11)
        self.assertEqual(obj.var_b, 20)
        self.assertEqual(obj.fun_b(), 21)


        # Subclasses override properties of parent classes
        class Level1:
            var = 100
            def fun(self):
                return 101
        class Level2(Level1):
            var = 200
            def fun(self):
                return 201
        class Level3(Level2):
            pass
        obj = Level3()

        self.assertEqual(obj.var, 200)
        self.assertEqual(obj.fun(), 201)
        # print(obj.var, obj.fun())

        # For multiple inheritance, subclasses will go from left to right for inheritance tree
        class Left:
            var = "L"
            var_left = "LL"
            def fun(self):
                return "Left"
        class Right:
            var = "R"
            var_right = "RR"
            def fun(self):
                return "Right"
        class Sub(Left, Right):
            pass

        obj = Sub()

        self.assertEqual(obj.var, "L")
        self.assertEqual(obj.var_left, "LL")
        self.assertEqual(obj.var_right, "RR")
        self.assertEqual(obj.fun(), "Left")

        # print(obj.var, obj.var_left, obj.var_right, obj.fun())

        # Polymorphism , doanything called from object of class Two will result in
        class One:
            def do_it(self):
                print("do_it from One")

            def doanything(self):
                self.do_it()


        class Two(One):
            def do_it(self):
                print("do_it from Two")


        one = One()
        two = Two()

        text_trap = StringIO()
        with redirect_stdout(text_trap):
            one.doanything()
            result = text_trap.getvalue()
            self.assertEqual(result, "do_it from One\n")

        text_trap.truncate(0)
        text_trap.seek(0)
        # text_trap.flush()
        text_trap = StringIO()
        with redirect_stdout(text_trap):
            two.doanything()
            result = text_trap.getvalue()
            self.assertEqual(result, "do_it from Two\n")

    def testInheritanceVehiclesExample(self):
        pass
        import time

        # Creating vehicle using inheritance
        class Vehicle:
            def change_direction(self, on):
                pass
            def turn(self):
                change_direction(self, True)
                time.sleep(0.25)
                change_direction(self, False)

        class TrackedVehicle(Vehicle):
            def control_track(self, stop):
                pass
            def change_direction(self, on):
                control_track(self, on)

        class WheeledVehicle(Vehicle):
            def turn_front_wheels(self, on):
                 pass

            def change_direction(self, on):
                turn_front_wheels(self, on)


        # Creating a vehicle using composition
        import time

        class Tracks:
            def change_direction(self, left, on):
                print("tracks: ", left, on)

        class Wheels:
            def change_direction(self, left, on):
                print("wheels: ", left, on)

        class Vehicle:
            def __init__(self, controller):
                self.controller = controller

            def turn(self, left):
                self.controller.change_direction(left, True)
                time.sleep(0.00025)
                self.controller.change_direction(left, False)


        wheeled = Vehicle(Wheels())
        tracked = Vehicle(Tracks())


        self.printFunction(wheeled.turn, True)
        self.assertEqual(self.printFunction(wheeled.turn, True), "wheels:  True True\nwheels:  True False\n")
        self.assertEqual(self.printFunction(tracked.turn, False),"tracks:  False True\ntracks:  False False\n")

        # wheeled.turn(True)
        # tracked.turn(False)
        # Prints out
        # tracks:  False False")
        # ...wheels:  True True
        # wheels:  True False
        # tracks:  False True
        # tracks:  False False


        # 3.5.1.20 OOP Fundamentals: MRO
        class Top:
            def m_top(self):
                print("top")
                return "top"

        class Middle(Top):
            def m_middle(self):
                print("middle")
                return "middle"

       # with self.assertRaises(TypeError, "Will raise an assert due to MRO Top can not come before Bottom"):
        # class Bottom(Top, Middle):
        #     def m_bottom(self):
        #         print("bottom")

        class Bottom(Middle, Top ):
            def m_bottom(self):
                print("bottom")
                return "bottom"

        object = Bottom()

        self.assertEqual(self.printFunction(object.m_bottom), "bottom\n")
        self.assertEqual(self.printFunction(object.m_middle), "middle\n", msg="Resolution order from class inheritance is Bottom, Middle__left, Top, Middle_Right")
        self.assertEqual(self.printFunction(object.m_top), "top\n")


        # 3.5.1.21 OOP Fundamentals: MRO
        # Diamond prob lem
        class Top:
            def m_top(self):
                print("top")
            def m_middle(self):
                print("Printing middle from Top")

        class Middle_Left(Top):
            def m_middle(self):
                print("middle_left")

        class Middle_Right(Top):
            def m_middle(self):
                print("middle_right")


        class Bottom(Middle_Left, Middle_Right):
            def m_bottom(self):
                print("bottom")


        object = Bottom()
        self.assertEqual(self.printFunction(object.m_bottom), "bottom\n")
        self.assertEqual(self.printFunction(object.m_middle), "middle_left\n", msg="Resolution order from class inheritance is Bottom, Middle__left, Top, Middle_Right")
        self.assertEqual(self.printFunction(object.m_top), "top\n")

        # object.m_middle()
        middleLeftObject = Middle_Left()
        middleRightObject = Middle_Right()
        TopObject = Top()

        # Adding m_middle to Top class only gets called if you call explicitlu since inherited classes have overridden behavior
        self.assertEqual(self.printFunction(TopObject.m_middle), "Printing middle from Top\n")
        self.assertEqual(self.printFunction(middleLeftObject.m_middle), "middle_left\n")
        self.assertEqual(self.printFunction(middleRightObject.m_middle), "middle_right\n")

    #      3.6.1.1 Exceptions once again
    def testExceptions(self):
        def reciprocal(n) -> float:
            try:
                n = 1 / n
            except ZeroDivisionError:
                print("Division failed.")
                return "Division failed."
            else:
                print("Everything went fine.")
                return n
            finally:
                print("It's time to say goodbye")
                return n

        self.assertEqual(self.printFunction(reciprocal, 2), "Everything went fine.\nIt's time to say goodbye\n", "Printed output should call the else and fninally ")
        self.assertEqual(self.printFunction(reciprocal, 0), "Division failed.\nIt's time to say goodbye\n")

        # try:
        #     i = int("Hello!")
        # except Exception as e:
        #     print(e)
        #     print(e.__str__())

        with self.assertRaises(ValueError):
            self.printFunction(int, "Hello")

        # import math
        # print(math.pow(2, 3))

        # try:
        #     (math.pow(2))
        # except TypeError:
        #     print("Not able to execute math.pow()")
        # else:
        #     print("Here")
        # finally:
        #     print("Will always execute")

        

if __name__ == "__main__":
    
    unittest.main()