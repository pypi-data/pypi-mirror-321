..
    Copyright (c) 2023, 2025, Panagiotis Tsirigotis
    
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

.. _traffic_action:

Traffic actions
===============

Traffic actions allow certain predefined operations to be applied to incoming
or outgoing packets that are matched by some traffic filter.
An example of such an operation is rate policing.

Although traffic actions may exist as standalone objects in the kernel,
they **must** be associated with a traffic filter in order to take
effect.

A traffic action is of a certain action kind; ``police`` is such an
action kind (the terminology *action kind* is specific to this package).
Traffic actions are identified by an action index; this index
is per action kind.

This package provides Python classes that correspond to traffic action kinds.
They are implemented as subclasses of the :class:`TrafficAction` class.
An instance of a :class:`TrafficAction` subclass
can be created and added to a :class:`TrafficFilter` instance
**before** the filter is instantiated.

Traffic actions can be shared. This is implemented by creating
an instance of a :class:`TrafficAction` subclass and specifying
the action index of an existing action (of the same kind).

Standalone traffic actions are not currently supported.

.. currentmodule:: linuxnet.qos

The **linuxnet.qos** package supports the following
traffic action classes:

.. toctree::
    :maxdepth: 1
    :glob:

    actions/*

-------------

Certain classes provide functionality common to all traffic actions.

.. currentmodule:: linuxnet.qos.action

.. autoclass:: ActionDecision
    :members:
    :member-order: bysource
