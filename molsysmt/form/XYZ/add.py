from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='XYZ', to_form='XYZ')
def add(to_item, item):

    raise NotImplementedMethodError()
