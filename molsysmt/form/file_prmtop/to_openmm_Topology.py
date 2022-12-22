from molsysmt._private.digestion import digest

@digest(form='file:prmtop')
def to_openmm_Topology(item, atom_indices='all', digest=True):

    from . import to_openmm_AmberPrmtopFile
    from ..openmm_AmberPrmtopFile import to_openmm_Topology as openmm_AmberPrmtopFile_to_openmm_Topology

    tmp_item = to_openmm_AmberPrmtopFile(item, digest=False)
    tmp_item = openmm_AmberPrmtopFile_to_openmm_Topology(tmp_item, atom_indices=atom_indices, digest=False)

    return tmp_item

