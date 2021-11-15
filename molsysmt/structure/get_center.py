from molsysmt._private_tools.exceptions import *
from molsysmt._private_tools._digestion import *
from molsysmt._private_tools.math import serialized_lists
from molsysmt.basic import select, get
from molsysmt.lib import com as libcom
from molsysmt import puw
import numpy as np

def get_center(molecular_system, selection='all', groups_of_atoms=None, weights=None, frame_indices='all', syntaxis='MolSysMT', engine='MolSysMT', parallel=False):

    molecular_system = digest_molecular_system(molecular_system)
    engine = digest_engine(engine)

    if engine=='MolSysMT':

        if groups_of_atoms is None:
            atom_indices = select(molecular_system, selection=selection, syntaxis=syntaxis)
            groups_of_atoms = [atom_indices]

        groups_serialized = serialized_lists(groups_of_atoms, dtype='int64')

        if weights is None:
            weights = np.ones((groups_serialized.n_values))
        elif weights is 'masses':
            raise NotImplementedError

        coordinates = get(molecular_system, target='system', frame_indices=frame_indices, coordinates=True)

        length_units = puw.get_unit(coordinates)
        coordinates = np.asfortranarray(puw.get_value(coordinates), dtype='float64')
        n_atoms = coordinates.shape[1]
        n_frames = coordinates.shape[0]

        com = libcom.center_of_mass(coordinates,
                                    groups_serialized.indices, groups_serialized.values, groups_serialized.starts,
                                    weights, n_frames, n_atoms,
                                    groups_serialized.n_indices, groups_serialized.n_values)

        del(coordinates, groups_serialized)

        return com*length_units

    else:

        raise NotImplementedError(NotImplementedMessage)

