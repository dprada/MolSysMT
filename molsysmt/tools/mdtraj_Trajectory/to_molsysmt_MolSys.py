def to_molsysmt_MolSys(item, atom_indices='all', frame_indices='all'):

    from molsysmt._private_tools.exceptions import ItemWithWrongForm
    from molsysmt.tools.mdtraj_Trajectory import is_mdtraj_Trajectory
    from molsysmt.native.molsys import MolSys
    from molsysmt.tools.mdtraj_Trajectory import to_molsysmt_Topology as mdtraj_Trajectory_to_molsysmt_Topology
    from molsysmt.tools.mdtraj_Trajectory import to_molsysmt_Trajectory as mdtraj_Trajectory_to_molsysmt_Trajectory
    from molsysmt.basic import convert

    if not is_mdtraj_Trajectory(item):
        raise ItemWithWrongForm('mdtraj.Trajectory')

    tmp_item = MolSys()
    tmp_item.topology = mdtraj_Trajectory_to_molsysmt_Topology(item, atom_indices=atom_indices)
    tmp_item.trajectory = mdtraj_Trajectory_to_molsysmt_Trajectory(item, atom_indices=atom_indices, frame_indices=frame_indices)

    return tmp_item

