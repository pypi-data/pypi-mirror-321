from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any
from datetime import datetime
import json
import uuid
from dataclasses_json import DataClassJsonMixin


@dataclass
class BaseEvent(DataClassJsonMixin):
    """Base event class with common attributes for all events"""

    event_id: str
    user_id: str
    event_type: str
    timestamp: str
    entity_id: str
    location: str
    site_id: str
    survey_date: str
    survey_id: str
    correlation_id: Optional[str] = None
