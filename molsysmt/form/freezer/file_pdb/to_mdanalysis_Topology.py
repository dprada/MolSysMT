def to_mdanalysis_Topology(item, atom_indices='all', structure_indices='all', check=True):

    if check:
        from molsysmt.tools.file_pdb.is_file_pdb import _checking_form
        _checking_form(item, check=check)

    from molsysmt.tools.file_pdb import to_mdanalysis_topology_PDBParser as file_pdb_to_mdanalysis_topology_PDBParser
    from molsysmt.tools.mdanalysis_topology_PDBParser import to_mdanalysis_Topology as mdanalysis_topology_PDBParser_to_mdanalysis_Topology
    from molsysmt.tools.mdanalysis_Topology import extract

    tmp_item = file_pdb_to_mdanalysis_topology_PDBParser(item)
    tmp_item = mdanalysis_topology_PDBParser_to_mdanalysis_Topology(tmp_item, structure_indices=structure_indices)
    tmp_item = extract(tmp_item, atom_indices=atom_indices)

    return tmp_item
