from os.path import basename as _basename
from pdbfixer.pdbfixer import PDBFixer as _pdbfixer_PDBFixer

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _pdbfixer_PDBFixer : form_name
}

## Methods

def to_nglview(item):

    from .api_mdtraj_Trajectory import to_nglview as _mdtraj_to_nglview
    tmp_item = to_mdtraj(item)
    return _mdtraj_to_nglview(tmp_item)

def to_aminoacids3_seq(item):

    return ''.join([ r.name for r in item.topology.residues() ])

def to_aminoacids1_seq(item):

    from molmodmt.forms.seqs.api_aminoacids3 import to_aminoacids1_seq as _aminoacids3_to_aminoacids1
    tmp_item = to_aminoacids3_seq(item)
    tmp_item = _aminoacids3_to_aminoacids1(tmp_item)
    del(_aminoacids3_to_aminoacids1)
    return tmp_item

def to_biopython_Seq(item):

    from molmodmt.forms.seqs.api_aminoacids1 import to_biopython_Seq as _aminoacids1_to_biopython_Seq
    tmp_item = to_aminoacids1_seq(item)
    tmp_item = _aminoacids1_to_biopython_Seq(tmp_item)
    del(_aminoacids1_to_biopython_Seq)
    return tmp_item

def to_biopython_SeqRecord(item):

    from molmodmt.forms.seqs.api_aminoacids1 import to_biopython_SeqRecord as _aminoacids1_to_biopython_SeqRecord
    tmp_item = to_aminoacids1_seq(item)
    tmp_item = _aminoacids1_to_biopython_SeqRecord(tmp_item)
    del(_aminoacids1_to_biopython_SeqRecord)
    return tmp_item


def to_mdtraj_Topology(item):

    from mdtraj.core.topology import Topology as _mdtraj_Topology
    tmp_form = to_openmm_Topology(item)
    tmp_form = _mdtraj_Topology.from_openmm(tmp_form)
    del(_mdtraj_Topology)
    return tmp_form

def to_mdtraj_Trajectory(item, selection=None, syntaxis='mdtraj'):

    import simtk.unit as _unit
    from molmodmt import extract as _extract
    from .api_openmm_Topology import to_mdtraj_Topology as _openmm_Topology_to_mdtraj_Topology
    from mdtraj.core.trajectory import Trajectory as _mdtraj_Trajectory

    tmp_item_topol = _openmm_Topology_to_mdtraj_Topology(item.topology)
    tmp_item = _mdtraj_Trajectory(item.positions/_unit.nanometers, tmp_item_topol)
    tmp_item = _extract(tmp_item, selection=selection, syntaxis=syntaxis)
    return tmp_item

def to_mdtraj(item, selection=None, syntaxis='mdtraj'):

    return to_mdtraj_Trajectory(item, selection=selection, syntaxis=syntaxis)

def to_openmm_Modeller(item, selection=None, syntaxis='mdtraj'):

    from simtk.openmm.app import Modeller as _openmm_app_Modeller
    return _openmm_app_Modeller(item.topology, item.positions)

def to_openmm_Topology(item, selection=None, syntaxis='mdtraj'):

    return item.topology

def to_openmm_Positions(item, selection=None, syntaxis='mdtraj'):

    return item.positions

def to_yank_Topography(item):

    from yank import Topography as _yank_Topography
    tmp_form = to_openmm_Topology(item)
    tmp_form = _yank_Topography(tmp_form)
    del(_yank_Topography)
    return tmp_form

def to_parmed_Structure(item):

    from .api_openmm_Topology import to_parmed_Structure as _openmm_Topology_to_parmed_Structure
    tmp_form = to_openmm_Topology(item)
    tmp_form = _openmm_Topology_to_parmed_Structure(tmp_form)
    del(_openmm_Topology_to_parmed_Structure)
    return tmp_form

def to_pdbfixer(item, selection=None, syntaxis="mdtraj"):
    return item

def to_pdb(item, filename=None, selection=None, syntaxis="mdtraj"):

    from simtk.openmm.app import PDBFile as _openmm_app_PDBFILE
    return _openmm_app_PDBFILE.writeFile(item.topology, item.positions, open(filename, 'w'), keepIds=True)

def select_with_MDTraj(item, selection):

    tmp_form=to_mdtraj(item)
    tmp_sel=tmp_form.topology.select(selection)
    del(tmp_form)
    return tmp_sel

def extract_atom_indices(item, atom_indices, mode='keeping_selection'):

    from molmodmt import convert, extract
    tmp_item = convert(item, 'openmm.Modeller')
    tmp_item = extract(tmp_item, atom_indices, mode=mode)
    tmp_item = convert(tmp_item, 'pdbfixer.PDBFixer')
    return tmp_item


def duplicate(item):

    from os import remove
    from molmodmt import convert
    from molmodmt.utils.pdb import tmp_pdb_filename
    tmp_file = tmp_pdb_filename()
    convert(item, tmp_file)
    tmp_item = convert(tmp_file,'pdbfixer.PDBFixer')
    remove(tmp_file)
    return tmp_item

