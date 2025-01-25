# Copyright (c) 2024, RTE (http://www.rte-france.com)
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# SPDX-License-Identifier: MPL-2.0

import importlib.metadata
import logging

import pandas as pd

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

pd.options.mode.copy_on_write = True

__version__ = importlib.metadata.version("mechaphlowers")
