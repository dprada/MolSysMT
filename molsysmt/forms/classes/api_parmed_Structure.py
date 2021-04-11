from molsysmt._private_tools.exceptions import *
from molsysmt.forms.common_gets import *
import numpy as np
from parmed.structure import Structure as _parmed_Structure
from molsysmt.molecular_system import molecular_system_components

form_name='parmed.Structure'

is_form={
    _parmed_Structure : form_name
}

info=["",""]

has = molecular_system_components.copy()
for ii in ['elements', 'coordinates', 'box', 'ff_parameters']:
    has[ii]=True

## Methods

def to_openmm_Topology(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    tmp_item = item.topology

    return tmp_item

def to_openmm_Modeller(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    from simtk.openmm.app.modeller import Modeller
    from molsysmt.forms.classes.api_openmm_Modeller import opemm_Modeller_to_openmm_Modeller as openmm_Modeller_to_openmm_Modeller

    tmp_item = Modeller(item.topology, item.positions)

    if (atom_indices is not 'all') or (frame_indices is not 'all'):
        tmp_item = openmm_Modeller_to_openmm_Modeller(tmp_item, atom_indices=atom_indices, frame_indices=frame_indices)

    return tmp_item

def to_mdtraj_Topology(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    from mdtraj.core.topology import Topology as mdtraj_Topology
    from .api_mdtraj_Topology import to_mdtraj_Topology as mdtraj_Topology_to_mdtraj_Topology

    tmp_item = mdtraj_Topology.from_openmm(item.topology)

    if (atom_indices is not 'all') or (frame_indices is not 'all'):
        tmp_item = mdtraj_Topology_to_mdtraj_Topology(tmp_item, atom_indices=atom_indices, frame_indices=frame_indices)

    return tmp_item

def to_mdtraj_Trajectory(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    from mdtraj.core.trajectory import Trajectory as mdtraj_trajectory
    from simtk.unit import nanometers

    tmp_topology = to_mdtraj_Topology(item, molecular_system, atom_indices=atom_indices, frame_indices=frame_indices)
    coordinates = get_coordinates_from_atom(item, indices=atom_indices, frame_indices=frame_indices)
    coordinates = coordinates.in_units_of(nanometers)._value
    tmp_item = mdtraj_trajectory(coordinates, tmp_topology)
    del(tmp_topology, coordinates)

    return tmp_item

def to_nglview_NGLWidget(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    from nglview import show_parmed as _nglview_show_parmed

    if (atom_indices is not 'all') or (frame_indices is not 'all'):
        tmp_item = to_parmed_Structure(item, molecular_system=molecular_system, atom_indices=atom_indices, frame_indices=frame_indices)
    else:
        tmp_item = item

    tmp_item = _nglview_show_parmed(tmp_item)

    return tmp_item

def to_pdb(item, molecular_system=None, atom_indices='all', frame_indices='all', output_filename=None):

    if (atom_indices is not 'all') or (frame_indices is not 'all'):
        tmp_item = to_parmed_Structure(item, molecular_system=molecular_system, atom_indices=atom_indices, frame_indices=frame_indices)
    else:
        tmp_item = item

    tmp_item.save(output_filename)

    return output_filename

def to_mol2(item, molecular_system=None, atom_indices='all', frame_indices='all', output_filename=None):

    if (atom_indices is not 'all') or (frame_indices is not 'all'):
        tmp_item = to_parmed_Structure(item, molecular_system=molecular_system, atom_indices=atom_indices, frame_indices=frame_indices)
    else:
        tmp_item = item

    tmp_item.save(output_filename)

    return output_filename

def select_with_MDTraj(item, selection):

    tmp_form=to_mdtraj(item)
    tmp_sel=tmp_form.topology.select(selection)
    del(tmp_form)
    return tmp_sel

def select_with_ParmEd(item, selection):

    from parmed.amber import AmberMask as _AmberMask
    tmp_sel = list(_AmberMask(item,selection).Selected())
    del(_AmberMask)
    return tmp_sel

def to_parmed_Structure(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    if (atom_indices is 'all') and (frame_indices is 'all'):
        from copy import deepcopy
        tmp_item = deepcopy(item)
        return tmp_item
    else:
        from molsysmt._private_tools.atom_indices import atom_indices_to_AmberMask
        from molsysmt._private_tools.atom_indices import complementary_atom_indices
        tmp_atom_indices = complementary_atom_indices(item, atom_indices)
        mask = atom_indices_to_AmberMask(item, tmp_atom_indices)
        tmp_item = copy(item)
        tmp_item.strip(atom_indices2AmberMask(atom_indices,len(item.atoms),inverse=True))
        return tmp_item

def add(item, from_item, atom_indices='all', frame_indices='all'):

    raise NotImplementedError

def append_frames(item, step=None, time=None, coordinates=None, box=None):

    raise NotImplementedError

##### Set

## Atom

def get_n_atoms_from_atom (item, indices='all', frame_indices='all'):

    return len(item.atoms)

def get_n_groups_from_atom (item, indices='all', frame_indices='all'):

    return len(item.groups)

def get_mass_from_atom (item, indices='all', frame_indices='all'):

    return [atom.mass for atom in item.atoms]

def get_bonded_atoms_from_atom (item, indices='all', frame_indices='all'):

    tmp_bonded = [[] for ii in range(len(st.atoms))]
    for bond in st.bonds:
        tmp_bonded[bond.atom1.idx].append(bond.atom2.idx)
        tmp_bonded[bond.atom2.idx].append(bond.atom1.idx)

    return tmp_bonded

def get_bonds_from_atom (item, indices='all', frame_indices='all'):

    tmp_bonds = []
    for bond in item.bonds:
        tmp_bonds.append([bond.atom1.idx,bond.atom2.idx])

    return tmp_bonds

def get_graph_from_atom (item, indices='all', frame_indices='all'):

    from networkx import Graph as _Graph
    tmp_graph = _Graph(getting(item,bonds=True))
    for atom in item.atoms:
        if len(atom.bonds)==0:
            tmp_graph.add_node(atom.idx)
    result.append(tmp_graph)

def get_molecules_from_atom (item, indices='all', frame_indices='all'):

    from networkx import connected_components as _connected_components
    tmp_graph = getting(item, graph=True)
    result.append([list(ii) for ii in _connected_components(tmp_graph)])

def get_molecule_type_from_atom (item, indices='all', frame_indices='all'):

    from molsysmt._private_tools.types import group2molecule_types
    tmp_molecules = getting(item,molecules=True)
    tmp_types = []
    for molecule in tmp_molecules:
        tmp_types.append(group2molecule_types(item.atoms[molecule[0]].group.name))
    if len(tmp_types)==1:
        tmp_types=tmp_types[0]
    return tmp_types


## system

def get_n_atoms_from_system (item, indices='all', frame_indices='all'):

    return len(item.atoms)

