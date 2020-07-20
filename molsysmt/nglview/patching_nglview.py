
patch_show =\
"\n\
\n\
### From MolSysMT\n\
\n\
from .adaptor import MolSysMTTrajectory\n\
\n\
__all__.append('show_molsysmt')\n\
\n\
def show_molsysmt(molsys, selection='all', frame_indices='all', **kwargs):\n\
    '''Show NGL widget with molsysmt.MolSys object.\n\
\n\
    Visit `MolSysmt documentation webpage <http://www.uibcdf.org/MolSysMT>`_ for further\n\
    info.\n\
\n\
    Examples\n\
    --------\n\
    >>> import nglview as nv # doctest: +SKIP\n\
    ... import molsysmt as msm\n\
    ... t = msm.convert([nv.datafiles.GRO, nv.datafiles.XTC])\n\
    ... w = nv.show_molsysmt(t)\n\
    ... w\n\
    '''\n\
    structure_trajectory = MolSysMTTrajectory(molsys, selection=selection,\n\
                                              frame_indices=frame_indices)\n\
    return NGLWidget(structure_trajectory, **kwargs)\n\
"


patch_adaptor=\
"\n\
\n\
### From MolSysMT\n\
\n\
__all__.append('MolSysMTTrajectory')\n\
\n\
@register_backend('molsysmt')\n\
class MolSysMTTrajectory(Trajectory, Structure):\n\
    '''MolSysMT adaptor.\n\
\n\
    Visit `MolSysmt documentation webpage <http://www.uibcdf.org/MolSysMT>`_ for further info.\n\
\n\
    Example\n\
    -------\n\
    >>> import nglview as nv\n\
    >>> import molsysmt as msm\n\
    >>> traj = msm.convert([nv.datafiles.GRO, nv.datafiles.XTC], to_form='molsysmt.MolSys')\n\
    >>> t = nv.MolSysMTTrajectory(traj)\n\
    >>> w = nv.NGLWidget(t)\n\
    >>> w\n\
    '''\n\
\n\
    def __init__(self, molsys, selection='all', frame_indices='all'):\n\
\n\
        try:\n\
            import molsysmt as msm\n\
        except ImportError:\n\
            raise ImportError(\n\
                \"'MolSysMTTrajectory' requires the molsysmt package\")\n\
\n\
        self.pdb = msm.convert(molsys, to_form='.pdb', selection=selection, frame_indices=0)\n\
        self.coordinates = 10.0*msm.get(molsys, target='system', frame_indices=frame_indices,\n\
                                        coordinates=True)._value\n\
        self.ext = \"pdb\"\n\
        self.params = {}\n\
        self.id = str(uuid.uuid4())\n\
\n\
    def get_coordinates(self, index):\n\
            return self.coordinates[index]\n\
\n\
    @property\n\
    def n_frames(self):\n\
        return self.coordinates.shape[0]\n\
\n\
    def get_structure_string(self):\n\
\n\
        return self.pdb\n\
"


def adding_molsysmt():

    from pathlib import Path
    import nglview as nv


    ## show.py

    filepath = Path(nv.__file__).parent / 'show.py'

    with open(filepath) as f:
        content = f.read()

    if 'MolSysMT' not in content:

        content += patch_show

        with open(filepath,'w') as f:
            f.write(content)

    ## adaptor.py

    filepath = Path(nv.__file__).parent / 'adaptor.py'

    with open(filepath) as f:
        content = f.read()

    if 'MolSysMT' not in content:

        content += patch_adaptor

        with open(filepath,'w') as f:
            f.write(content)

