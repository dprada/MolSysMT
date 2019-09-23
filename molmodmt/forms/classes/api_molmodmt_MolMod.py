from os.path import basename as _basename
from molmodmt.utils.exceptions import *
from molmodmt import MolMod as _molmodmt_MolMod

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _molmodmt_MolMod : form_name,
    'molmod': form_name,
    'MolMod': form_name,
    'molmodmt.MolMod': form_name
}

def info(item):

    from molmodmt import get

    tmp_dict = {}
    tmp_dict['form'] = form_name
    tmp_dict['n_atoms'] = get(item, element='system', n_atoms=True)
    tmp_dict['trajectory file'] = item.trajectory.file.name
    tmp_dict['trajectory loaded'] = str(item.trajectory.n_frames)+' frames,'+str(item.trajectory.n_atoms)+' atoms'

    return tmp_dict

def to_aminoacids3_seq(item, selection=None, syntaxis='mdtraj'):

    from molmodmt import convert as _convert
    tmp_item = _convert(item,'mdtraj.Topology')
    tmp_item = _convert(tmp_item,'aminoacids3:seq')
    return tmp_item

def to_aminoacids1(item, selection=None, syntaxis='mdtraj'):
    return to_aminoacids1_seq(item, selection=selection, syntaxis=syntaxis)

def to_aminoacids1_seq(item, selection=None, syntaxis='mdtraj'):

    from molmodmt import convert as _convert
    tmp_item = to_aminoacids3_seq(item)
    tmp_item = _convert('aminoacids3:'+tmp_item,'aminoacids1:seq')
    return tmp_item

def to_biopython_Seq(item, selection=None, syntaxis='mdtraj'):

    from molmodmt.forms.seqs.api_aminoacids1 import to_biopython_Seq as _aminoacids1_to_biopython_Seq
    tmp_item = to_aminoacids1_seq(item)
    tmp_item = _aminoacids1_to_biopython_Seq(tmp_item)
    del(_aminoacids1_to_biopython_Seq)
    return tmp_item

def to_biopython_SeqRecord(item, selection=None, syntaxis='mdtraj'):

    from molmodmt.forms.seqs.api_aminoacids1 import to_biopython_SeqRecord as _aminoacids1_to_biopython_SeqRecord
    tmp_item = to_aminoacids1_seq(item)
    tmp_item = _aminoacids1_to_biopython_SeqRecord(tmp_item)
    del(_aminoacids1_to_biopython_SeqRecord)
    return tmp_item

def to_molmodmt(item):
    return item

def to_mdtraj(item, selection=None, syntaxis='MDTraj'):

    return to_mdtraj_Trajectory(item, selection=selection, syntaxis=syntaxis)

def to_mdtraj_Trajectory(item, selection=None, syntaxis='MDTraj'):

    from simtk import unit as _unit
    from mdtraj.core.trajectory import Trajectory as _mdtraj_Trajectory

    tmp_item_topology = to_mdtraj_Topology(item, selection=item.trajectory.file.atom_indices)
    tmp_box_lengths = item.trajectory.get_box_lengths().in_units_of(_unit.nanometers)._value
    tmp_box_angles = item.trajectory.get_box_angles().in_units_of(_unit.degrees)._value
    tmp_coordinates = item.trajectory.coordinates.in_units_of(_unit.nanometers)._value
    tmp_time=item.trajectory.time.in_units_of(_unit.picoseconds)._value
    tmp_item = _mdtraj_Trajectory(tmp_coordinates,tmp_item_topology, tmp_time,
            unitcell_lengths=tmp_box_lengths, unitcell_angles=tmp_box_angles)

    return tmp_item

def to_mdtraj_Topology(item, selection=None, syntaxis='MDTraj'):

    from .api_molmodmt_Topology import to_mdtraj_Topology as _to_mdtraj_Topology
    return _to_mdtraj_Topology(item.topology, selection=selection, syntaxis=syntaxis)

