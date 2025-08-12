 # https://www.bigocheatsheet.com/
 
 # https://www.bigocheatsheet.com/
 # https://wiki.python.org/moin/TimeComplexity
 
 # https://www.pythonmorsels.com/time-complexities/
 
# https://nedbatchelder.com/text/bigo.html
 
 
 
 # https://inventwithpython.com/beyond/chapter13.html
    
 # https://www.geeksforgeeks.org/python/timeit-python-examples/
 
import timeit


def timeExamples():
    # Example 1: O(1) - Constant Time
    def constant_time_example():
        return 42

    # Example 2: O(n) - Linear Time
    def linear_time_example(n):
        return sum(range(n))

    # Example 3: O(n^2) - Quadratic Time
    def quadratic_time_example(n):
        return sum(i * j for i in range(n) for j in range(n))

    # Timing the examples
    print("Timing constant time example:")
    print(timeit.timeit(constant_time_example, number=1000000))

    print("Timing linear time example with n=1000:")
    print(timeit.timeit(lambda: linear_time_example(1000), number=1000))

    print("Timing quadratic time example with n=1000:")
    print(timeit.timeit(lambda: quadratic_time_example(1000), number=10))
    
    
def memoryMeasurementExamples():
    # Example 1: O(1) - Constant Space
    def constant_space_example():
        return [1, 2, 3]

    # Example 2: O(n) - Linear Space
    def linear_space_example(n):
        return list(range(n))

    # Example 3: O(n^2) - Quadratic Space
    def quadratic_space_example(n):
        return [[i * j for j in range(n)] for i in range(n)]

    print("Memory usage of constant space example:")
    print(constant_space_example())

    print("Memory usage of linear space example with n=1000:")
    print(linear_space_example(1000))

    print("Memory usage of quadratic space example with n=1000:")
    print(quadratic_space_example(1000))
    
    
    



if __name__ == "__main__":
    timeExamples()