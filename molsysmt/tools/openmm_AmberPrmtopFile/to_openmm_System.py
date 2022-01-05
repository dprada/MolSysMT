def to_openmm_System(item, selection='all', frame_indices='all', syntaxis='MolSysMT'):

    from molsysmt.tools.openmm_AmberPrmtopFile import is_openmm_AmberPrmtopFile
    from molsysmt.basic import convert

    if not is_openmm_AmberPrmtopFile(item):
        raise ValueError

    tmp_item = convert(item, to_form='openmm.System', selection=selection,
            frame_indices=frame_indices, syntaxis=syntaxis)

    return tmp_item