def to_pdb(item, filename=None, selection=None, syntaxis='MDTraj'):

    from molmodmt.native.io_molmod import to_pdb as _to_pdb

    return _to_pdb(item, filename=filename, selection=selection, syntaxis=syntaxis)

def select_with_MDTraj(item, selection=None, syntaxis='MDTraj'):
    from molmodmt import select
    return select(item.topology, selection=selection, syntaxis=syntaxis)

def extract_atom_indices(item, atom_indices, mode='keeping_selection'):

    if mode=='keeping_selection':
        return item.extract(atom_indices)
    elif mode=='removing_selection':
        from molmodmt.utils.atom_indices import complementary_atom_indices
        tmp_atom_indices = complementary_atom_indices(item, atom_indices)
        return item.extract(tmp_atom_indices)

def to_nglview(item):

    from .api_mdtraj_Trajectory import to_nglview as _mdtraj_to_nglview

    if type(item) in [list,tuple]:
        tmp_item = []
        for ii in item:
            tmp_item.append(to_mdtraj_Trajectory(ii))
    else:
        tmp_item = to_mdtraj_Trajectory(item)

    return _mdtraj_to_nglview(tmp_item)

def duplicate(item):

    from molmodmt.native.molmod import MolMod
    from .api_molmodmt_Trajectory import duplicate as duplicate_Trajectory
    from .api_molmodmt_Structure import duplicate as duplicate_Structure
    from .api_molmodmt_Topology import duplicate as duplicate_Topology
    from .api_molmodmt_Topography import duplicate as duplicate_Topography

    tmp_item = MolMod()
    tmp_item.trajectory = duplicate_Trajectory(item.trajectory)
    tmp_item.topology = duplicate_Topology(item.topology)
    tmp_item.structure = duplicate_Structure(item.structure)
    tmp_item.topography = duplicate_Topography(item.topography)

    return tmp_item

###### Get

## atom

def get_n_aminoacids_from_atom (item, indices=None, frame_indices=None):

    from .api_molmodmt_Topology import get_n_aminoacids_from_atom as _get
    return _get(item, indices=indices, frame_indices=frame_indices)

def get_n_nucleotides_from_atom (item, indices=None, frame_indices=None):

    from .api_molmodmt_Topology import get_n_nucleotides_from_atom as _get
    return _get(item, indices=indices, frame_indices=frame_indices)

def get_n_waters_from_atom (item, indices=None, frame_indices=None):

    from .api_molmodmt_Topology import get_n_waters_from_atom as _get
    return _get(item, indices=indices, frame_indices=frame_indices)

def get_n_ions_from_atom (item, indices=None, frame_indices=None):

    from .api_molmodmt_Topology import get_n_ions_from_atom as _get
    return _get(item, indices=indices, frame_indices=frame_indices)

def get_coordinates_from_atom(item, indices=None, frame_indices=None):

    from .api_molmodmt_Trajectory import get_coordinates_from_atom as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_bonded_atoms_from_atom(item, indices=None, frame_indices=None):

    from .api_molmodmt_Topology import get_bonded_atoms_from_atom as _get
    trajectory_indices = item.trajectory.file.atom_indices
    tmp_indices = [trajectory_indices[ii] for ii in indices]
    bonded_atoms_topology = _get(item.topology, indices=tmp_indices, frame_indices=frame_indices)
    traduction = { trajectory_indices[ii] : ii for ii in range(len(trajectory_indices)) }
    bonded_atoms = {}
    for ii_topology, ii_bonded_topology in bonded_atoms_topology.items():
        bonded_atoms[traduction[ii_topology]]=[traduction[jj] for jj in ii_bonded_topology]

    return bonded_atoms

