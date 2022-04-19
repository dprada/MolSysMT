from molsysmt._private.exceptions import *

from molsysmt.form.file_pdb.is_file_pdb import is_file_pdb as is_form
from molsysmt.form.file_pdb.extract import extract
from molsysmt.form.file_pdb.add import add
from molsysmt.form.file_pdb.append_structures import append_structures
from molsysmt.form.file_pdb.get import *
from molsysmt.form.file_pdb.set import *

form_name='mdtraj.HDF5TrajectoryFile'
form_type='class'
form_info=["",""]

form_attributes = {

    'atom_index' : True,
    'atom_id' : True,
    'atom_name' : True,
    'atom_type' : True,

    'bond_index' : True,
    'bond_id' : True,
    'bond_name' : True,
    'bond_type' : True,
    'bond_order' : True,

    'group_index' : True,
    'group_id' : True,
    'group_name' : True,
    'group_type' : True,

    'component_index' : True,
    'component_id' : False,
    'component_name' : False,
    'component_type' : False,

    'molecule_index' : True,
    'molecule_id' : True,
    'molecule_name' : True,
    'molecule_type' : True,

    'chain_index' : True,
    'chain_id' : True,
    'chain_name' : True,
    'chain_type' : True,

    'entity_index' : False,
    'entity_id' : False,
    'entity_name' : False,
    'entity_type' : False,

    'coordinates' : True,
    'velocities' : True,
    'box' : True,
    'time' : True,
    'step' : True,

    'forcefield_parameters' : True,

    'forcefield' : False,
    'temperature' : False,
    'pressure' : False,
    'integrator' : False,
    'damping' : False,
}

def to_mdtraj_Topology(item, molecular_system, atom_indices='all', structure_indices='all'):

    from molsysmt.form.mdtraj_HDF5TrajectoryFile import to_mdtraj_Topology as mdtraj_HDF5TrajectoryFile_to_mdtraj_Topology

    tmp_item = mdtraj_HDF5TrajectoryFile_to_mdtraj_Topology(item, atom_indices=atom_indices, structure_indices=structure_indices, check=False)

    return tmp_item


def merge(item_1, item_2):

    raise NotImplementedError

def add(to_item, item):

    raise NotImplementedError

def append_structures(item, step=None, time=None, coordinates=None, box=None):

    raise NotImplementedError

def concatenate_structures(item, step=None, time=None, coordinates=None, box=None):

    raise NotImplementedError

#### Get

# atom

