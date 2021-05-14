from molsysmt._private_tools.exceptions import *
from molsysmt.forms.common_gets import *
import numpy as np
import importlib
import sys
from molsysmt.molecular_system import molecular_system_components

form_name='file:xtc'

is_form = {
    }

info=["",""]

has = molecular_system_components.copy()
for ii in ['coordinates', 'box']:
    has[ii]=True

def to_molsysmt_Trajectory(item, molecular_system, atom_indices='all', frame_indices='all'):

    from molsysmt.native.io.trajectory.files import from_xtc as xtc_to_molsysmt_Trajectory

    tmp_item, tmp_molecular_system = xtc_to_molsysmt_Trajectory(item, molecular_system, atom_indices=atom_indices, frame_indices=frame_indices)

    return tmp_item, tmp_molecular_system

def to_mdtraj_XTCTrajectoryFile(item, molecular_system, atom_indices='all', frame_indices='all'):

    from mdtraj.formats import XTCTrajectoryFile

    tmp_item = XTCTrajectoryFile(item)
    tmp_molecular_system = molecular_system.combine_with_items(tmp_item)

    return tmp_item, tmp_molecular_system

def to_file_xtc(item, molecular_system, atom_indices='all', frame_indices='all', output_filename=None, copy_if_all=True):

    if (atom_indices is 'all') and (frame_indices is 'all'):
        if copy_if_all:
            tmp_item = extract_item(item)
            tmp_molecular_system = molecular_system.combine_with_items(tmp_item)
        else:
            tmp_item = item
            tmp_molecular_system = molecular_system
    else:
        tmp_item = extract_item(item, atom_indices=atom_indices, frame_indices=frame_indices)
        tmp_molecular_system = molecular_system.combine_with_items(tmp_item, atom_indices=atom_indices, frame_indices=frame_indices)

    return tmp_item, tmp_molecular_system

def extract_item(item, atom_indices='all', frame_indices='all'):

    if (atom_indices is 'all') and (frame_indices is 'all'):
        raise NotImplementedError()
    else:
        raise NotImplementedError()

    return tmp_item

def add(item, from_item, atom_indices='all', frame_indices='all'):

    raise NotImplementedError

def append_frames(item, step=None, time=None, coordinates=None, box=None):

    raise NotImplementedError

#### Get

def aux_get(item, indices='all', frame_indices='all'):

    from molsysmt.forms import forms

    if 'mdtraj.XTCTrajectoryFile' in forms:

        tmp_item = to_mdtraj_XTCTrajectoryFile(item)
        method_name = sys._getframe(1).f_code.co_name
        module = importlib.import_module('molsysmt.forms.classes.api_mdtraj_XTCTrajectoryFile')
        _get = getattr(module, method_name)
        output = _get(tmp_item, indices=indices, frame_indices=frame_indices)

    else:

        raise NotImplementedError

    return output

## atom

def get_atom_index_from_atom(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_atom_id_from_atom(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_atom_name_from_atom(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_atom_type_from_atom(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_group_index_from_atom (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_component_index_from_atom (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_chain_index_from_atom (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_molecule_index_from_atom (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_entity_index_from_atom (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_inner_bonded_atoms_from_atom (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_n_inner_bonds_from_atom (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_n_inner_bonds_from_atom (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_coordinates_from_atom(item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_frame_from_atom(item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

## group

def get_group_id_from_group(item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_group_name_from_group(item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_group_type_from_group(item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

## component

def get_component_id_from_component (item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_component_name_from_component (item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_component_type_from_component (item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

## molecule

def get_molecule_id_from_molecule (item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_molecule_name_from_molecule (item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_molecule_type_from_molecule (item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

## chain

def get_chain_id_from_chain (item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_chain_name_from_chain (item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_chain_type_from_chain (item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

## entity

def get_entity_id_from_entity (item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_entity_name_from_entity (item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_entity_type_from_entity (item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

## system

def get_n_atoms_from_system(item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_n_groups_from_system(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_n_components_from_system(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_n_chains_from_system(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_n_molecules_from_system(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_n_entities_from_system(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_n_bonds_from_system(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_coordinates_from_system(item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_box_from_system(item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_box_shape_from_system(item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_box_lengths_from_system(item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_box_angles_from_system(item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_box_volume_from_system(item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_time_from_system(item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_step_from_system(item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_n_frames_from_system(item, indices='all', frame_indices='all'):

    return aux_get(item, indices=indices, frame_indices=frame_indices)

def get_bonded_atoms_from_system(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

## bond

def get_bond_order_from_bond(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_bond_type_from_bond(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_atom_index_from_bond(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

###### Set

def set_box_to_system(item, indices='all', frame_indices='all', value=None):

    raise NotImplementedError

def set_coordinates_to_system(item, indices='all', frame_indices='all', value=None):

    raise NotImplementedError
