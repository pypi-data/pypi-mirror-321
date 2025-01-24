######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.13.4.1+obcheckpoint(0.1.6);ob(v1)                                                    #
# Generated on 2025-01-15T20:56:03.735136                                                            #
######################################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import typing


class SerializationHandler(object, metaclass=type):
    def serialze(self, *args, **kwargs) -> typing.Union[str, bytes]:
        ...
    def deserialize(self, *args, **kwargs) -> typing.Any:
        ...
    ...

