
class Group:

    def __init__(self, id=None, index=None, name=None, type=None):

        self.id = id
        self.index = index
        self.name = name
        self.type = type

        self.atom = []
        self.n_atoms = 0

        self.component = None
        self.chain = None
        self.molecule = None
        self.entity = None
        self.bioassembly = None
