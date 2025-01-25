from typing import List, Optional, Union

from pydantic import ConfigDict, Field
from pydantic.dataclasses import dataclass

from ltiaas.resources.scores.enums import ActivityProgress, GradingProgress
from ltiaas.utils.serialization import Serializable


@dataclass(config=ConfigDict(extra="allow", populate_by_name=True))
class Result(Serializable):
    id: str
    user_id: str = Field(alias="userId", coerce_numbers_to_str=True)
    score_of: str = Field(alias="scoreOf")
    result_score: Optional[float | int] = Field(None, alias="resultScore")
    result_maximum: Optional[float | int] = Field(None, alias="resultMaximum")
    comment: Optional[str] = None


@dataclass(config=ConfigDict(extra="allow", populate_by_name=True))
class Score(Serializable):
    user_id: Union[str] = Field(alias="userId", coerce_numbers_to_str=True)
    activity_progress: ActivityProgress = Field(alias="activityProgress")
    grading_progress: GradingProgress = Field(alias="gradingProgress")
    score_given: Optional[float] = Field(None, alias="scoreGiven")
    score_maximum: Optional[float] = Field(None, alias="scoreMaximum")
    comment: Optional[str] = None

    def __post_init__(self):
        if self.score_given is not None and self.score_maximum is None:
            raise ValueError(
                "The scoreMaximum must be defined if scoreGiven is defined"
            )


@dataclass
class ResultContainer(Serializable):
    scores: List[Result]
    next: Optional[str] = None
    first: Optional[str] = None
    last: Optional[str] = None
    prev: Optional[str] = None
