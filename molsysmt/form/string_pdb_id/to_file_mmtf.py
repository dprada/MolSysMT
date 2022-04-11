from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *

def to_file_mmtf(item, atom_indices='all', structure_indices='all', output_filename=None, check=True):

    if check:

        digest_item(item, 'string:pdb_id')
        atom_indices = digest_atom_indices(atom_indices)
        structure_indices = digest_structure_indices(structure_indices)

    from ..file_mmtf import download as download_file_mmtf
    from ..file_mmtf import extract as extract_file_mmtf

    download_file_mmtf(item, output_filename)
    tmp_item = extract_file_mmtf(tmp_item, atom_indices=atom_indices, structure_indices=structure_indices,
            output_filename=output_filename, copy_if_all=False, check=False)

    return tmp_item

