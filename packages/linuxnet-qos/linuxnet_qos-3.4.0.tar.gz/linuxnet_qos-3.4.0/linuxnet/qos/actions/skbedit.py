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

"""
This module provides access to the ``skbedit`` action.
"""

from typing import Iterator, List, Optional

from ..deps import get_logger
from ..exceptions import TcParsingError
from ..parsers import TrafficFilterParser

from .action import TrafficAction, ActionDecision

_logger = get_logger("linuxnet.qos.actions.skbedit")


class SkbeditAction(TrafficAction):
    """This class supports the **tc(8)** ``skbedit`` action as
    documented in :manpage:`tc-skbedit(8)`.
    """

    KIND = 'skbedit'

    def __init__(self, action_index: Optional[int] =None,
                        decision: Optional[ActionDecision] =None,
                        *,
                        queue_mapping: Optional[int] =None,
                        priority: Optional[str] =None,
                        mark: Optional[int] =None,
                        mask: Optional[int] =None,
                        packet_type: Optional[str],
                        inheritdsfield: Optional[bool] =False):
        """
        :param action_index: an integer that effectively names the action
        :param decision: control action to take
        :param queue_mapping: specify transmit queue for packet
        :param priority: priority
        :param mark: firewall mark
        :param mask: mask for the ``mark``
        :param packet_type: packet type
        :param inheritdsfield: use the ``DiffServ`` field to override the
            classification decision
        """
        super().__init__(action_index, decision)
        self.__queue_mapping = queue_mapping
        self.__priority = priority
        self.__mark = mark
        self.__mask = mask
        self.__packet_type = packet_type
        self.__inheritdsfield = inheritdsfield

    @classmethod
    def get_kind(cls) -> str:
        """Returns ``skbedit``
        """
        return cls.KIND

    def get_queue_mapping(self) -> Optional[int]:
        """Returns the queue mapping, if any
        """
        return self.__queue_mapping

    def get_priority(self) -> Optional[str]:
        """Returns the priority, if any
        """
        return self.__priority

    def get_mark(self) -> Optional[int]:
        """Returns the firewall mark, if any
        """
        return self.__mark

    def get_mask(self) -> Optional[int]:
        """Returns the mask for the firewall mark, if any
        """
        return self.__mask

    def get_packet_type(self) -> Optional[str]:
        """Returns the packet type, if any
        """
        return self.__packet_type

    def inheritdsfield(self) -> bool:
        """Returns the **inheritdsfield** value
        """
        return self.__inheritdsfield

    def _action_specific_args(self) -> List[str]:
        """Returns a list of **tc(8)** arguments to create this action
        """
        args = []
        if self.__queue_mapping:
            args.extend(['queue_mapping', str(self.__queue_mapping)])
        if self.__priority:
            args.extend(['priority', self.__priority])
        if self.__mark:
            markstr = f'0x{self.__mark:x}'
            if self.__mask:
                markstr += f'/0x{self.__mark:x}'
            args.extend(['mark', markstr])
        if self.__packet_type:
            args.extend(['ptype', self.__packet_type])
        if self.__inheritdsfield:
            args.append('inheritdsfield')
        args.append(self.get_decision().value)
        return args

    @classmethod
    def parse(cls,      # pylint: disable=too-many-locals
                        fields: List[str],
                        line_iter: Iterator) -> TrafficAction:
        """The ``fields`` list holds the line fields after ``skbedit``.
        The ``line_iter`` is an iterator for the following lines.
        If the fields are successfully parsed, a :class:`SkbeditAction`
        instance is returned.

        :meta private:
        """
        #
        # The expected format of the fields is:
        #
        #    queue_mapping 3 priority 1:2 mark 3/0xff ptype host inheritdsfield pipe
        #
        # The following line looks like this:
        #
        #       index 7 ref 1 bind 1
        #
        field_iter = iter(fields)
        queue_mapping = None
        priority = None
        packet_type = None
        mark = None
        mask = None
        inheritdsfield = False
        common_args = {}
        try:
            for field in field_iter:
                if field == 'queue_mapping':
                    queue_mapping = int(next(field_iter))
                elif field == 'priority':
                    priority = next(field_iter)
                elif field == 'mark':
                    value = next(field_iter)
                    if '/' in value:
                        markstr, maskstr = value.split('/', 1)
                        mark = int(markstr, 0)
                        mask = int(maskstr, 0)
                    else:
                        mark = int(value, 0)
                elif field == 'ptype':
                    packet_type = next(field_iter)
                elif field == 'inheritdsfield':
                    inheritdsfield = True
                elif cls._parse_common(field, field_iter, common_args):
                    pass
                else:
                    raise TcParsingError(f"unknown skbedit param: {field}")
        except ValueError as valerr:
            raise TcParsingError(f"bad skbedit {field} value") from valerr
        action_index = None
        for line in line_iter:
            if not line:
                break
            fields = line.split()
            try:
                if fields[0] == 'index':
                    action_index = int(fields[1])
            except IndexError:
                pass
        return SkbeditAction(
                        action_index, **common_args,
                        queue_mapping=queue_mapping, priority=priority,
                        mark=mark, mask=mask,
                        packet_type=packet_type,
                        inheritdsfield=inheritdsfield)


TrafficFilterParser.register_action(action_name=SkbeditAction.KIND,
                                        klass=SkbeditAction)
