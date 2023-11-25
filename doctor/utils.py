from dataclasses import dataclass

@dataclass
class Patient:
    name: str
    last_name: str
    sex: str
    weight: str
    email: str
    fractions_number: int
    large_bodied: bool = False
    priority: bool = False
    breath_holding: bool = False
    fractions_number: int = None
    inpatient: bool = False
