def to_openmm_System(item, selection='all', frame_indices='all', syntaxis='MolSysMT'):

    from molsysmt.tools.openmm_Context import is_openmm_Context
    from molsysmt.basic import convert

    if not is_openmm_Context(item):
        raise ValueError

    tmp_item = convert(item, to_form='openmm.System', selection=selection,
            frame_indices=frame_indices, syntaxis=syntaxis)

    return tmp_item

