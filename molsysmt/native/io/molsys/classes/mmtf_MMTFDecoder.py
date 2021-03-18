
def from_mmtf_MMTFDecoder(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    from molsysmt.native.molsys import MolSys
    from molsysmt.native.io.topology.classes import from_mmtf_MMTFDecoder as molsysmt_Topology_from_mmtf_MMTFDecoder
    from molsysmt.native.io.trajectory.classes import from_mmtf_MMTFDecoder as molsysmt_Trajectory_from_mmtf_MMTFDecoder

    tmp_item = MolSys()
    tmp_item.topology = molsysmt_Topology_from_mmtf_MMTFDecoder(item, molecular_system=molecular_system, atom_indices=atom_indices, frame_indices=frame_indices)
    tmp_item.trajectory = molsysmt_Trajectory_from_mmtf_MMTFDecoder(item, molecular_system=molecular_system, atom_indices=atom_indices, frame_indices=frame_indices)
    return tmp_item

