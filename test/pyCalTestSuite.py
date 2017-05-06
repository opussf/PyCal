#!/usr/bin/env python
import unittest
#import xmlrunner
from pyCalTests import *
#from TestSolveSudoku import *
#from TestSudokuboard import *
#from TestSudokuFiles import *
#from TestMakeRandomSudoku import *

suite = unittest.TestSuite()
suite.addTests( unittest.makeSuite( TestPyCal ) )
#suite.addTests( unittest.makeSuite( TestSolveSudoku ) )
#suite.addTests( unittest.makeSuite( TestSudokuFiles ) )
#suite.addTests( unittest.makeSuite( TestMakeRandomSudoku ) )

if __name__=="__main__":
	unittest.main()
