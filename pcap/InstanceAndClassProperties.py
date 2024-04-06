class ExampleClass1:
        def __init__(self, val = 1):
            self.__first = val

        def set_second(self, val = 2):
            self.__second = val


if __name__ == "__main__":
    example_object_1 = ExampleClass1()
    example_object_2 = ExampleClass1(2)

    example_object_2.set_second(3)

    example_object_3 = ExampleClass1(4)
    example_object_3.__third = 5

    # {'_ExampleClass1__first': 1}
    # {'_ExampleClass1__first': 2, '_ExampleClass1__second': 3}
    # {'_ExampleClass1__first': 4, '_TestSecton3__third': 5}

    # Name mangling for double underscore properties. Adds class name
    # self.assertDictEqual(example_object_1.__dict__, {"_ExampleClass1__first": 1}, "Name managed added underscore and class name.")
    # self.assertDictEqual(example_object_2.__dict__, {"_ExampleClass1__first": 2, "_ExampleClass1__second": 3},  "Name managed added underscore and class name.")
    # # revisit: tampham: Why is this different
    # self.assertDictEqual(example_object_3.__dict__, {"_ExampleClass1__first": 4, "_TestSecton3__third": 5}, "Turtorial 3.3.1.2 says tis should be __third:5. ")



    print(example_object_1.__dict__)
    print(example_object_2.__dict__)
    print(example_object_3.__dict__)
            
