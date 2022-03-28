def to_pdbfixer_PDBFixer(item, selection='all', structure_indices='all', syntaxis='MolSysMT'):

    from molsysmt.tools.mdtraj_Trajectory import is_mdtraj_Trajectory
    from molsysmt.basic import convert

    if not is_mdtraj_Trajectory(item):
        raise ValueError

    tmp_item = convert(item, to_form='pdbfixer.PDBFixer', selection=selection,
            structure_indices=structure_indices, syntaxis=syntaxis)

    return tmp_item
