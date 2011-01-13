import unittest
import doctest
#import zope.testing
from zope.component.testing import setUp, tearDown, PlacelessSetup
from zope.configuration.xmlconfig import XMLConfig

import quotationtool.site


class SiteTests(PlacelessSetup, unittest.TestCase):
    
    def testConfiguration(self):
        XMLConfig('configure.zcml', quotationtool.site)()
        
        

def test_suite():
    return unittest.TestSuite((
            unittest.makeSuite(SiteTests),
            ))

