######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.13.4.1+obcheckpoint(0.1.6);ob(v1)                                                    #
# Generated on 2025-01-15T20:56:03.666634                                                            #
######################################################################################################

from __future__ import annotations

import metaflow
import typing
if typing.TYPE_CHECKING:
    import metaflow.exception
    import metaflow

from ......exception import MetaflowException as MetaflowException
from .core import resolve_root as resolve_root

TYPE_CHECKING: bool

class UnresolvableDatastoreException(metaflow.exception.MetaflowException, metaclass=type):
    ...

def init_datastorage_object():
    ...

def resolve_storage_backend(pathspec: typing.Union[str, "metaflow.Task"] = None):
    ...

