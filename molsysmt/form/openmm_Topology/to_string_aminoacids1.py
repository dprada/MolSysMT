from molsysmt._private.digestion import digest
import numpy as np

@digest(form='openmm.Topology')
def to_string_aminoacids1(item, atom_indices='all'):

    from . import to_molsysmt_Topology
    from ..molsysmt_Topology import to_string_aminoacids1 as molsysmt_Topology_to_string_aminoacids1
    from . import get_group_index_from_atom

    tmp_item = to_molsysmt_Topology(item)
    tmp_item = molsysmt_Topology_to_string_aminoacids1(tmp_item, atom_indices=atom_indices)

    return tmp_item

