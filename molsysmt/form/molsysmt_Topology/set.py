from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *
from .is_molsysmt_Topology import is_molsysmt_Topology
from molsysmt import puw

###### Set

## Atom

def set_atom_name_to_atom(item, indices='all', structure_indices='all', value=None, check=True):

    if check:

        try:
            is_molsysmt_Topology(item)
        except:
            raise WrongFormError('molsysmt.Topology')

        try:
            indices = digest_indices(indices)
        except:
            raise WrongIndicesError()

        try:
            structure_indices = digest_structure_indices(structure_indices)
        except:
            raise WrongStructureIndicesError()

    item.atoms_dataframe.loc[indices, 'atom_name']=value

    pass

##### System
#
#def set_box_to_system(item, structure_indices='all', value=None, check=True):
#
#    if check:
#
#        try:
#            is_molsysmt_Topology(item)
#        except:
#            raise WrongFormError('molsysmt.Topology')
#
#        try:
#            structure_indices = digest_structure_indices(structure_indices)
#        except:
#            raise WrongStructureIndicesError()
#
#        try:
#            box = digest_box(value)
#        except:
#            raise WrongStructureIndicesError()
#
#    box = puw.convert(box, to_unit='nm', to_form='openmm.unit')
#
#    print(np.shape(box))
#
#    pass

