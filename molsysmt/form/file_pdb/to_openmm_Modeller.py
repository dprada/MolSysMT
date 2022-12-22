from molsysmt._private.digestion import digest

@digest(form='file:pdb')
def to_openmm_Modeller(item, atom_indices='all', structure_indices='all', digest=True):

    from . import to_openmm_PDBFile
    from ..openmm_PDBFile import to_openmm_Modeller as openmm_PDBFile_to_openmm_Modeller

    tmp_item = to_openmm_PDBFile(item, digest=False)
    tmp_item = openmm_PDBFile_to_openmm_Modeller(item, atom_indices=atom_indices, structure_indices=structure_indices, digest=False)

    return tmp_item

