def to_file_mol2(item, selection='all', model_indices='all', output_filename=None, syntaxis='MolSysMT'):

    from molsysmt.tools.string_pdb_text import is_string_pdb_text
    from molsysmt.tools.file_mol2 import is_file_mol2
    from molsysmt.basic import convert

    if not is_string_pdb_text(item):
        raise ValueError

    if output_filename is None:
        raise ValueError

    if not is_file_mol2(output_filename):
        raise ValueError

    tmp_item = convert(item, output_filename, selection=selection, frame_indices=model_indices, syntaxis=syntaxis)

    return tmp_item
