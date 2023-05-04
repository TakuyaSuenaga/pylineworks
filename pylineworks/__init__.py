from pkg_resources import get_distribution, DistributionNotFound

from pylineworks.core.api import Api as api

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    pass
