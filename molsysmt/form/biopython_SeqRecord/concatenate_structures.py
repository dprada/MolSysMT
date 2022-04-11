from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *

def concatenate_structures(item, step=None, time=None, coordinates=None, box=None, check=True):

    if check:

        digest_item(item, 'biopython.SeqRecord')
        step = digest_step(step)
        time = digest_time(time)
        coordinates = digest_coordinates(coordinates)
        box = digest_box(box)

    raise NotImplementedMethodError()

