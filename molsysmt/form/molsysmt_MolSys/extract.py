from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *
from .is_molsysmt_MolSys import is_molsysmt_MolSys

def extract(item, atom_indices='all', structure_indices='all', copy_if_all=True, check=True):

    if check:

        try:
            is_molsysmt_MolSys(item)
        except:
            raise WrongFormError('molsysmt.MolSys')

        try:
            atom_indices = digest_atom_indices(atom_indices)
        except:
            raise WrongAtomIndicesError()

        try:
            structure_indices = digest_structure_indices(structure_indices)
        except:
            raise WrongStructureIndicesError()


    if (atom_indices is 'all') and (structure_indices is 'all'):
        if copy_if_all:
            tmp_item = item.copy()
        else:
            tmp_item = item
    else:
        tmp_item = item.extract(atom_indices=atom_indices, structure_indices=structure_indices)

    return tmp_item
