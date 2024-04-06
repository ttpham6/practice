import argparse
from io import StringIO
from inspect import isclass
from contextlib import redirect_stdout

def printToVar(obj) -> str: 
    text_trap = StringIO()
    with redirect_stdout(text_trap):
        print(obj, end="")
        return text_trap.getvalue()


def printFunction(*args) -> str:
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


#     """_summary_: Print class Tree 
#     """
# def print_exception_tree(thisclass, nest = 0):
#     if nest > 1:
#         print("   |" * (nest - 1), end="")
#     if nest > 0:
#         print("   +---", end="")

#     print(thisclass.__name__)

#     for subclass in thisclass.__subclasses__():
#         print_exception_tree(subclass, nest + 1)

def showIntsSameClassID():
    start = -5
    end = 256
    inc = start
    for x in range(start, end):
        try:
            assert x == inc
            assert id(x) == id(inc)
            # inc += 1
        except AssertionError:
            print(f"{x}: {inc}")
            print(f"{id(x)}: {id(inc)}")
        # else:
        #     print("Calling else")
        #     inc += 1
        finally:
            inc += 1  


class LanguageInfo():
    def __init__(self) -> None:
        pass
    
    @classmethod
    def printClassTree(cls, thisclass, nest = 0):
        if not isclass(thisclass):
            raise TypeError("Not a class")
        
        if nest > 1:
            print("   |" * (nest - 1), end="")
        if nest > 0:
            print("   +---", end="")

        print(thisclass.__name__)

        for subclass in thisclass.__subclasses__():
            cls.printClassTree(subclass, nest + 1)
        
    @classmethod
    def asciiTable(cls, width = 4 ):
        print("Numbers 0-9 are 48-57")
        print("A-Z are 65-90")
        print("a-z are 97-102")
        print(f"The differene between upper and lower is {ord('a')-ord('A')}")
        
        
        for val in range(256):
            if val % width  == 0: print()

            if val == 0:
                print(f'{val:<3}:{hex(val):<4}:{'NU':2}', end="\t")
            elif val == 8:
                print(f'{val:<3}:{hex(val):<4}:{'\\b':2}', end="\t")   
            elif val == 9:
                print(f'{val:<3}:{hex(val):<4}:{'HT':2}', end="\t")   
            elif val == 10:
                print(f'{val:<3}:{hex(val):<4}:{'\\n':2}', end="\t")
                # print(f'{val:<3}:{hex(val):<4}:{'LF':2}', end="\t")   
            elif val == 11:
                print(f'{val:<3}:{hex(val):<4}:{'VT':2}', end="\t")   
            elif val == 12:
                print(f'{val:<3}:{hex(val):<4}:{'\\f':2}', end="\t")   
            elif val == 13:
                print(f'{val:<3}:{hex(val):<4}:{'\\r':2}', end="\t")   
                # print(f'{val:<3}:{hex(val):<4}:{'CR':2}', end="\t")   
            elif val == 14:
                print(f'{val:<3}:{hex(val):<4}:{'SI':2}', end="\t")
            elif val == 15:
                print(f'{val:<3}:{hex(val):<4}:{'SO':2}', end="\t")   
            elif val == 27:
                print(f'{val:<3}:{hex(val):<4}:{'ESC':2}', end="\t")   
            elif val == 32:
                print(f'{val:<3}:{hex(val):<4}:{'SPC':2}', end="\t")   
            else:
                print(f'{val:<3}:{hex(val):<4}:{chr(val):2}', end="\t")
    
    

    
    
if __name__ == "__main__":
    # LanguageInfo.printClassTree(BaseException)
    LanguageInfo.asciiTable()
#     showIntsSameClassID()