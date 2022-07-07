from molsysmt._private.exceptions import *
from molsysmt._private.digestion import  *

def to_openmm_Simulation(item, atom_indices='all', coordinates=None, check=True):

    if check:

        digest_item(item, 'openmm.Topology')
        atom_indices = digest_atom_indices(atom_indices)
        coordinates = digest_coordinates(coordinates)

    from . import to_openmm_System
    from ..openmm_System import to_openmm_Simulation as openmm_System_to_openmm_Simulation

    tmp_item = to_openmm_System(item, atom_indices=atom_indices, coordinates=coordinates, check=False)
    tmp_item = openmm_System_to_openmm_Simulation(tmp_item, check=False)

    return tmp_item

