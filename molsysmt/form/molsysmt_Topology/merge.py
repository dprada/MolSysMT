from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *
from .is_molsysmt_Topology import is_molsysmt_Topology

def merge(item_1, item_2):

    if check:

        try:
            is_molsysmt_Topology(item_1)
        except:
            raise WrongFormError('molsysmt.Topology')

        try:
            is_molsysmt_MolSys(item_2)
        except:
            raise WrongFormError('molsysmt.Topology')


    raise NotImplementedError
