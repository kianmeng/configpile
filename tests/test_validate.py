from __future__ import annotations

from ast import With
from dataclasses import dataclass
from typing import Optional, Sequence

from typing_extensions import Annotated

from configpile import Config, Err, Param, Positional, Validator, config, types


@dataclass(frozen=True)
class WithValidation(Config):
    """
    This is a description
    """

    a: Annotated[int, Param.store(types.int_)]  #: Super doc message

    def validate_a(self) -> Validator:
        if self.a < 0:
            return Err.make("Argument a cannot be negative")
        return None


def test_validation() -> None:
    assert len(WithValidation.validators_()) == 1
    res = WithValidation.parse_command_line_(args=["--a", "2"], env={})
    assert isinstance(res, WithValidation)
    res1 = WithValidation.parse_command_line_(args=["--a", "-2"], env={})
    assert isinstance(res1, Err)
