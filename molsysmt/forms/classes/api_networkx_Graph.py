from molsysmt._private_tools.exceptions import *
from molsysmt.forms.common_gets import *
import numpy as np
from networkx import Graph as _networkx_Graph
from molsysmt.molecular_system import molecular_system_components

form_name='networkx.Graph'

is_form={
    _networkx_Graph : form_name
}

info=["",""]

has = molecular_system_components.copy()
for ii in ['elements', 'bonds']:
    has[ii]=True

def select_with_MDTraj(item, selection):

    raise NotImplementedError

def to_networkx_Graph(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    if (atom_indices is 'all') and (frame_indices is 'all'):
        tmp_item = item.copy()
        tmp_molecular_system = molecular_system.combine_with_items(tmp_item)
    else:
        tmp_item = item.subgraph(atom_indices).copy()
        tmp_molecular_system = molecular_system.combine_with_items(tmp_item, atom_indices=atom_indices, frame_indices=frame_indices)

    return tmp_item, tmp_molecular_system

def add(item, from_item, atom_indices='all', frame_indices='all'):

    raise NotImplementedError

def append_frames(item, step=None, time=None, coordinates=None, box=None):

    raise NotImplementedError

###### Get

## system


