######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.13.5                                                                                 #
# Generated on 2025-01-16T23:35:54.535192                                                            #
######################################################################################################

from __future__ import annotations

import metaflow
import typing
if typing.TYPE_CHECKING:
    import metaflow.monitor


class DebugMonitor(metaflow.monitor.NullMonitor, metaclass=type):
    @classmethod
    def get_worker(cls):
        ...
    ...

class DebugMonitorSidecar(object, metaclass=type):
    def __init__(self):
        ...
    def process_message(self, msg):
        ...
    ...

