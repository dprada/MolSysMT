def to_openmm_Topology(item, selection='all', frame_indices='all', syntaxis='MolSysMT'):

    from molsysmt.tools.openff_Topology import is_openff_Topology
    from molsysmt.basic import convert

    if not is_openff_Topology(item):
        raise ValueError

    tmp_item = convert(item, to_form='openmm.Topology', selection=selection,
            frame_indices=frame_indices, syntaxis=syntaxis)

    return tmp_item

