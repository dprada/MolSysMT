from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *

def to_pdbfixer_PDBFixer(item, atom_indices='all', structure_indices='all', check=True):

    if check:

        digest_item(item, 'openmm.Simulation')
        atom_indices = digest_atom_indices(atom_indices)
        structure_indices = digest_structure_indices(structure_indices)

    from . import to_file_pdb as openmm_Simulation_to_file_pdb
    from molsysmt._private.files_and_directories import temp_filename
    from molsysmt.item.file_pdb import to_pdbfixer_PDBFixer as file_pdb_to_pdbfixer_PDBFixer
    from os import remove

    tmp_file = temp_filename(extension='pdb')
    tmp_item = molsysmt_Simulation_to_file_pdb(item, output_filename=tmp_file,
            atom_indices=atom_indices, structure_indices=structure_indices, check=False)
    tmp_item = file_pdb_to_pdbfixer_PDBFixer(tmp_file, check=False)
    remove(tmp_pdbfile)

    return tmp_item
