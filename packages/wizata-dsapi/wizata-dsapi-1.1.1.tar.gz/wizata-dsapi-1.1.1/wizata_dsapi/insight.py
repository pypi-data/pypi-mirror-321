import uuid
from enum import Enum
from .api_dto import ApiDto
import json


class Insight(ApiDto):

    @classmethod
    def route(cls):
        return "insights"

    @classmethod
    def from_dict(cls, data):
        obj = Insight()
        obj.from_json(data)
        return obj

    def __init__(self,
                 insight_id: uuid.UUID = None,
                 name: str = None,
                 display_precision: float = 0.0,
                 condition: dict = None,
                 component_id: uuid.UUID = None,
                 twin_id: uuid.UUID = None,
                 datapoint_id: uuid.UUID = None):
        if insight_id is None:
            self.insight_id = uuid.uuid4()
        else:
            self.insight_id = insight_id
        self.name = name
        self.display_precision = display_precision
        self.condition = condition
        self.component_id = component_id
        self.twin_id = twin_id
        self.datapoint_id = datapoint_id

    def api_id(self) -> str:
        return str(self.insight_id).upper()

    def endpoint(self) -> str:
        return "Insights"

    def from_json(self, obj):
        if "id" in obj.keys():
            self.insight_id = uuid.UUID(obj["id"])

        if "name" in obj.keys():
            self.name = obj["name"]

        if "displayPrecision" in obj.keys() and obj["displayPrecision"] is not None:
            self.display_precision = float(obj["displayPrecision"])

        if "condition" in obj.keys():
            if isinstance(obj["condition"], str):
                self.condition = json.loads(obj["condition"])
            else:
                self.condition = obj["condition"]

        if "componentId" in obj.keys() and obj["componentId"] is not None:
            self.component_id = uuid.UUID(obj["componentId"])

        if "twinId" in obj.keys() and obj["twinId"] is not None:
            self.twin_id = uuid.UUID(obj["twinId"])

        if "sensorId" in obj.keys() and obj["sensorId"] is not None:
            self.datapoint_id = uuid.UUID(obj["sensorId"])

    def to_json(self, target: str = None):
        obj = {
            "id": str(self.insight_id),
        }

        if self.name is not None:
            obj["name"] = str(self.name)

        if self.display_precision is not None:
            obj["displayPrecision"] = self.display_precision

        if self.condition is not None:
            if not isinstance(self.condition, dict):
                raise ValueError('on insight condition must be JSON serializable dict')
            obj["condition"] = json.dumps(self.condition)

        if self.component_id is not None:
            obj["componentId"] = str(self.component_id)

        if self.twin_id is not None:
            obj["twinId"] = str(self.twin_id)

        if self.datapoint_id is not None:
            obj["sensorId"] = str(self.datapoint_id)

        return obj
