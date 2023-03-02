from molsysmt._private.digestion import digest

@digest(form='openmm.PDBFile')
def to_molsysmt_Topology(item, atom_indices='all'):

    from .to_openmm_Topology import to_openmm_Topology
    from ..openmm_Topology import to_molsysmt_Topology as openmm_Topology_to_molsysmt_Topology

    tmp_item = to_openmm_Topology(item)
    tmp_item = openmm_Topology_to_molsysmt_Topology(tmp_item, atom_indices=atom_indices)

    return tmp_item

def _to_molsysmt_Topology(item, molecular_system, atom_indices='all', structure_indices='all'):

    return to_molsysmt_Topology(item, atom_indices=atom_indices)

