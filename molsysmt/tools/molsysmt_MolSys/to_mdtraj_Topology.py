def to_mdtraj_Topology(item, atom_indices='all', check_form=True):

    if check_form:
        from molsysmt.tools.molsysmt_MolSys import is_molsysmt_MolSys
        from molsysmt._private_tools.exceptions import ItemWithWrongForm
        if not is_molsysmt_MolSys(item):
            raise ItemWithWrongForm('molsysmt.MolSys')

    from molsysmt.tools.molsysmt_MolSys import to_molsysmt_Topology as molsysmt_MolSys_to_molsysmt_Topology
    from molsysmt.tools.molsysmt_Topology import to_mdtraj_Topology as molsysmt_Topology_to_mdtraj_Topology

    tmp_item = molsysmt_MolSys_to_molsysmt_Topology(item, check_form=False)
    tmp_item = molsysmt_Topology_to_mdtraj_Topology(tmp_item, atom_indices=atom_indices, check_form=False)

    return tmp_item

