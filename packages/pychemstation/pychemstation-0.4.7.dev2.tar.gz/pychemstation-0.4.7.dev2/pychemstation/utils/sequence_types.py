from dataclasses import dataclass
from enum import Enum
from typing import Optional


class SampleType(Enum):
    SAMPLE = 1
    BLANK = 2
    CONTROL = 3
    CALIBRATION = 4


class InjectionSource(Enum):
    AS_METHOD = "AsMethod"
    MANUAL = "Manual"
    HIP_ALS = "HipAls"


@dataclass
class SequenceEntry:
    vial_location: Optional[int] = None
    method: Optional[str] = None
    num_inj: Optional[int] = 1
    inj_vol: Optional[int] = 2
    inj_source: Optional[InjectionSource] = InjectionSource.HIP_ALS
    sample_name: Optional[str] = None
    sample_type: Optional[SampleType] = SampleType.SAMPLE


@dataclass
class SequenceTable:
    name: str
    rows: list[SequenceEntry]
