from typing import Any

GET = 'GET'
POST = 'POST'
PUT = 'PUT'
PATCH = 'PATCH'
DELETE = 'DELETE'
HEAD = 'HEAD'
OPTIONS = 'OPTIONS'

LOCATION = 'Location'
RETRY_AFTER = 'Retry-After'

EQUITY = 'EQUITY'

Alpha = Any
MultiAlpha = Any

Region = Any
Delay = Any
Universe = Any
InstrumentType = Any
Category = Any
FieldType = Any
DatasetsOrder = Any
FieldsOrder = Any
Status = Any
AlphaType = Any
Language = Any
Color = Any
Neutralization = Any
UnitHandling = Any
NanHandling = Any
Pasteurization = Any
AlphasOrder = Any

from . import auto_auth_session
from . import filter_range
from . import wqb_session
from . import wqb_urls

__all__ = (
    auto_auth_session.__all__
    + filter_range.__all__
    + wqb_session.__all__
    + wqb_urls.__all__
)

from .auto_auth_session import *
from .filter_range import *
from .wqb_session import *
from .wqb_urls import *
