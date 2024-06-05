"""Module providing customized error handling exceptions"""
class AttributeNotFoundError(Exception):
    """Custom helper exception to handle cases when product specific attributes
    passed as filtering argument do not exist in product's metadata.
    """
    def __init__(self, error: Exception) -> None:
        self.message = f"'{error.args[0]}' is not found in the product attributes."
        super().__init__(self.message)


class AuthorizationError(Exception):
    pass


class QueryError(Exception):
    pass


class DownloadError(Exception):
    pass


class FilterByAttributeError(Exception):
    """Raised when filtering products locally by attributes fails."""
    pass