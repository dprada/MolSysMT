from .is_openmm_Modeller import is_openmm_Modeller
from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *

def append_structures(item, step=None, time=None, coordinates=None, box=None, check=True):

    if check:

        try:
            is_openmm_Modeller(item)
        except:
            raise WrongFormError('openmm.Modeller')

        try:
            step = digest_step(step)
        except:
            raise WrongStepError()

        try:
            time = digest_time(time)
        except:
            raise WrongTimeError()

        try:
            coordinates = digest_coordinates(coordinates)
        except:
            raise WrongCoordinatesError()

        try:
            box = digest_box(box)
        except:
            raise WrongBoxError()

    raise NotImplementedMethodError()
    pass

