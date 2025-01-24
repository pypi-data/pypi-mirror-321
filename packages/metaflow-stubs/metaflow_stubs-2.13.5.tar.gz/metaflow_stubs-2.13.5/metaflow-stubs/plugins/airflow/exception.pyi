######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.13.5                                                                                 #
# Generated on 2025-01-16T23:35:54.553713                                                            #
######################################################################################################

from __future__ import annotations

import metaflow
import typing
if typing.TYPE_CHECKING:
    import metaflow.exception

from ...exception import MetaflowException as MetaflowException

class AirflowException(metaflow.exception.MetaflowException, metaclass=type):
    def __init__(self, msg):
        ...
    ...

class NotSupportedException(metaflow.exception.MetaflowException, metaclass=type):
    ...

