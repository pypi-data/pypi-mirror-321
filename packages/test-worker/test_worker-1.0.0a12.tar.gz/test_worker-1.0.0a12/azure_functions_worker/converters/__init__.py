# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from .meta import get_binding_registry

# Import binding implementations to register them
from . import blob  # NoQA
from . import cosmosdb  # NoQA
from . import eventgrid  # NoQA
from . import eventhub  # NoQA
from . import http  # NoQA
from . import kafka # NoQA
from . import queue  # NoQA
from . import servicebus  # NoQA
from . import timer  # NoQA
from . import durable_functions  # NoQA
from . import sql  # NoQA
from . import warmup  # NoQA
from . import mysql  # NoQA

__version__ = '1.0.0a10'
