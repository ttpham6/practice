import unittest



class DifferentExceptions(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    """_summary_
    Bases exceptions won't be directly invoked
    They are exctende by other exceptions
    
    """
    def testBaseExceptions(self):
        
        with self.assertRaises(BaseException, msg="The base class of all exceptions"):
            raise BaseException
        
        with self.assertRaises(Exception, msg="Used for extending exceptions"):
            raise Exception

        with self.assertRaises(Exception, msg="Used for extending exceptions"):
            raise Exception

        with self.assertRaises(AssertionError, msg="Base class "):
            assert False


    def testMathExceptions(self):
        with self.assertRaises(ArithmeticError, msg= "Math exceptions are derived from this base class"):
            raise ArithmeticError
        
        self.assertFalse("A" > "a", "A is ord x41  a is ord x61")
        self.assertTrue(1.0 == 1, "Same value")
        self.assertFalse("1" == 1, "String == or != is always false")
        self.assertFalse(True == "1", "Returns false")
        self.assertTrue(True == 1, "Numeric comparison against 1 returns True")
        self.assertFalse(True == 0, "Numeric comparison against 0 returns False")
        self.assertTrue(True == 1.0, "Numeric comparison against 1.0 returns true")
        self.assertEqual("1" + "1", "11", "String addition adds appends two strings together")
        self.assertEqual(1 + 1, 2, "Basic addition" )
        
        with self.assertRaises(TypeError, msg="TypeError: unsupported operand type(s) for +: 'int' and 'str'"):        
            result = 1 + "1"


    def testTabException(self):
        # You can not mix tabs and spaces
        # PEP requires spaces in place of tabs
        # 4 spaces per indentation
        # Tabs are allowed for backwards compatiblity
        with self.assertRaises(TabError):
            # Mixes tab and spaces here
		    pass


if __name__ == "__main__":
    unittest.main()
    
    
    
    
    """
    BaseException
   +---BaseExceptionGroup
   |   +---ExceptionGroup
   +---Exception
   |   +---ArithmeticError
   |   |   +---FloatingPointError
   |   |   +---OverflowError
   |   |   +---ZeroDivisionError
   |   |   |   +---DivisionByZero
   |   |   |   +---DivisionUndefined
   |   |   +---DecimalException
   |   |   |   +---Clamped
   |   |   |   +---Rounded
   |   |   |   |   +---Underflow
   |   |   |   |   +---Overflow
   |   |   |   +---Inexact
   |   |   |   |   +---Underflow
   |   |   |   |   +---Overflow
   |   |   |   +---Subnormal
   |   |   |   |   +---Underflow
   |   |   |   +---DivisionByZero
   |   |   |   +---FloatOperation
   |   |   |   +---InvalidOperation
   |   |   |   |   +---ConversionSyntax
   |   |   |   |   +---DivisionImpossible
   |   |   |   |   +---DivisionUndefined
   |   |   |   |   +---InvalidContext
   |   +---AssertionError
   |   +---AttributeError
   |   +---BufferError
   |   +---EOFError
   |   +---ImportError
   |   |   +---ModuleNotFoundError
   |   |   |   +---PackageNotFoundError
   |   |   +---ZipImportError
   |   +---LookupError
   |   |   +---IndexError
   |   |   +---KeyError
   |   |   +---CodecRegistryError
   |   +---MemoryError
   |   +---NameError
   |   |   +---UnboundLocalError
   |   +---OSError
   |   |   +---BlockingIOError
   |   |   +---ChildProcessError
   |   |   +---ConnectionError
   |   |   |   +---BrokenPipeError
   |   |   |   +---ConnectionAbortedError
   |   |   |   +---ConnectionRefusedError
   |   |   |   +---ConnectionResetError
   |   |   |   |   +---RemoteDisconnected
   |   |   +---FileExistsError
   |   |   +---FileNotFoundError
   |   |   +---InterruptedError
   |   |   +---IsADirectoryError
   |   |   +---NotADirectoryError
   |   |   +---PermissionError
   |   |   +---ProcessLookupError
   |   |   +---TimeoutError
   |   |   +---UnsupportedOperation
   |   |   +---herror
   |   |   +---gaierror
   |   |   +---SSLError
   |   |   |   +---SSLCertVerificationError
   |   |   |   +---SSLZeroReturnError
   |   |   |   +---SSLWantWriteError
   |   |   |   +---SSLWantReadError
   |   |   |   +---SSLSyscallError
   |   |   |   +---SSLEOFError
   |   |   +---BadGzipFile
   |   |   +---Error
   |   |   |   +---SameFileError
   |   |   +---SpecialFileError
   |   |   +---ExecError
   |   |   +---ReadError
   |   +---ReferenceError
   |   +---RuntimeError
   |   |   +---NotImplementedError
   |   |   +---RecursionError
   |   |   +---_DeadlockError
   |   |   +---BrokenBarrierError
   |   |   +---VariableError
   |   +---StopAsyncIteration
   |   +---StopIteration
   |   +---SyntaxError
   |   |   +---IndentationError
   |   |   |   +---TabError
   |   +---SystemError
   |   |   +---CodecRegistryError
   |   +---TypeError
   |   |   +---FloatOperation
   |   |   +---MultipartConversionError
   |   +---ValueError
   |   |   +---UnicodeError
   |   |   |   +---UnicodeDecodeError
   |   |   |   +---UnicodeEncodeError
   |   |   |   +---UnicodeTranslateError
   |   |   +---UnsupportedOperation
   |   |   +---JSONDecodeError
   |   |   +---Error
   |   |   +---MessageDefect
   |   |   |   +---NoBoundaryInMultipartDefect
   |   |   |   +---StartBoundaryNotFoundDefect
   |   |   |   +---CloseBoundaryNotFoundDefect
   |   |   |   +---FirstHeaderLineIsContinuationDefect
   |   |   |   +---MisplacedEnvelopeHeaderDefect
   |   |   |   +---MissingHeaderBodySeparatorDefect
   |   |   |   +---MultipartInvariantViolationDefect
   |   |   |   +---InvalidMultipartContentTransferEncodingDefect
   |   |   |   +---UndecodableBytesDefect
   |   |   |   +---InvalidBase64PaddingDefect
   |   |   |   +---InvalidBase64CharactersDefect
   |   |   |   +---InvalidBase64LengthDefect
   |   |   |   +---HeaderDefect
   |   |   |   |   +---InvalidHeaderDefect
   |   |   |   |   +---HeaderMissingRequiredValue
   |   |   |   |   +---NonPrintableDefect
   |   |   |   |   +---ObsoleteHeaderDefect
   |   |   |   |   +---NonASCIILocalPartDefect
   |   |   |   |   +---InvalidDateDefect
   |   |   +---UnsupportedDigestmodError
   |   |   +---AddressValueError
   |   |   +---NetmaskValueError
   |   |   +---IllegalMonthError
   |   |   +---IllegalWeekdayError
   |   |   +---SSLCertVerificationError
   |   +---Warning
   |   |   +---BytesWarning
   |   |   +---DeprecationWarning
   |   |   +---EncodingWarning
   |   |   +---FutureWarning
   |   |   +---ImportWarning
   |   |   +---PendingDeprecationWarning
   |   |   +---ResourceWarning
   |   |   +---RuntimeWarning
   |   |   +---SyntaxWarning
   |   |   +---UnicodeWarning
   |   |   +---UserWarning
   |   |   |   +---GetPassWarning
   |   +---ExceptionGroup
   |   +---_OptionError
   |   +---_Error
   |   +---error
   |   +---error
   |   +---DebuggerInitializationError
   |   +---_GiveupOnSendfile
   |   +---TokenError
   |   +---StopTokenizing
   |   +---Empty
   |   +---Full
   |   +---Incomplete
   |   +---MessageError
   |   |   +---MessageParseError
   |   |   |   +---HeaderParseError
   |   |   |   +---BoundaryError
   |   |   +---MultipartConversionError
   |   |   +---CharsetError
   |   +---Error
   |   +---HTTPException
   |   |   +---NotConnected
   |   |   +---InvalidURL
   |   |   +---UnknownProtocol
   |   |   +---UnknownTransferEncoding
   |   |   +---UnimplementedFileMode
   |   |   +---IncompleteRead
   |   |   +---ImproperConnectionState
   |   |   |   +---CannotSendRequest
   |   |   |   +---CannotSendHeader
   |   |   |   +---ResponseNotReady
   |   |   +---BadStatusLine
   |   |   |   +---RemoteDisconnected
   |   |   +---LineTooLong
   |   +---ExpatError
   |   +---error
   |   +---Error
   |   |   +---ProtocolError
   |   |   +---ResponseError
   |   |   +---Fault
   |   +---Error
   |   +---LZMAError
   |   +---RegistryError
   |   +---_GiveupOnFastCopy
   |   +---ClassFoundException
   |   +---EndOfBlock
   |   +---ErrorDuringImport
   |   +---ArgumentError
   |   +---COMError
   |   +---_Error
   |   +---PickleError
   |   |   +---PicklingError
   |   |   +---UnpicklingError
   |   +---_Stop
   |   +---UnableToResolveVariableException
   |   +---InvalidTypeInArgsException
   |   +---SubprocessError
   |   |   +---CalledProcessError
   |   |   +---TimeoutExpired
   |   +---Error
   |   +---BadZipFile
   |   +---LargeZipFile
   |   +---TraversalError
   |   +---ArgumentError
   |   +---ArgumentTypeError
   +---GeneratorExit
   +---KeyboardInterrupt
   +---SystemExit

    Returns:
        _type_: _description_
    """