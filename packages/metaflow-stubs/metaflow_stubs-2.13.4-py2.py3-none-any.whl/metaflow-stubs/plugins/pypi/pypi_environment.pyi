######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.13.4                                                                                 #
# Generated on 2025-01-15T17:53:58.625440                                                            #
######################################################################################################

from __future__ import annotations

import metaflow
import typing
if typing.TYPE_CHECKING:
    import metaflow.plugins.pypi.conda_environment

from .conda_environment import CondaEnvironment as CondaEnvironment

class PyPIEnvironment(metaflow.plugins.pypi.conda_environment.CondaEnvironment, metaclass=type):
    ...

