#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2006 - 2010 Loic Dachary <loic@dachary.org>
# Copyright (C) 2006 Mekensleep
#
# Mekensleep
# 26 rue des rosiers
# 75004 Paris
#       licensing@mekensleep.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301, USA.
#
# Authors:
#  Pierre-Andre (05/2006)
#  Loic Dachary <loic@dachary.org>
#

import unittest, sys
from os import path

TESTS_PATH = path.dirname(path.realpath(__file__))
sys.path.insert(0, path.join(TESTS_PATH, ".."))

import os.path
import types

from pokerengine import pokerchips

class PokerChipsTestCase(unittest.TestCase):
        
    # -----------------------------------------------------------------------------------------------------
    def setUp(self):
        pass
    
    # -----------------------------------------------------------------------------------------------------    
    def tearDown(self):
        pass
        
    # -----------------------------------------------------------------------------------------------------    
    def testInit(self):
        """Test Poker Chips : Initialisation"""
        
        values = [5, 10, 20]
        pokerchip = pokerchips.PokerChips(values)
        
        self.failUnlessEqual(pokerchip, pokerchips.PokerChips(values, 0))
        self.failUnlessEqual(pokerchip.toint(), 0)
        
        pokerchip1 = pokerchips.PokerChips(values, 153)
        pokerchip2 = pokerchips.PokerChips(values, pokerchip1)
        
        self.failUnlessEqual(pokerchip1, pokerchip2)
        self.failUnlessEqual(pokerchip2.toint(), 153)
        
        pokerchip1 = pokerchips.PokerChips(values, [10, 5, 1])
        self.failUnlessEqual(pokerchip1.toint(), 120)
        
    # -----------------------------------------------------------------------------------------------------    
    def testOperatorEqu(self):
        """Test Poker Chips : Equality"""
        
        values = [5, 10, 20]
        pokerchip1 = pokerchips.PokerChips(values, 153)
        pokerchip2 = pokerchips.PokerChips(values, 153)
        pokerchip3 = pokerchips.PokerChips(values, 154)
        
        self.failUnlessEqual(pokerchip1, pokerchip2)
        self.failIfEqual(pokerchip1, pokerchip3)
        
        self.failUnlessEqual(pokerchip1 != pokerchip2, False)
        self.failUnlessEqual(pokerchip1 != pokerchip3, True)
        self.failUnlessEqual(pokerchip1 != 153, True)
        
    # -----------------------------------------------------------------------------------------------------    
    def testToInt(self):
        """Test Poker Chips : To integer"""
        
        values = [5, 10, 20]
        pokerchip = pokerchips.PokerChips(values)
        self.failUnlessEqual(pokerchip.toint(), 0)
        
        pokerchip = pokerchips.PokerChips(values, 153)
        self.failUnlessEqual(pokerchip.toint(), 153)
        
        pokerchip = pokerchips.PokerChips(values, [1, 1, 1])
        self.failUnlessEqual(pokerchip.toint(), 35)
        
    # -----------------------------------------------------------------------------------------------------    
    def testAdd(self):
        """Test Poker Chips : Addition"""
        
        values = [5, 10, 20]
        pokerchip1 = pokerchips.PokerChips(values, 155)
        pokerchip2 = pokerchips.PokerChips(values, 223)
        
        pokerchip1.add(pokerchip2)
        self.failUnlessEqual(pokerchip1.toint(), 155 + 223)
        
    # -----------------------------------------------------------------------------------------------------    
    def testSub(self):
        """Test Poker Chips : Substraction"""
        
        values = [5, 10, 20]
        pokerchip1 = pokerchips.PokerChips(values, [3, 2, 1])
        pokerchip2 = pokerchips.PokerChips(values, [1, 1, 1])
        
        pokerchip1.subtract(pokerchip2)
        self.failUnlessEqual(pokerchip1, pokerchips.PokerChips(values, [2, 1, 0]))
        
        pokerchip1 = pokerchips.PokerChips(values, 155)
        pokerchip1.subtract(130)
        self.failUnlessEqual(pokerchip1.toint(), 25)
        
        pokerchip1 = pokerchips.PokerChips(values, 155)
        pokerchip1.subtract(160)
        self.failUnlessEqual(pokerchip1.toint(), 0)
        
    # -----------------------------------------------------------------------------------------------------    
    def testToString(self):
        """Test Poker Chips : String representation"""
        
        self.failUnlessEqual(pokerchips.PokerChips.tostring(0), '0')
        self.failUnlessEqual(pokerchips.PokerChips.tostring(1), '1')
        
    # -----------------------------------------------------------------------------------------------------    
    def testInt2Chips(self):
        """Test Poker Chips : From integer"""
        
        values = [5, 10, 20]
        self.failUnlessEqual(pokerchips.PokerChips.int2chips([], pokerchips.INT2CHIPS_FACTOR, 15), ([], 15))
        self.failUnlessEqual(pokerchips.PokerChips.int2chips(values, pokerchips.INT2CHIPS_FACTOR, 0), ([0, 0, 0], 0))
        self.failUnlessEqual(pokerchips.PokerChips.int2chips(values, pokerchips.INT2CHIPS_FACTOR, 5), ([1, 0, 0], 0))
        self.failUnlessEqual(pokerchips.PokerChips.int2chips(values, pokerchips.INT2CHIPS_FACTOR, 7), ([1, 0, 0], 2))
        self.failUnlessEqual(pokerchips.PokerChips.int2chips(values, pokerchips.INT2CHIPS_FACTOR, 15), ([3, 0, 0], 0))
        self.failUnlessEqual(pokerchips.PokerChips.int2chips(values, pokerchips.INT2CHIPS_FACTOR, 50), ([8, 1, 0], 0))
        self.failUnlessEqual(pokerchips.PokerChips.int2chips(values, pokerchips.INT2CHIPS_FACTOR, 90), ([8, 3, 1], 0))
        self.failUnlessEqual(pokerchips.PokerChips.int2chips(values, pokerchips.INT2CHIPS_FACTOR, 93), ([6, 4, 1], 3))
        
    # -----------------------------------------------------------------------------------------------------    
    def testToList(self):
        """Test Poker Chips : To list"""
        
        values = [5, 10, 20]
        self.failUnlessEqual(pokerchips.PokerChips(values, 0).tolist(), [])
        self.failUnlessEqual(pokerchips.PokerChips(values, 3).tolist(), [1,3])
        self.failUnlessEqual(pokerchips.PokerChips(values, 5).tolist(), [5, 1])
        self.failUnlessEqual(pokerchips.PokerChips(values, 7).tolist(), [1, 2 ,5, 1])
        self.failUnlessEqual(pokerchips.PokerChips(values, 15).tolist(), [5, 3])
        self.failUnlessEqual(pokerchips.PokerChips(values, 50).tolist(), [5, 8, 10, 1])
        self.failUnlessEqual(pokerchips.PokerChips(values, 90).tolist(), [5, 8, 10, 3, 20, 1])
        self.failUnlessEqual(pokerchips.PokerChips(values, 93).tolist(), [1, 3, 5, 6, 10, 4, 20, 1])
        
        values = [1, 2, 4]
        self.failUnlessEqual(pokerchips.PokerChips(values, 7).tolist(), [1, 7])
        
    # -----------------------------------------------------------------------------------------------------    
    def testlimitChips(self):
        """Test Poker Chips : Limit chips"""
        
        values = [5, 10, 20]
        chips = pokerchips.PokerChips(values, [pokerchips.MAX_CHIPS_PER_STACK + 2, 0, 0])
        self.failUnlessEqual(chips.tolist(),  [5, pokerchips.MAX_CHIPS_PER_STACK, 10, 1])
        chips = pokerchips.PokerChips(values, [pokerchips.MAX_CHIPS_PER_STACK + 3, 0, 0])
        self.failUnlessEqual(chips.tolist(),  [5, pokerchips.MAX_CHIPS_PER_STACK + 1, 10, 1])
        chips = pokerchips.PokerChips(values, [pokerchips.MAX_CHIPS_PER_STACK + 4, pokerchips.MAX_CHIPS_PER_STACK, pokerchips.MAX_CHIPS_PER_STACK])
        self.failUnlessEqual(chips.tolist(),  [5, pokerchips.MAX_CHIPS_PER_STACK, 10, pokerchips.MAX_CHIPS_PER_STACK, 20, pokerchips.MAX_CHIPS_PER_STACK +1])
        
    # -----------------------------------------------------------------------------------------------------    
    def testStrOperator(self):
        """Test Poker Chips : String representation"""
        
        values = [5, 10, 20]
        pokerchip = pokerchips.PokerChips(values, 93)
        self.failUnlessEqual(str(pokerchip), 'PokerChips(%s) = %d (-%d)' %([6, 4, 1], 93, 3))
    
    # -----------------------------------------------------------------------------------------------------    
    def testReprOperator(self):
        """Test Poker Chips : Representation"""
        
        values = [5, 10, 20]
        pokerchip = pokerchips.PokerChips(values, 93)
        self.failUnlessEqual(repr(pokerchip), '%s(%s)' %('PokerChips', [6, 4, 1]))
        
    # -----------------------------------------------------------------------------------------------------    
    def testCopy(self):
        """Test Poker Chips : Copy"""
        values = [5, 10, 20]
        
        pokerchip1 = pokerchips.PokerChips(values, 93)
        pokerchip2 = pokerchip1.copy()
        self.failUnlessEqual(pokerchip1, pokerchip2)
        self.failUnlessEqual(pokerchip2.toint(), 93)
        
        pokerchip1.add(7)
        self.failIfEqual(pokerchip1, pokerchip2)
        self.failUnlessEqual(pokerchip1.toint(), 100)
        self.failUnlessEqual(pokerchip2.toint(), 93)
        
# -----------------------------------------------------------------------------------------------------
def GetTestSuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(PokerChipsTestCase))
    # Comment out above and use line below this when you wish to run just
    # one test by itself (changing prefix as needed).
#    suite.addTest(unittest.makeSuite(PokerChipsTestCase, prefix = "test2"))
    return suite
    
# -----------------------------------------------------------------------------------------------------
def GetTestedModule():
    return pokerchips
  
# -----------------------------------------------------------------------------------------------------
def run():
    return unittest.TextTestRunner().run(GetTestSuite())
    
# -----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    if run().wasSuccessful():
        sys.exit(0)
    else:
        sys.exit(1)

# Interpreted by emacs
# Local Variables:
# compile-command: "( cd .. ; ./config.status tests/test-pokerchips.py ) ; ( cd ../tests ; make COVERAGE_FILES='../pokerengine/pokerchips.py' TESTS='coverage-reset test-pokerchips.py coverage-report' check )"
# End:
