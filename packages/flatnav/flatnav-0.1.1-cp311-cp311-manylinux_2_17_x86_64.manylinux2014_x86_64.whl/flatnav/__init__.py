import sys 
from ._core import (
    MetricType,
    data_type,
    __version__,
    __doc__
)

class _IndexModule:
    from ._core.index import (
        IndexL2Float,
        IndexIPFloat,
        IndexL2Uint8,
        IndexIPUint8,
        IndexL2Int8,
        IndexIPInt8,
        create,
    )

index = _IndexModule
sys.modules['flatnav.index'] = _IndexModule

__all__ = [
    'MetricType',
    'data_type',
    'index',
    '__version__',
    '__doc__'
]