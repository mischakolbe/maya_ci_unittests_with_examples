"""Example unittests.

Note:
    Visit unittest documentation page for all assert options:
    https://docs.python.org/2.7/library/unittest.html#module-unittest
"""
from maya import cmds

from base import MayaBaseTestCase

import example_code


class TestMakeTransform(MayaBaseTestCase):
    def setUp(self):
        """Run BEFORE every test_* method.
        
        Notes:
            There is a "tearDown" method as well, which runs AFTER every test.
        """
        super(TestMakeTransform, self).setUp()

        self.transform = example_code.make_transform(name="TestTransform")

    def test_node_name(self):
        """Test whether returned name is correct."""
        self.assertEqual(self.transform, "TestTransform")

    def test_node_exists(self):
        """Test whether node was actually created."""
        transform_exists = cmds.objExists(self.transform)
        self.assertTrue(transform_exists)

    def test_visibility_data_type(self):
        """Test whether visibility attribute of node is a boolean."""
        visibility = cmds.getAttr(self.transform + ".visibility")
        self.assertIs(type(visibility), bool)

    def test_has_roughly_correct_scale(self):
        """Test whether node is roughly at the right scale."""
        transform_scale = cmds.getAttr(self.transform + ".sx")
        self.assertAlmostEqual(transform_scale, 1.00000001, places=7)

    def test_movement(self):
        """Test whether node can move."""
        target_pos = [1, 2, 3.45]
        cmds.xform(self.transform, translation=target_pos, worldSpace=True)
        actual_pos = cmds.xform(
            self.transform, query=True, translation=True, worldSpace=True
        )
        self.assertListEqual(actual_pos, target_pos)

    def test_for_strange_attribute(self):
        """Test for an expected Error."""
        with self.assertRaises(ValueError):
            cmds.getAttr(self.transform + ".whyWouldItHaveThisAttribute")
