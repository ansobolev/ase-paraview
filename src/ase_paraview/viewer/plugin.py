from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path
from typing import TYPE_CHECKING

from ase.visualize.viewers import CLIViewer

if TYPE_CHECKING:
    from ase import Atoms


def view_paraview(atoms: Atoms, **_) -> subprocess.Popen:
    from ase.io import write

    with tempfile.NamedTemporaryFile(suffix='.xyz', delete=False) as f:
        tmp_path = Path(f.name)

    write(str(tmp_path), atoms)
    return subprocess.Popen(['paraview', str(tmp_path)])


view_paraview_v3 = view_paraview


class ParaViewViewer(CLIViewer):
    def __init__(self):
        super().__init__('paraview', 'xyz', ['paraview'])

    def view(self, atoms, data=None, repeat=None, **kwargs):
        view_paraview(atoms, **kwargs)

        # The code below is for use inside a running ParaView session (e.g. pvpython),
        # not for launching ParaView from ASE.
        #
        # import paraview.simple as para
        # source = para.GetActiveSource()
        # renderView1 = para.GetRenderView()
        # atoms = para.Glyph(
        #     Input=source,
        #     GlyphType='Sphere',
        #     Scalars='radii',
        #     ScaleMode='scalar',
        # )
        # para.RenameSource('Atoms', atoms)
        # atomsDisplay = para.Show(atoms, renderView1)
        # atoms.ScaleFactor = 0.8
        # para.ColorBy(atomsDisplay, 'atomic numbers')
        # atomsDisplay.SetScalarBarVisibility(renderView1, True)
        # para.Render()
