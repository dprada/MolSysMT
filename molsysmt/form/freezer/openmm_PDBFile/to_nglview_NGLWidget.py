def to_nglview_NGLWidget(item, selection='all', structure_indices='all', syntaxis='MolSysMT'):

    from molsysmt.tools.openmm_PDBFile import is_openmm_PDBFile
    from molsysmt.basic import convert

    if not is_openmm_PDBFile(item):
        raise ValueError

    tmp_item = convert(item, to_form='nglview.NGLWidget', selection=selection,
            structure_indices=structure_indices, syntaxis=syntaxis)

    return tmp_item
