"""Example module."""
from maya import cmds


def make_transform(name="test"):
    """Create a named transform.. Exciting!

    Args:
        name (str): Name for the transform to be created.

    Returns:
        str: Name of the created transform
    """
    transform = cmds.createNode("transform", name=name)

    return transform