def get_molecules_from_atom(item, indices=None, frame_indices=None):

    from .api_molmodmt_Topology import get_molecules_from_atom as _get
    trajectory_indices = item.trajectory.file.atom_indices
    tmp_indices = [trajectory_indices[ii] for ii in indices]
    molecules_topology = _get(item.topology, indices=tmp_indices, frame_indices=frame_indices)
    traduction = { trajectory_indices[ii] : ii for ii in range(len(trajectory_indices)) }
    molecules = []
    for tmp_molecule in molecules_topology:
        molecules.append([traduction[ii] for ii in tmp_molecule])

    return molecules

## residue

## chain

## system

def get_n_atoms_from_system(item, indices=None, frame_indices=None):

    from .api_molmodmt_Trajectory import get_n_atoms_from_system as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_n_residues_from_system(item, indices=None, frame_indices=None):

    from .api_molmodmt_Topology import get_n_residues_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_chains_from_system(item, indices=None, frame_indices=None):

    from .api_molmodmt_Topology import get_n_chains_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_aminoacids_from_system (item, indices=None, frame_indices=None):

    from .api_molmodmt_Topology import get_n_aminoacids_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_nucleotides_from_system (item, indices=None, frame_indices=None):

    from .api_molmodmt_Topology import get_n_nucleotides_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_waters_from_system (item, indices=None, frame_indices=None):

    from .api_molmodmt_Topology import get_n_waters_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_ions_from_system (item, indices=None, frame_indices=None):

    from .api_molmodmt_Topology import get_n_ions_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_molecules_from_system(item, indices=None, frame_indices=None):

    return len(get_molecules_from_system(item, indices=indices))

def get_n_frames_from_system(item, indices=None, frame_indices=None):

    from .api_molmodmt_Trajectory import get_n_frames_from_system as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_n_bonds_from_system(item, indices=None, frame_indices=None):

    from .api_molmodmt_Topology import get_n_bonds_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)


def get_masses_from_system(item, indices=None, frame_indices=None):

    from .api_molmodmt_Topology import get_masses_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_bonded_atoms_from_system(item, indices=None, frame_indices=None):

    from .api_molmodmt_Topology import get_bonded_atoms_from_atom as _get
    trajectory_indices = item.trajectory.file.atom_indices
    bonded_atoms_topology = _get(item.topology, indices=trajectory_indices, frame_indices=frame_indices)
    traduction = { trajectory_indices[ii] : ii for ii in range(len(trajectory_indices)) }
    bonded_atoms = {}
    for ii_topology, ii_bonded_topology in bonded_atoms_topology.items():
        bonded_atoms[traduction[ii_topology]]=[traduction[jj] for jj in ii_bonded_topology]

    return bonded_atoms

def get_bonds_from_system(item, indices=None, frame_indices=None):

    from .api_molmodmt_Topology import get_bonds_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_graph_from_system(item, indices=None, frame_indices=None):

    from .api_molmodmt_Topology import get_graph_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecules_from_system(item, indices=None, frame_indices=None):

    from .api_molmodmt_Topology import get_molecules_from_atom as _get
    trajectory_indices = item.trajectory.file.atom_indices
    molecules_topology = _get(item.topology, indices=trajectory_indices, frame_indices=frame_indices)
    traduction = { trajectory_indices[ii] : ii for ii in range(len(trajectory_indices)) }
    molecules = []
    for tmp_molecule in molecules_topology:
        molecules.append([traduction[ii] for ii in tmp_molecule])

    return molecules

def get_coordinates_from_system(item, indices=None, frame_indices=None):

    from .api_molmodmt_Trajectory import get_coordinates_from_system as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_box_from_system(item, indices=None, frame_indices=None):

    from .api_molmodmt_Trajectory import get_box_from_system as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_time_from_system(item, indices=None, frame_indices=None):

    from .api_molmodmt_Trajectory import get_time_from_system as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_box_shape_from_system(item, indices=None, frame_indices=None):

    return item.trajectory.box_shape

###### Set

def set_box_to_system(item, indices=None, frame_indices=None, value=None):

    item.trajectory.box = value
    pass

def set_coordinates_to_system(item, indices=None, frame_indices=None, value=None):

    item.trajectory.coordinates = value
    pass




