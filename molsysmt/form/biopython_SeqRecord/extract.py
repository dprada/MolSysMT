from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *
from .is_biopython_SeqRecord import is_biopython_SeqRecord

def extract(item, atom_indices='all', structure_indices='all', copy_if_all=True, check=True):

    if check:

        try:
            is_biopython_SeqRecord(item)
        except:
            raise WrongFormError('biopython.SeqRecord')

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

        raise NotImplementedError

    return tmp_item
