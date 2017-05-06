#!/usr/bin/env python

import unittest

class TestPyCal( unittest.TestCase ):
	def setUp( self ):
		pass
	def tearDown( self ):
		pass
	def test_1( self ):
		pass


def suite():
    suite = unittest.TestSuite()
    suite.addTests( unittest.makeSuite( TestPyCal ) )
    return suite


if __name__=="__main__":
    unittest.main()