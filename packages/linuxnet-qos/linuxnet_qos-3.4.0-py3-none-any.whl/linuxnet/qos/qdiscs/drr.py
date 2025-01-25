# Copyright (c) 2025, Panagiotis Tsirigotis

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

"""This module provides access to the deficit round robin scheduler (``drr``)
queueing discipline.
"""

import re

from typing import List, Optional, TextIO

from ..deps import get_logger
from ..exceptions import TcParsingError
from ..handle import Handle
from ..tcunit import unitstr2int
from ..parsers import QDiscParser, QClassParser

from .qdisc import QDisc, QClass, QStats

_logger = get_logger("linuxnet.qos.qdiscs.drr")


class DRRQClassStats(QStats):
    """DRR-specific class stats (see :class:`QStats` for inherited stats)
    """

    __LINE4_REGEX_PROG = re.compile(r"deficit (\d+)b")

    def __init__(self):
        super().__init__()
        self.__deficit = 0

    @property
    def deficit(self) -> int:
        """Byte deficit
        """
        return self.__deficit

    def __parse_fourth_line(self, line: str) -> bool:
        """Initialize attributes from ``line``, which is the 4th line
        of ``tc class ls`` output
        """
        # The line looks like this:
        #
        #    deficit 0b
        #
        match = self.__LINE4_REGEX_PROG.match(line.strip())
        if match is None:
            _logger.warning("4th line not parsable: %s", line)
            return False
        self.__deficit = int(match.group(1))
        return True

    def init_from_output(self, line_group_iter: 'LineGroupIter') -> bool:
        """This method is used when parsing the output of ``tc -s qdisc ls``
        to extract statistics information.
        The iterator returns the lines of the output of ``tc -s qdisc ls``
        for a single queuing class.

        :meta private:
        """
        #
        # The first line of the output has already been consumed,
        # and the 2nd line is the next to be returned.
        # Parent class will consume the 2nd and 3rd line
        #
        if not super().init_from_output(line_group_iter):
            return False
        try:
            line = next(line_group_iter)
            if not self.__parse_fourth_line(line):
                return False
        except StopIteration:
            return False
        except ValueError as valerr:
            _logger.warning("bad value in stats line: %s (line=%s)",
                                valerr, line)
            return False
        return True

    def dump(self, outfile: TextIO, width: Optional[int] =None) -> None:
        """Dump stats to ``outfile``.
        There is one stat per line output. Each line has the format::

            header: value

        The ``header:`` part occupies at least ``width`` characters.
        """
        super().dump(outfile, width)
        width = width or self.HEADER_WIDTH
        print(f"{'Deficit:':{width}} {self.__deficit}", file=outfile)


class DRRQClass(QClass):
    """A class of the :class:`DRRQDisc` (``drr``) queuing discipline.
    """

    def __init__(self, class_handle: Handle, parent_handle: Handle,
                        *,
                        quantum: int):
        """
            :param class_handle: handle of this :class:`DRRQClass`
            :param parent_handle: handle of parent :class:`DRRQDisc`
            :param quantum: number of bytes to dequeue per turn
        """
        super().__init__(class_handle, parent_handle, class_name='DRRQClass')
        self.__quantum = quantum
        self.__stats = None

    def __str__(self):
        return f"DRRQClass({self.get_handle()})"

    def get_description(self) -> str:
        """Returns a string describing the class and its attributes
        """
        class_name = self.get_class_name()
        retval = f'{class_name}({self.get_handle()})'
        retval += f' quantum {self.__quantum}'
        return retval

    def get_quantum(self) -> int:
        """Returns the quantum (bytes)
        """
        return self.__quantum

    def get_stats(self) -> Optional[DRRQClassStats]:
        """Returns class stats (an :class:`DRRQClassStats` instance) or
        ``None`` if no stats are available.
        """
        return self.__stats

    def qclass_creation_args(self) -> List[str]:
        """Returns the tc arguments to create this DRR class
        """
        return ['drr', 'quantum', str(self.__quantum)]

    def _parse_stats(self, line_group_iter) -> None:
        """Parse queuing stats
        """
        stats = DRRQClassStats()
        if stats.init_from_output(line_group_iter):
            self.__stats = stats

    @classmethod
    def parse(cls, qclass_output) -> 'DRRQClass':
        """Create a :class:`DRRQClass` from the output of **tc(8)**

        :meta private:
        """
        #
        # The iterator returns the fields of a line like this:
        #
        # class drr 1:1 root quantum 1514b
        #
        # The fields 'class', 'drr', 'root' (and their values)
        # have been consumed by the caller.
        #
        try:
            quantum = None
            field_iter = qclass_output.get_field_iter()
            for field in field_iter:
                if field == 'quantum':
                    quantum = unitstr2int(next(field_iter), 'b')
                else:
                    raise TcParsingError(f"unknown field '{field}'")
            if quantum is None:
                raise TcParsingError("DRR class missing quantum")
            drr_qclass = DRRQClass(qclass_output.get_handle(),
                                    qclass_output.get_parent_handle(),
                                    quantum=quantum)
            return drr_qclass
        except ValueError as valerr:
            raise TcParsingError(f"bad value for {field}") from valerr


class DRRQDisc(QDisc):
    """This class provides access to the multiqueue (``drr``)
    queueing discipline of Linux
    """

    def __str__(self):
        return f"DRRQDisc({self.get_handle()})"

    def qdisc_creation_args(self) -> List[str]:
        """Returns the arguments expected by the **tc(8)** command to create
        a DRR qdisc
        """
        return ['drr']

    @classmethod
    def parse(cls, qdisc_output) -> 'DRRQDisc':
        """Create a :class:`DRRQDisc` object from the output of
        **tc(8)**.

        :meta private:
        """
        #
        # The tc output looks like this:
        #
        # qdisc drr 0: root refcnt 9
        #
        # There are no discipline-specific parameters.
        #
        return DRRQDisc(qdisc_output.get_handle(),
                                qdisc_output.get_parent_handle())

QDiscParser.register_qdisc('drr', DRRQDisc)
QClassParser.register_qclass('drr', DRRQClass)
