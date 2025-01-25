from collections.abc import Iterator, Sequence
from datetime import datetime, timedelta
from typing import Self, SupportsIndex, final, overload

__all__ = ['DatetimeRange']


@final
class DatetimeRange(Sequence[datetime]):

    __slots__ = (
        '__start',
        '__stop',
        '__step',
    )

    __start: datetime
    __stop: datetime
    __step: timedelta

    @property
    def start(
        self,
        /,
    ) -> datetime:
        return self.__start

    @property
    def stop(
        self,
        /,
    ) -> datetime:
        return self.__stop

    @property
    def step(
        self,
        /,
    ) -> timedelta:
        return self.__step

    def __init__(
        self,
        start: datetime,
        stop: datetime,
        step: timedelta,
        /,
    ) -> None:
        if not step:
            raise ValueError(f"DatetimeRange() arg 3 must not be {step}")
        self.__start = start
        self.__stop = stop
        self.__step = step

    def __repr__(
        self,
        /,
    ) -> str:
        return f"DatetimeRange({self.start}, {self.stop}, {self.step})"

    def __eq__(
        self,
        other: object,
        /,
    ) -> bool:
        if not isinstance(other, DatetimeRange):
            return False
        return (
            self.start == other.start
            and self.stop == other.stop
            and self.step == other.step
        )

    def __hash__(
        self,
        /,
    ) -> int:
        return hash((self.start, self.stop, self.step))

    def __len__(
        self,
        /,
    ) -> int:
        return (self.stop - self.start) // self.step

    def __contains__(
        self,
        key: object,
        /,
    ) -> bool:
        if not isinstance(key, datetime):
            return False
        return self.start <= key < self.stop and 0 == (key - self.start) % self.step

    @overload
    def __getitem__(
        self,
        key: SupportsIndex,
        /,
    ) -> datetime: ...

    @overload
    def __getitem__(
        self,
        key: slice,
        /,
    ) -> Self: ...

    def __getitem__(
        self,
        key: SupportsIndex | slice,
        /,
    ) -> datetime | Self:
        raise NotImplementedError()

    def __iter__(
        self,
        /,
    ) -> Iterator[datetime]:
        stop = self.stop
        step = self.step
        current = self.start
        while current < stop:
            yield current
            current += step

    def __reversed__(
        self,
        /,
    ) -> Iterator[datetime]:
        start = self.start
        step = self.step
        current = start + len(self) * step
        while start <= current:
            yield current
            current -= step

    def count(
        self,
        value: datetime,
        /,
    ) -> int:
        return 1 if value in self else 0

    def index(
        self,
        value: datetime,
        /,
    ) -> int:
        if value not in self:
            raise ValueError(f"{value} is not in {self}")
        return (value - self.start) // self.step
