# Copyright (c) 2023, 2025, Panagiotis Tsirigotis

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

"""This module provides traffic action classes
"""

from enum import Enum
from typing import Any, List, Optional, Mapping


class ActionDecision(Enum):
    """List of decisions for **tc(8)** actions (see :manpage:`tc-actions(8)`);
    these are also referred-to as *controls*.
    """
    #: Reclassify packet
    RECLASSIFY = 'reclassify'
    #: Pass packet to next action
    PIPE = 'pipe'
    #: Drop packet
    DROP = 'drop'
    #: Pass packet to next filter
    CONTINUE = 'continue'
    #: End packet classification (packet returned to queuing discipline/class)
    PASS = 'pass'

    @classmethod
    def create_from_string(cls, decision_str: str) -> 'ActionDecision':
        """Convert from a string to an :class:`ActionDecision` member.

        :param decision_str: the string representation of
            :class:`ActionDecision` member.
        :rtype: a :class:`ActionDecision` member

        Raises a :exc:`ValueError` if no match is found.
        """
        for decision in ActionDecision.__members__.values():
            if decision.value == decision_str:
                return decision
        raise ValueError(f'bad ActionDecision value: {decision_str}')


class TrafficAction:
    """Generic action class. It cannot be instantiated.
    It is subclassed based on action type (aka kind).
    """

    def __init__(self, action_index: Optional[int],
                decision: Optional[ActionDecision] =None):
        """
        :param kind: the action type (e.g. ``police``)
        :param action_index: an integer that effectively names the action;
            the kernel will pick one if it is not explicitly given
        :param decision: what to do after executing the action
        """
        self.__actid = action_index
        self.__decision = decision

    def __str__(self):
        return f'TrafficAction({self.get_kind()})'

    def get_kind(self) -> str:
        """Returns the action type
        """
        raise NotImplementedError

    def get_action_index(self) -> Optional[int]:
        """Returns the action index
        """
        return self.__actid

    def get_decision(self) -> Optional[ActionDecision]:
        """Returns the decision (e.g. :attr:`ActionDecision.DROP`)
        for this action
        """
        return self.__decision

    def _action_specific_args(self) -> List[str]:
        """Returns a list of **tc(8)** arguments that are specific
        to this action.
        """
        raise NotImplementedError

    # The field_iter is not used (yet).
    #
    # pylint: disable=unused-argument
    #
    @staticmethod
    def _parse_common(field: str, field_iter,
                                parsed_args: Mapping[str, Any]) -> bool:
        """Check if ``field`` is one of a list of common action attributes,
        and set a mapping in parsed_args. The parsed_args is expected
        to be passed to our constructor later.
        Returns ``True`` if the field is parsed, ``False`` otherwise.
        """
        for decision in ActionDecision.__members__.values():
            if field == decision.value:
                parsed_args['decision'] = decision
                return True
        return False
    # pylint: enable=unused-argument

    def action_creation_args(self) -> List[str]:
        """Returns a list of **tc(8)** arguments to instantiate this action
        """
        args = ['action', self.get_kind()]
        if self.__actid is not None:
            args.extend(['index', str(self.__actid)])
        args.extend(self._action_specific_args())
        if self.__decision is not None:
            args.append(self.__decision.value)
        return args
