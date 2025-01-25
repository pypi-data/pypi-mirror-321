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

.. currentmodule:: linuxnet.qos

linuxnet.qos API
================

The **linuxnet.qos** API consists of the following:

- :class:`QDiscConfig` : objects of this class contain the queueing
  discipline configuration for a particular network interface
- :ref:`Classes <qdisc>` that provide access to queueing disciplines
  (e.g. :class:`HTBQDisc`); where those disciplines are classful,
  Python classes are available for the queueing discipline classes
  (e.g. :class:`HTBQClass`)
- Classes that provide access to queueing discipline
  :ref:`statistics <queuing_statistics>`; at a minimum, the statistics
  are those available
  via the :ref:`QStats <qstats>` class, but some queueing disciplines
  provide their own subclass with additional statistics
- :ref:`Classes <traffic_filter>` that provide access
  to traffic filters
- :ref:`Classes <traffic_action>` that provide access
  to traffic actions (e.g. policing)

The programming model of this library is centered around the
:class:`QDiscConfig` class. One creates a :class:`QDiscConfig` instance,
which is then used to obtain the queuing discipline configuration
of the interface, or to modify that configuration.
All configuration changes must explicitly take place via 
a :class:`QDiscConfig` instance.

Installing a new queuing discipline configuration is a 2-step process:
first, one creates an instance of the specific Python class for the
desired queuing discipline (e.g. :class:`HTBQDisc`) with the appropriate
parameters, and then uses that Python class instance as an argument
to the :func:`QDiscConfig.create_qdisc` method to create the queuing
discipline inside the kernel.

Installing a new queuing class is a 2-step process:
first, one creates an instance of the specific Python class for the
desired queuing class (e.g. :class:`HTBQClass`) with the appropriate
parameters, and then uses that Python class instance as an argument
to the :func:`QDiscConfig.create_qclass` method to create the queuing
class inside the kernel.

Installing a new filter is a 2-step process:
first, one creates an instance of the specific Python class for the
desired traffic filter (e.g. :class:`U32Filter`) with the appropriate
parameters, and then uses that Python class instance as an argument
to the :func:`QDiscConfig.create_filter` method to create the traffic
filter inside the kernel.


.. toctree::
    :maxdepth: 2
    :hidden:

    config
    qdisc
    traffic_filters
    traffic_actions
    stats
    exceptions
    extensibility