def get_atom_id_from_atom(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_atom_name_from_atom(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_atom_type_from_atom(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_group_index_from_atom (item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_component_index_from_atom (item, indices='all', structure_indices='all'):

    from molsysmt.elements.component import get_component_index_from_atom as _get
    return _get(item, indices=indices)

def get_chain_index_from_atom (item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_molecule_index_from_atom (item, indices='all', structure_indices='all'):

    from molsysmt.elements.molecule import get_molecule_index_from_atom as _get
    return _get(item, indices=indices)

def get_entity_index_from_atom (item, indices='all', structure_indices='all'):

    from molsysmt.elements.entity import get_entity_index_from_atom as _get
    return _get(item, indices=indices)

def get_inner_bonded_atoms_from_atom (item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_n_inner_bonds_from_atom (item, indices='all', structure_indices='all'):

    if indices is 'all':
        return get_n_inner_bonds_from_system (item)
    else:
        raise NotImplementedError

def get_coordinates_from_atom(item, indices='all', structure_indices='all'):

    from molsysmt._private.math import serie_to_chunks

    if structure_indices is 'all':
        structure_indices = np.arange(get_n_structures_from_system(item))
    if indices is 'all':
        indices = np.arange(get_n_atoms_from_system(item))

    starts_serie_frames, size_serie_frames = serie_to_chunks(structure_indices)

    xyz_list = []

    for start, size in zip(starts_serie_frames, size_serie_frames):
        item.seek(start)
        frame_hdf5 = item.read(n_structures=size, atom_indices=indices)
        xyz = frame_hdf5.coordinates
        xyz_list.append(xyz)

    xyz = np.concatenate(xyz_list)
    del(xyz_list)

    xyz = xyz.astype('float64')

    xyz = xyz*puw.unit('nm')
    xyz = puw.standardize(xyz)

    return xyz

def get_frame_from_atom(item, indices='all', structure_indices='all'):

    from molsysmt._private.math import serie_to_chunks
    from molsysmt.pbc import box_vectors_from_box_lengths_and_angles

    if structure_indices is 'all':
        structure_indices = np.arange(get_n_structures_from_system(item))
    if indices is 'all':
        indices = np.arange(get_n_atoms_from_system(item))

    starts_serie_frames, size_serie_frames = serie_to_chunks(structure_indices)

    xyz_list = []
    time_list = []
    box_list = []

    for start, size in zip(starts_serie_frames, size_serie_frames):
        item.seek(start)
        frame_hdf5 = item.read(n_structures=size, atom_indices=indices)
        xyz = frame_hdf5.coordinates
        xyz_list.append(xyz)
        time = frame_hdf5.time
        time_list.append(time)
        cell_lengths = frame_hdf5.cell_lengths*puw.unit('nm')
        cell_angles = frame_hdf5.cell_angles*puw.unit('degrees')
        box = box_vectors_from_box_lengths_and_angles(cell_lengths, cell_angles)
        box_list.append(puw.get_value(box))

    xyz = np.concatenate(xyz_list)
    del(xyz_list)
    time = np.concatenate(time_list)
    del(time_list)
    box = np.concatenate(box_list)
    del(box_list)

    xyz = xyz.astype('float64')
    box = box.astype('float64')
    time = time.astype('float64')

    xyz = xyz*puw.unit('nm')
    xyz = puw.standardize(xyz)
    box = box*puw.unit('nm')
    box = puw.standardize(box)
    time = time*puw.unit('ps')
    time = puw.standardize(time)
    step = None

    return step, time, xyz, box

## group

def get_group_id_from_group(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_group_name_from_group(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_group_type_from_group(item, indices='all', structure_indices='all'):

    raise NotImplementedError

## component

def get_component_id_from_component (item, indices='all', structure_indices='all'):

    from molsysmt.elements.component import get_component_id_from_component as get
    return get(item, indices)

def get_component_name_from_component (item, indices='all', structure_indices='all'):

    from molsysmt.elements.component import get_component_name_from_component as get
    return get(item, indices)

def get_component_type_from_component (item, indices='all', structure_indices='all'):

    from molsysmt.elements.component import get_component_type_from_component as get
    return get(item, indices)

## molecule

def get_molecule_id_from_molecule (item, indices='all', structure_indices='all'):

    from molsysmt.elements.molecule import get_molecule_id_from_molecule as get
    return get(item, indices)

def get_molecule_name_from_molecule (item, indices='all', structure_indices='all'):

    from molsysmt.elements.molecule import get_molecule_name_from_molecule as get
    return get(item, indices)

def get_molecule_type_from_molecule (item, indices='all', structure_indices='all'):

    from molsysmt.elements.molecule import get_molecule_type_from_molecule as get
    return get(item, indices)

## chain

def get_chain_id_from_chain (item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_chain_name_from_chain (item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_chain_type_from_chain (item, indices='all', structure_indices='all'):

    raise NotImplementedError

## entity

def get_entity_id_from_entity (item, indices='all', structure_indices='all'):

    from molsysmt.elements.entity import get_entity_id_from_molecule as get
    return get(item, indices)

def get_entity_name_from_entity (item, indices='all', structure_indices='all'):

    from molsysmt.elements.entity import get_entity_name_from_molecule as get
    return get(item, indices)

def get_entity_type_from_entity (item, indices='all', structure_indices='all'):

    from molsysmt.elements.entity import get_entity_type_from_molecule as get
    return get(item, indices)

## system

def get_n_atoms_from_system (item, indices='all', structure_indices='all'):

    return item.topology.n_atoms

def get_n_groups_from_system(item, indices='all', structure_indices='all'):

    return item.topology.n_residues

def get_n_components_from_system(item, indices='all', structure_indices='all'):

    from molsysmt.elements.component import get_n_components_from_system as get
    return get(item, indices)

def get_n_chains_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_n_molecules_from_system(item, indices='all', structure_indices='all'):

    from molsysmt.elements.molecule import get_n_molecules_from_system as get
    return get(item, indices)

def get_n_entities_from_system(item, indices='all', structure_indices='all'):

    from molsysmt.elements.entity import get_n_entities_from_system as get
    return get(item, indices)

def get_n_bonds_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_coordinates_from_system(item, indices='all', structure_indices='all'):

    return get_coordinates_from_atom(item, indices='all', structure_indices=structure_indices)

def get_box_from_system(item, indices='all', structure_indices='all'):

    from molsysmt._private.math import serie_to_chunks
    from molsysmt.pbc import box_vectors_from_box_lengths_and_angles

    if structure_indices is 'all':
        structure_indices = np.arange(get_n_structures_from_system(item))

    starts_serie_frames, size_serie_frames = serie_to_chunks(structure_indices)

    box_list = []

    for start, size in zip(starts_serie_frames, size_serie_frames):
        item.seek(start)
        frame_hdf5 = item.read(n_structures=size, atom_indices=atom_indices)
        cell_lengths = frame_hdf5.cell_lengths
        cell_angles = frame_hdf5.cell_angles
        box = box_vectors_from_box_lengths_and_angles(cell_lengths*puw.unit('nm'), cell_angles*puw.unit('degrees'))
        box_list.append(puw.get_value(box))

    box = np.concatenate(box_list)
    del(box_list)

    box = box.astype('float64')

    box = box*puw.unit('nm')
    box = puw.standardize(box)

    return box

def get_box_shape_from_system (item, indices='all', structure_indices='all'):

    from molsysmt._private.pbc import get_shape_from_angles
    position = item.tell()
    frame_hdf5 = item.read(n_structures=1)
    cell_angles = frame_hdf5.cell_angles * puw.unit('degrees')
    shape = get_shape_from_angles(cell_angles)
    item.seek(position)
    del(frame_hdf5)
    return shape

def get_box_lengths_from_system(item, indices='all', structure_indices='all'):

    from molsysmt._private.math import serie_to_chunks

    if structure_indices is 'all':
        structure_indices = np.arange(get_n_structures_from_system(item))

    starts_serie_frames, size_serie_frames = serie_to_chunks(structure_indices)

    cell_lengths_list = []

    for start, size in zip(starts_serie_frames, size_serie_frames):
        item.seek(start)
        frame_hdf5 = item.read(n_structures=size, atom_indices=atom_indices)
        cell_lengths_list.append(frame_hdf5.cell_lengths)

    cell_lengths = np.concatenate(cell_lengths_list)
    del(cell_lengths_list)

    cell_lengths = cell_lengths.astype('float64')

    cell_lengths = cell_lengths*puw.unit('nm')
    cell_lengths = puw.standardize(cell_lengths)

    return cell_lengths

def get_box_angles_from_system(item, indices='all', structure_indices='all'):

    from molsysmt._private.math import serie_to_chunks

    if structure_indices is 'all':
        structure_indices = np.arange(get_n_structures_from_system(item))

    starts_serie_frames, size_serie_frames = serie_to_chunks(structure_indices)

    cell_angles_list = []

    for start, size in zip(starts_serie_frames, size_serie_frames):
        item.seek(start)
        frame_hdf5 = item.read(n_structures=size, atom_indices=atom_indices)
        cell_angles_list.append(frame_hdf5.cell_angles)

    cell_angles = np.concatenate(cell_angles_list)
    del(cell_angles_list)

    cell_lengths = cell_angles.astype('float64')

    cell_lengths = cell_angles*puw.unit('degrees')
    cell_angles = puw.standardize(cell_angles)

    return cell_angles

def get_box_volume_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_time_from_system(item, indices='all', structure_indices='all'):

    from molsysmt._private.math import serie_to_chunks

    if structure_indices is 'all':
        structure_indices = np.arange(get_n_structures_from_system(item))

    starts_serie_frames, size_serie_frames = serie_to_chunks(structure_indices)

    time_list = []

    for start, size in zip(starts_serie_frames, size_serie_frames):
        item.seek(start)
        frame_hdf5 = item.read(n_structures=size, atom_indices=atom_indices)
        time = frame_hdf5.time
        time_list.append(time)

    time = np.concatenate(time_list)
    del(time_list)

    time = time.astype('float64')

    time = time*puw.unit('ps')
    time = puw.standardize(time)

    return time

def get_step_from_system(item, indices='all', structure_indices='all'):

    return None

def get_n_structures_from_system (item, indices='all', structure_indices='all'):

    return item._handle.root.coordinates.shape[0]

def get_bonded_atoms_from_system(item, indices='all', structure_indices='all'):

    raise NotImplementedError

## bond

def get_bond_order_from_bond(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_bond_type_from_bond(item, indices='all', structure_indices='all'):

    raise NotImplementedError

def get_atom_index_from_bond(item, indices='all', structure_indices='all'):

    raise NotImplementedError

###### Set

def set_box_to_system(item, indices='all', structure_indices='all', value=None):

    raise NotImplementedError

def set_coordinates_to_system(item, indices='all', structure_indices='all', value=None):

    raise NotImplementedError
