from ..exceptions import WrongElementError

elements = [
    'atom',
    'group',
    'component',
    'chain',
    'molecule',
    'entity',
    'system',
    'bond',
]

elements_from_plural = {
    'atoms': 'atom',
    'groups': 'group',
    'residue': 'group',
    'residues': 'group',
    'components': 'component',
    'chains': 'chain',
    'molecules': 'molecule',
    'entities': 'entity',
    'systems': 'system',
    'bonds': 'bond',
}


def digest_element(element):
    """ Helper function to check an element type. Raises a BadCallError
        if the element type is not supported by MolSysMT.

        Parameters
        ----------
        element : str
            The name of the element.

        Raises
        ------
        BadCallError
            If the element is not a string or its name is not valid.
    """
    if isinstance(element, str):
        element_name_lower = element.lower()
        if element_name_lower in elements_from_plural:
            return elements_from_plural[element_name_lower]
        if element_name_lower not in elements:
            raise WrongElementError("wrong element name")
        return element_name_lower

    raise WrongElementError("element is not a string")
