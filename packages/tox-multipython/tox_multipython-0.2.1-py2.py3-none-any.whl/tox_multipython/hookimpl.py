import os
import re
import sys
from subprocess import check_output

import pluggy

try:
    from typing import TYPE_CHECKING
except ImportError:
    TYPE_CHECKING = False

if TYPE_CHECKING:
    # ruff: noqa: F401 = Union is actually used for typing below
    from typing import Union

# debug logging

DEBUG = bool(os.environ.get('MULTIPYTHON_DEBUG', False))
if DEBUG:
    try:
        from loguru import logger
    except ImportError:
        pass


def debug(msg):  # type: (str) -> None
    if DEBUG:
        logger.debug(msg)


hookimpl = pluggy.HookimplMarker('tox')

RX = (
    re.compile(r'^(?P<impl>py)(?P<maj>[23])(?P<min>[0-9][0-9]?)$'),
    re.compile(r'^(?P<impl>py)(?P<maj>3)(?P<min>[0-9][0-9])(?P<suffix>t)$'),
)


@hookimpl
def tox_get_python_executable(envconfig):  # type: ignore
    """Return a python executable for the given python base name."""
    debug('Requested Python executable: {data}'.format(data=envconfig.__dict__))
    path = None
    for rx in RX:
        match = rx.match(envconfig.envname)
        if match is not None:
            debug('Candidate tag: {tag}'.format(tag=envconfig.envname))
            path = get_python_path(envconfig.envname)
            break
    if path:
        debug('Found Python executable: {path}'.format(path=path))
        return path
    else:
        debug('Failed to propose Python executable')
        return None


def get_python_path(tag):  # type: (str) -> Union[str, None]
    # get path
    try:
        # ruff: noqa: S603 = allow check_output with arbitrary cmdline
        # ruff: noqa: S607 = py is on path, specific location is not guaranteed
        out = check_output(['py', 'bin', '--path', tag])
        enc = sys.getfilesystemencoding()
        path = (out.decode() if enc is None else out.decode(enc)).strip()
        if not path:
            return None
    except Exception:
        return None
    return path
