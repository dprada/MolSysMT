from molsysmt._private.digestion import digest
import numpy as np
from scipy.spatial.transform import Rotation
from molsysmt import pyunitwizard as puw
import gc

@digest()
def rotate(molecular_system, rotation=None, rotation_center=None, selection='all', structure_indices='all',
        syntax='MolSysMT', in_place=False):

    from molsysmt.basic import get, set, select
    from molsysmt.structure import translate

    atom_indices = select(molecular_system, selection=selection, syntax=syntax)
    coordinates = get(molecular_system, element='atom', indices=atom_indices, structure_indices=structure_indices,
                      coordinates=True)

    if rotation_center is not None:

        coordinates = translate(coordinates, translation=-rotation_center)

    coordinates, length_unit =  puw.get_value_and_unit(coordinates)

    if isinstance(rotation, np.ndarray):

        shape=rotation.shape

        if shape[:2]==(1,1):
            rotator = Rotation.from_matrix(rotation[0,0,:,:])
            for ii in range(coordinates.shape[0]):
                coordinates[ii,:,:] = rotator.apply(coordinates[ii,:,:])
        elif shape[1]==1:
            for ii in range(coordinates.shape[0]):
                rotator = Rotation.from_matrix(rotation[ii,0,:,:])
                coordinates[ii,:,:] = rotator.apply(coordinates[ii,:,:])
        else:
            for ii in range(coordinates.shape[0]):
                for jj in range(coordinates.shape[1]):
                    rotator = Rotation.from_matrix(rotation[ii,jj,:,:])
                    coordinates[ii,jj,:] = rotator.apply(coordinates[ii,jj,:])

    elif isinstance(rotation, type(Rotation)):

        raise NotImplementedError

    else:

        raise NotImplementedError

    coordinates = puw.quantity(coordinates, unit=length_unit)

    if rotation_center is not None:

        coordinates = translate(coordinates, translation=rotation_center)


    if in_place:

        set(molecular_system, element='atom', indices=atom_indices, structure_indices=structure_indices,
            coordinates=coordinates)
        del(coordinates, rotation_center, atom_indices)
        gc.collect()

    else:

        tmp_molecular_system = copy(molecular_system)
        set(tmp_molecular_system, element='atom', indices=atom_indices, structure_indices=structure_indices,
            coordinates=new_coordinates)
        del(coordinates, rotation_center, atom_indices)
        gc.collect()

        return tmp_molecular_system

