# Copyright (c) 2022, Panagiotis Tsirigotis

# This file is part of linuxnet-qos.
#
# linuxnet-qos is free software: you can redistribute it and/or
# modify it under the terms of version 3 of the GNU Affero General Public
# License as published by the Free Software Foundation.
#
# linuxnet-qos is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public
# License for more details.
#
# You should have received a copy of the GNU Affero General
# Public License along with linuxnet-qos. If not, see
# <https://www.gnu.org/licenses/>.

"""Compatibility module to hide the dependency on the progutil package.
"""

# pylint: disable=unused-import

try:
    from progutil.logging import get_logger
except ImportError:
    from logging import getLogger as get_logger
