def to_molsysmt_MolecularMechanicsDict(item, selection='all', frame_indices='all', syntaxis='MolSysMT'):

    from molsysmt.tools.molsysmt_MolecularMechanics import is_molsysmt_MolecularMechanics
    from molsysmt.basic import convert

    if not is_molsysmt_MolecularMechanics(item):
        raise ValueError

    tmp_item = convert(item, to_form='molsysmt.MolecularMechanicsDict', selection=selection,
            frame_indices=frame_indices, syntaxis=syntaxis)

    return tmp_item
