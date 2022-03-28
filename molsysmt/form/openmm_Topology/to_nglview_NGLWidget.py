from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *
from .is_openmm_Topology import is_openmm_Topology


def to_nglview_NGLWidget(item, atom_indices='all', coordinates=None, check=True):

    if check:

        try:
            is_pdbfixer_PDBFixer(item)
        except:
            raise WrongFormError('pdbfixer.PDBFixer')

        try:
            atom_indices = digest_atom_indices(atom_indices)
        except:
            raise WrongAtomIndicesError()

        try:
            coordinates = digest_coordinates(coordinates)
        except:
            raise WrongCoordinatesError()

    from . import to_string_pdb_text as to_string_pdb_text
    from ..string_pdb_text import to_nglview_NGLWidget as string_pdb_text_to_nglview_NGLWidget

    tmp_item = to_string_pdb_text(item, atom_indices=atom_indices, check=False)
    tmp_item = string_pdb_text_to_nglview_NGLWidget(tmp_item, check=False)

    return tmp_item
