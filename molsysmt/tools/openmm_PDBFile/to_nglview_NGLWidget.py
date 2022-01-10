def to_nglview_NGLWidget(item, selection='all', frame_indices='all', syntaxis='MolSysMT'):

    from molsysmt.tools.openmm_PDBFile import is_openmm_PDBFile
    from molsysmt.basic import convert

    if not is_openmm_PDBFile(item):
        raise ValueError

    tmp_item = convert(item, to_form='nglview.NGLWidget', selection=selection,
            frame_indices=frame_indices, syntaxis=syntaxis)

    return tmp_item
