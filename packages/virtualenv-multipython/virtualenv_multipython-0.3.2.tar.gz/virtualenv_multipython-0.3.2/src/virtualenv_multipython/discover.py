import os
import re
from subprocess import check_output
import sys

try:
    from typing import TYPE_CHECKING, Union
except ImportError:
    TYPE_CHECKING = False

# ruff: noqa: F401
if TYPE_CHECKING:
    import argparse  # type: ignore[unused-ignore]

from virtualenv.discovery.builtin import Builtin  # type: ignore
from virtualenv.discovery.discover import Discover  # type: ignore
from virtualenv.discovery.py_info import PythonInfo  # type: ignore

# debug logging

DEBUG = bool(os.environ.get('MULTIPYTHON_DEBUG', False))
if DEBUG:
    try:
        from loguru import logger
    except ImportError:
        pass


RX = (
    re.compile(r'^(?P<impl>py)(?P<maj>[23])(?P<min>[0-9][0-9]?)$'),
    re.compile(r'^(?P<impl>py)(?P<maj>3)(?P<min>[0-9][0-9])(?P<suffix>t)$'),
)


class MultiPython(Discover):  # type: ignore[misc]
    def __init__(self, options):  # type: (argparse.Namespace) -> None
        super(MultiPython, self).__init__(options)
        self.try_first_with = options.try_first_with
        self.python = options.python
        if DEBUG:
            data = options.__dict__
            logger.debug('Created MultiPython with options: {data}'.format(data=data))
            self.builtin = Builtin(options)

    @classmethod
    def add_parser_arguments(cls, parser):  # type: (argparse.ArgumentParser) -> None
        Builtin.add_parser_arguments(parser)

    def run(self):  # type: () -> Union[PythonInfo, None]
        requests = self.try_first_with + self.python

        ret = None
        for python in requests:
            if os.path.isabs(python) and os.path.exists(python):
                if DEBUG:
                    logger.debug('Candidate path: {python}'.format(python=python))
                ret = self.get_path_info(python)
            else:
                for rx in RX:
                    if rx.match(python):
                        if DEBUG:
                            logger.debug(
                                'Candidate tag: {python}'.format(python=python)
                            )
                        ret = self.get_tag_info(python)
            if ret:
                break

        if DEBUG:
            data = self.builtin.run()
            logger.debug('Builtin discovery result: {data}'.format(data=data))
            logger.debug('Returning result: {ret}')
        return ret

    def get_path_info(self, path):  # type: (str) -> Union[PythonInfo, None]
        try:
            return PythonInfo.from_exe(path, resolve_to_host=False)
        except Exception:
            if DEBUG:
                logger.exception(
                    'Failed to get PythoInfo for path "{path}"'.format(path=path)
                )
            return None

    def get_tag_info(self, tag):  # type: (str) -> Union[PythonInfo, None]
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
            if DEBUG:
                logger.exception('Failed to call "py bin --path {tag}"'.format(tag=tag))
            return None
        # get info
        return self.get_path_info(path)
