"""Checks for redundant Union typehints in assignments"""
# pylint: disable=deprecated-typing-alias,consider-alternative-union-syntax,consider-using-alias,invalid-name,unused-argument,missing-function-docstring

from __future__ import annotations
from typing import Union, Optional, Sequence
ANSWER_0: Union[int, int, str, bool, float, str] = 0
ANSWER_1: Optional[int] = 1
ANSWER_2: Sequence[int] = [2]
ANSWER_3: Union[list[int], str, int, bool, list[int]] = 3  # [redundant-typehint-argument]
ANSWER_4: Optional[None] = None   # [redundant-typehint-argument]
ANSWER_5: Optional[list[int]] = None
ANSWER_6: Union[None, None] = None   # [redundant-typehint-argument]
#  +1: [redundant-typehint-argument]
ANSWER_7: Union[list[int], dict[int], dict[list[int]], list[str], list[str]] = [7]
ANSWER_8: int | int = 8  # [redundant-typehint-argument]
ANSWER_9: str | int | None | int | bool = 9   # [redundant-typehint-argument]
ANSWER_10: dict | list[int] | float | str | int | bool = 10
#  +1: [redundant-typehint-argument]
ANSWER_11: list[int] | dict[int] | dict[list[int]] | list[str] | list[str] = ['string']

# Multiple warnings for the same repeated type
# Multiple warnings for the same repeated type
x: int  # Only one occurrence of int is needed

# No warning for redundant types in compound type (yet !)
z: dict[int, str]

zz: dict[int, str] | dict[int, str]  # Remove redundant type hints in the compound type