##### Get

## Atom

def get_n_atoms_from_atom (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_n_atoms_from_atom as _get
    _get(item.topology, indices=indices)

def get_atom_name_from_atom (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_atom_name_from_atom as _get
    _get(item.topology, indices=indices)

def get_atom_index_from_atom (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_atom_index_from_atom as _get
    _get(item.topology, indices=indices)

def get_atom_id_from_atom (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_atom_id_from_atom as _get
    _get(item.topology, indices=indices)

def get_atom_type_from_atom (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_atom_type_from_atom as _get
    _get(item.topology, indices=indices)

def get_n_residues_from_atom (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_n_residues_from_atom as _get
    _get(item.topology, indices=indices)

def get_residue_name_from_atom (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_n_residue_from_atom as _get
    _get(item.topology, indices=indices)

def get_residue_index_from_atom (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_residue_index_from_atom as _get
    _get(item.topology, indices=indices)

def get_residue_id_from_atom (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_residue_id_from_atom as _get
    _get(item.topology, indices=indices)

def get_chain_index_from_atom (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_chain_index_from_atom as _get
    _get(item.topology, indices=indices)

def get_chain_id_from_atom (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_chain_id_from_atom as _get
    _get(item.topology, indices=indices)

def get_n_aminoacids_from_atom (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_n_aminoacids_from_atom as _get
    _get(item.topology, indices=indices)

def get_n_nucleotides_from_atom (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_n_nucleotides_from_atom as _get
    _get(item.topology, indices=indices)

def get_n_waters_from_atom (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_n_waters_from_atom as _get
    _get(item.topology, indices=indices)

def get_n_ions_from_atom (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_n_ions_from_atom as _get
    _get(item.topology, indices=indices)

def get_mass_from_atom (item, indices=None, frame_indices=None):

    from molmodmt import get_mass as _get
    return _get(item, indices=indices)

def get_net_mass_from_atom (item, indices=None, frame_indices=None):

    from molmodmt import get_net_mass as _get
    return _get(item, indices=indices)

def get_charge_from_atom (item, indices=None, frame_indices=None):

    from molmodmt import get_charge as _get
    return _get(item, indices=indices)
def get_net_charge_from_atom (item, indices=None, frame_indices=None):

    from molmodmt import get_net_charge as _get
    return _get(item, indices=indices)

def get_n_degrees_of_freedom_from_atom (item, indices=None, frame_indices=None):

    from molmodmt import get_degrees_of_freedom_charge as _get
    return _get(item, indices=indices)

def get_molecule_type_from_atom (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_molecule_type_from_atom as _get
    return _get(item, indices=indices)

def get_coordinates_from_atom (item, indices=None, frame_indices=None):

    from .api_openmm_Positions import get_coordinates_from_atom as _get
    return _get(item, indices=indices)

## residue

def get_n_residues_from_residue (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_n_residues_from_residue as _get
    return _get(item, indices=indices)

def get_residue_name_from_residue (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_residue_name_from_residue as _get
    return _get(item, indices=indices)

def get_residue_index_from_residue (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_residue_index_from_residue as _get
    return _get(item, indices=indices)

def get_residue_id_from_residue (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_residue_id_from_residue as _get
    return _get(item, indices=indices)

def get_chain_index_from_residue (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_chain_index_from_residue as _get
    return _get(item, indices=indices)

def get_chain_id_from_residue (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_chain_id_from_residue as _get
    return _get(item, indices=indices)

def get_molecule_type_from_residue (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_molecule_type_from_residue as _get
    return _get(item, indices=indices)

## chain

def get_chain_index_from_chain (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_chain_index_from_chain as _get
    return _get(item, indices=indices)

def get_chain_id_from_chain (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_chain_id_from_chain as _get
    return _get(item, indices=indices)

def get_molecule_type_from_chain (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_molecule_type_from_chain as _get
    return _get(item, indices=indices)

## system

def get_n_atoms_from_system (item, indices=None, frame_indices=None):

    from .api_openmm_Topology import get_n_atoms_from_system as _get
    return _get(item, indices=indices)

def get_charge_from_system (item, indices=None, frame_indices=None):

    from molmodmt import get_charge as _get
    return _get(item, indices=indices)

def get_net_charge_from_system (item, indices=None, frame_indices=None):

    from molmodmt import get_net_charge as _get
    return _get(item, indices=indices)

def get_n_degrees_of_freedom_from_system (item, indices=None, frame_indices=None):

    from molmodmt import get_degrees_of_freedom as _get
    return _get(item, indices=indices)


##### Set

def set_name_to_residue(item, indices=None, frame_indices=None, value=None):
    for residue in tmp_item.topology.residues():
        if residue.index in indices:
            name = value[np.where(indices == residue.index)[0][0]]
            residue.name = name
    for bond in tmp_item.topology.bonds():
        for ii in [0,1]:
            if bond[ii].residue.index in set_indices:
                name = kwargs[option][np.where(array_indices == bond[ii].residue.index)[0][0]]
                bond[ii].residue.name = name
