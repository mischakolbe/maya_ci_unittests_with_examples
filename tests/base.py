"""Unittest base class."""
import os
import sys

from unittest import TestCase

# Add script base path to system paths.
tests_path = os.path.dirname(os.path.realpath(__file__))
base_path = tests_path.rsplit(os.sep, 1)[0]
if base_path not in sys.path:
    sys.path.insert(0, base_path)

# Wait for Maya - otherwise tests might be run before Maya is actually loaded!
import maya.standalone
maya.standalone.initialize()

from maya import cmds


class MayaBaseTestCase(TestCase):
    """Base class for all Maya unittests."""
    @classmethod
    def setUpClass(self):
        """Run for every Test-Class, before any method is executed."""
        cmds.file(new=True, force=True)

    def tearDown(self):
        """Run after every Test-Class method."""
        cmds.file(new=True, force=True)
