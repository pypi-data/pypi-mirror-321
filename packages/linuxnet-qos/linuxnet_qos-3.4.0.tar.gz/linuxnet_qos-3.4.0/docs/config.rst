..
    Copyright (c) 2022, Panagiotis Tsirigotis
    
    This file is part of linuxnet-qos.
    
    linuxnet-qos is free software: you can redistribute it and/or
    modify it under the terms of version 3 of the GNU Affero General Public
    License as published by the Free Software Foundation.
    
    linuxnet-qos is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
    or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public
    License for more details.
    
    You should have received a copy of the GNU Affero General
    Public License along with linuxnet-qos. If not, see
    <https://www.gnu.org/licenses/>.

.. currentmodule:: linuxnet.qos

Queuing Discipline Configuration
================================

The :class:`QDiscConfig` class can be used to access and modify the queuing
discipline configuration of an interface. It provides
the ability to create and delete
arbitrary :class:`QDisc` and
:class:`QClass` objects.

.. autoclass:: QDiscConfig
    :members:
