from molsysmt.attribute.attributes import attributes as _all_attributes

attributes = {ii:False for ii in _all_attributes}

attributes['atom_index'] = True
attributes['atom_id'] = True
attributes['atom_name'] = True
attributes['atom_type'] = True
attributes['group_index'] = True
attributes['group_id'] = True
attributes['group_name'] = True
attributes['group_type'] = True
attributes['component_index'] = True
attributes['component_id'] = True
attributes['component_name'] = True
attributes['component_type'] = True
attributes['molecule_index'] = True
attributes['molecule_id'] = True
attributes['molecule_name'] = True
attributes['molecule_type'] = True
attributes['chain_index'] = True
attributes['chain_id'] = True
attributes['chain_name'] = True
attributes['chain_type'] = True
attributes['entity_index'] = True
attributes['entity_id'] = True
attributes['entity_name'] = True
attributes['entity_type'] = True
attributes['bond_index'] = True
attributes['bond_id'] = True
attributes['bond_name'] = True
attributes['bond_type'] = True
attributes['bond_order'] = True
attributes['bonded_atoms'] = True

del(_all_attributes)
