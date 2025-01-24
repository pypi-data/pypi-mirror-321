from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from .base_event import BaseEvent


# @dataclass
class StockpileEvent(BaseEvent):
    """Stockpile-related event class"""

    action: str = "calculate"
    details: Dict[str, Any] = field(default_factory=dict)

    def __init__(
        self,
        site_id: str,
        location: str,
        entity_id: str,
        survey_date: str,
        user_id: str,
        survey_id: str,
        action: str,
        **kwargs,
    ):
        super().__init__(
            event_type="stockpile_event",
            entity_id=entity_id,
            location=location,
            site_id=site_id,
            survey_date=survey_date,
            user_id=user_id,
            survey_id=survey_id,
            action=action,
        )
        self.action = action
        self.details = kwargs.get("details", {})


# @dataclass
class PitEvent(BaseEvent):
    """Stockpile-related event class"""

    action: str = "calculate"
    details: Dict[str, Any] = field(default_factory=dict)

    def __init__(
        self,
        site_id: str,
        location: str,
        entity_id: str,
        survey_date: str,
        user_id: str,
        survey_id: str,
        action: str,
        **kwargs,
    ):
        super().__init__(
            event_type="pit_event",
            entity_id=entity_id,
            location=location,
            site_id=site_id,
            survey_date=survey_date,
            user_id=user_id,
            survey_id=survey_id,
            action=action,
        )
        self.action = action
        self.details = kwargs.get("details", {})


# @dataclass
class VolumetricEvent(BaseEvent):
    """Stockpile-related event class"""

    action: str = "calculate"
    details: Dict[str, Any] = field(default_factory=dict)

    def __init__(
        self,
        site_id: str,
        location: str,
        entity_id: str,
        survey_date: str,
        user_id: str,
        survey_id: str,
        action: str,
        **kwargs,
    ):
        super().__init__(
            event_type="volumetric_event",
            entity_id=entity_id,
            location=location,
            site_id=site_id,
            survey_date=survey_date,
            user_id=user_id,
            survey_id=survey_id,
            action=action,
        )
        self.action = action
        self.details = kwargs.get("details", {})
