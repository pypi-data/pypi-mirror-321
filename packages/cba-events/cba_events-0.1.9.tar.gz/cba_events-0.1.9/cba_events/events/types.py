from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from .base_event import BaseEvent


# @dataclass
class StockpileEvent(BaseEvent):
    """Stockpile-related event class"""

    action: str
    details: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        super().__init__(event_type="stockpile")


class PitEvent(BaseEvent):
    """Stockpile-related event class"""

    action: str
    details: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        super().__init__(event_type="pit")


class VolumetricEvent(BaseEvent):
    """Stockpile-related event class"""

    action: str
    details: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        super().__init__(event_type="pit")
