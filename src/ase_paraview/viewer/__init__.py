import sys

from ase._4.plugins.viewer import ViewerPlugin

THIS_MODULE = sys.modules[__name__]


def _get_viewer():
    from ase_paraview.viewer.plugin import ParaViewViewer
    return ParaViewViewer


paraview_plugin = ViewerPlugin(
    name="paraview",
    citation="Andrei Sobolev and the ASE Developers",
    module=THIS_MODULE,
    implementation=_get_viewer,
)
