
__github_web__ = 'https://github.com/uibcdf/MolSysMT'
__github_issues_web__ = __github_web__ + '/issues'
api_doc = ''


class MolSysNotImplementedError(ValueError):
    """ Base class for not implemented errors. """

    def __init__(self, message=None):
        if message is None:
            message = ""

        message += (
            "The method has not been implemented yet. "
            f" Check {api_doc} for more information. "
            f"Write a new issue in {__github_issues_web__} asking for its implementation."
        )
        super().__init__(message)


class NotImplementedConversionError(MolSysNotImplementedError):
    pass


class NotImplementedMethodError(MolSysNotImplementedError):
    pass


class NotImplementedSyntaxisError(MolSysNotImplementedError):
    pass


class NotImplementedConversionError(MolSysNotImplementedError):
    pass


class LibraryNotFoundError(MolSysNotImplementedError):
    """ Exception raised when a library required by the user is not found.

        Some libraries are not considered as dependencies by Sabueso. These libraries are required if
        the user choose to execute a method with a not default engine. In this case, the user hat to
        install it previous. It that's not the case, the method will raise these exceptions suggesting
        the manual installation.
    """

    def __init__(self, library):

        message = (
            f"The python library {library} was not found. "
            f"If you still need help, open a new issue in {__github_issues_web__}."
        )

        super().__init__(message)