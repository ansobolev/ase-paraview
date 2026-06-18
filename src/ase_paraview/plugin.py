import sys

from ase._4.plugins.viewer import ViewerPlugin

THIS_MODULE = sys.modules[__name__]

paraview_plugin = ViewerPlugin(
    name="paraview-plugin",
    citation="Andrei Sobolev and the ASE Developers",
    module=THIS_MODULE,
    implementation="ase_paraview.plugin.ParaviewPlugin"
)


class ParaviewPlugin:
    pass
