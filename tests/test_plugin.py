from ase.visualize import view
from ase.build import bulk


def test_plugin():
    cu = bulk('Cu')
    view(cu, viewer="paraview")