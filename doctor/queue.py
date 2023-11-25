

# import sys
import os

# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))

from dataclasses import dataclass


@dataclass
class Patient:
    name: str
    family: str
    priority: bool = False
    fractions_number: int = None



FRACTION_LIMIT = os.environ.get('FRACTION_LIMIT', 40)



@dataclass
class Queues:
    all: [Patient] = None
    heavy_weight: [Patient] = None
    low_fraction: [Patient] = None

    
def is_priority(sub: Patient):
    return sub.priority
    
    
class QueueProccess:
    _instance = None
    
    def __new__(cls, *args, **kwars):
        if cls._instance is None:
            cls._instance = super(QueueProccess, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, queues: Queues) -> None:
        if not hasattr(self, 'queues'):
            self.queues = queues
    
    def add_patient(self, sub:Patient):
        if sub.fractions_number <= FRACTION_LIMIT:
            self.queues.low_fraction.append(sub)
        elif sub

    
    
    
list_p = [
    Patient(
           name='Jora',
           family='Kryjovnikov',
           priority=False,
           fractions_number=20
           gender
           

       ),
    Patient(
        name='Masha',
        family='Petrove',
        priority=True,
        fractions_number=60
    )
]

test = QueueProccess(Queues(all=list_p))
        
    

