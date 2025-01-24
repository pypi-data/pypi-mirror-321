######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.13.5                                                                                 #
# Generated on 2025-01-16T23:35:54.546077                                                            #
######################################################################################################

from __future__ import annotations

import metaflow
import typing
if typing.TYPE_CHECKING:
    import metaflow.plugins.pypi.conda_environment

from .conda_environment import CondaEnvironment as CondaEnvironment

class PyPIEnvironment(metaflow.plugins.pypi.conda_environment.CondaEnvironment, metaclass=type):
    ...

