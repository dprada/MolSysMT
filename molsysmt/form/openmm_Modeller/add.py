from .is_openmm_Modeller import is_openmm_Modeller
from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *

def add(to_item, item, check=True):

    if check:

        try:
            is_openmm_Modeller(item)
        except:
            raise WrongFormError('openmm.Modeller')

        try:
            is_openmm_Modeller(to_item)
        except:
            raise WrongFormError('openmm.Modeller')

    raise NotImplementedMethodError()
    pass
