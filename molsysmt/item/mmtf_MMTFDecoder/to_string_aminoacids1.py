from molsysmt._private.digestion import digest_item, digest_group_indices

def to_string_aminoacids1(item, group_indices='all', check=True):

    if check:

        digest_item(item, 'file:mmtf.MMTFDecoder')
        group_indices = digest_group_indices(atom_indices)

    from . import to_molsysmt_Topology
    from ..molsysmt_Topology import to_string_aminoacids1 as molsysmt_Topology_to_string_aminoacids1

    tmp_item = to_molsysmt_Topology(item, check=False)
    tmp_item = molsysmt_Topology_to_string_aminoacids1(tmp_item, group_indices=group_indices, check=False)

    return tmp_item
