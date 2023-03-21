from molsysmt._private.digestion import digest

@digest(form='pdbfixer.PDBFixer')
def to_molsysmt_Structures(item, atom_indices='all', structure_indices='all'):

    from molsysmt.native.structures import Structures
    from . import get_coordinates_from_atom, get_box_from_system

    tmp_item = Structures()
    coordinates = get_coordinates_from_atom(item, indices=atom_indices)
    box = get_box_from_system(item)

    tmp_item.append_structures(coordinates=coordinates, box=box)

    return tmp_item
