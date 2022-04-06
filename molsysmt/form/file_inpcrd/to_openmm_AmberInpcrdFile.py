from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *
from .is_file_inpcrd import is_file_inpcrd

def to_openmm_AmberInpcrdFile(item, atom_indices='all', structure_indices='all', check=True):

    if check:

        try:
            is_file_inpcrd(item)
        except:
            raise WrongFormError('file:inpcrd')

        try:
            atom_indices = digest_atom_indices(atom_indices)
        except:
            raise WrongAtomIndicesError()

        try:
            structure_indices = digest_structure_indices(structure_indices)
        except:
            raise WrongStructureIndicesError()

    from openmm.app import AmberInpcrdFile

    tmp_item = AmberInpcrdFile(item)

    return tmp_item
