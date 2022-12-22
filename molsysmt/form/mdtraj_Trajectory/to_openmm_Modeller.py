from molsysmt._private.digestion import digest

@digest(form='mdtraj.Trajectory')
def to_openmm_Modeller(item, atom_indices='all', structure_indices='all', digest=True):

    from . import to_openmm_Topology
    from . import get_coordinates_from_atom
    from ..openmm_Topology import to_openmm_Modeller as openmm_Topology_to_openmm_Modeller

    tmp_item = to_openmm_Topology(item, atom_indices=atom_indices, digest=False)
    coordinates = get_coordinates_from_atom(item, indices=atom_indices, structure_indices=structure_indices, digest=False)
    tmp_item = openmm_Topology_to_openmm_Modeller(tmp_item, coordinates=coordinates, digest=False)

    return tmp_item

