__title__ = 'FastAPI Pundra'
__version__ = '0.0.3'
__author__ = 'Mostafa'

# Version synonym
VERSION = __version__

# Export main functionality
from fastapi_pundra.rest.validation import dto
from fastapi_pundra.rest.paginate import paginate
from fastapi_pundra.rest.helpers import app_path, the_query, the_sorting
from fastapi_pundra.rest.global_exception_handler import setup_exception_handlers
from fastapi_pundra.rest.exceptions import (
    BaseAPIException,
    ValidationException,
    NotFoundException,
    ItemNotFoundException,
    UnauthorizedException,
    ForbiddenException,
    BadRequestException,
    ConflictException,
    MethodNotAllowedException
)

__all__ = [
    'dto',
    'paginate',
    'app_path',
    'the_query',
    'the_sorting',
    'setup_exception_handlers',
    'BaseAPIException',
    'ValidationException',
    'NotFoundException',
    'ItemNotFoundException',
    'UnauthorizedException',
    'ForbiddenException',
    'BadRequestException',
    'ConflictException',
    'MethodNotAllowedException'
]