def to_file_pdb(item, selection='all', structure_indices='all', output_filename=None, syntaxis='MolSysMT'):

    from molsysmt.tools.file_prmtop import is_file_prmtop
    from molsysmt.tools.file_pdb import is_file_pdb
    from molsysmt.basic import convert

    if not is_file_prmtop(item):
        raise ValueError

    if output_filename is None:
        raise ValueError

    if not is_file_pdb(output_filename):
        raise ValueError

    tmp_item = convert(item, output_filename, selection=selection, structure_indices=structure_indices, syntaxis=syntaxis)

    return tmp_item
