from molsysmt._private.digestion import digest

@digest(form='openmm.Topology')
def to_openmm_System(item, atom_indices='all', forcefield=None, water_model=None, implicit_solvent=None,
        non_bonded_method='no cutoff', switch_distance=None):

    forcefield = molecular_mechanics.to_openmm_ForceField()
    system_parameters = molecular_mechanics.get_openmm_System_parameters()
    tmp_item = forcefield.createSystem(item, **parameters)

    if molecular_mechanics.use_dispersion_correction or molecular_mechanics.ewald_error_tolerance:
        forces = {ii.__class__.__name__ : ii for ii in tmp_item.getForces()}
    if molecular_mechanics.use_dispersion_correction:
        forces['NonbondedForce'].setUseDispersionCorrection(True)
    if molecular_mechanics.ewald_error_tolerance:
        forces['NonbondedForce'].setEwaldErrorTolerance(molecular_mechanics.ewald_error_tolerance)

    return tmp_item

def _to_openmm_System(item, molecular_system, atom_indices='all', structure_indices='all'):

    from molsysmt.basic import convert

    molecular_mechanics = convert(molecular_system, to_form='molsysmt.MolecularMechanics')
    forcefield = molecular_mechanics.to_openmm_ForceField()
    system_parameters = molecular_mechanics.get_openmm_System_parameters()
    return to_openmm_System(item, atom_indices=atom_indices,
                                            forcefield=forcefield, parameters=parameters)

