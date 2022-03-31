from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *
import numpy as np
from molsysmt.basic import select

def get_covalent_chains(molecular_system, chain=None, selection='all', syntaxis='MolSysMT',
        check=True):

    if check:
        from molsysmt.tools.molecular_system import is_molecular_system
        if not is_molecular_system(molecular_system):
            raise MolecularSystemNeededError()

    from molsysmt.topology.get_bondgraph import get_bondgraph

    if selection is 'all':
        mask = None
    else:
        mask = select(molecular_system, selection=selection, syntaxis=syntaxis, check=False)

    chain_atom_indices = []

    for sel_in_chain in chain:
        atom_indices = select(molecular_system, selection=sel_in_chain, mask=mask)
        chain_atom_indices.append(atom_indices)

    atom_indices = np.sort(np.unique(np.concatenate(chain_atom_indices)))

    graph = get_bondgraph(molecular_system, selection=atom_indices, nodes_name='atom_index',
            check=False)

    n_slaves = len(chain_atom_indices)

    output = [[ii] for ii in chain_atom_indices[0]]
    for slave_index in range(n_slaves):
        chain_atom_indices[slave_index] = set(chain_atom_indices[slave_index])

    for slave_index in range(1,n_slaves):
        slave_preindex=slave_index-1
        tmp_output=output.copy()
        output=[]
        for chain in tmp_output:
            for ii in graph.neighbors(chain[slave_preindex]):
                if ii in chain_atom_indices[slave_index]:
                    new_chain = chain.copy()
                    new_chain.append(ii)
                    output.append(new_chain)
    del(graph)

    return np.array(output, dtype=int)

