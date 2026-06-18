import sys

from ase._4.plugins.viewer import ViewerPlugin
from ase.utils.plugins import ExternalViewer

THIS_MODULE = sys.modules[__name__]

V3ParaviewViewer = ExternalViewer(
    desc="View atoms using ParaView",
    module="ase_paraview.viewer.plugin",
)


def _get_viewer():
    from ase_paraview.viewer.plugin import ParaViewViewer
    return ParaViewViewer


paraview_plugin = ViewerPlugin(
    name="paraview",
    citation="Andrei Sobolev and the ASE Developers",
    module=THIS_MODULE,
    implementation=_get_viewer,
)
