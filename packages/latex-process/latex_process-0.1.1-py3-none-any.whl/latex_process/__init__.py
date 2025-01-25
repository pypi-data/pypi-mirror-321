from .processor import LatexProcess

__all__ = ['LatexProcess', 'LatexProcessError']

class LatexProcessError(Exception):
    """Custom exception class for LatexProcess errors"""
    pass
