

# import sys
import os

# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))
# from .models import Patient
from dataclasses import dataclass

from utils import Patient
# @dataclass
# class Patient:
#     name: str
#     family: str
#     priority: bool = False
#     fractions_number: int = None



FRACTION_LIMIT = os.environ.get('FRACTION_LIMIT', 40)
MALE_WEIGHT_LIMIT = os.environ.get('MALE_WEIGHT_LIMIT', 90)
FEMALE_WEIGHT_LIMIT = os.environ.get('MALE_WEIGHT_LIMIT', 60)
MALE_SEX = 'male'
FEMALE_SEX = 'female'


@dataclass
class Queues:
    all: [Patient]
    heavy_weight: [Patient]
    low_fraction: [Patient]

    
def is_priority(sub: Patient):
    return sub.priority
    
    
class QueueProccess:
    _instance = None
    
    def __new__(cls, *args, **kwars):
        if cls._instance is None:
            cls._instance = super(QueueProccess, cls).__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        if not hasattr(self, 'queues'):
            self.queues = Queues([], [], [])
    
    def add_patient(self, sub:Patient):
        # fracrtion queue
        if sub.fractions_number <= FRACTION_LIMIT:
            self.queues.low_fraction.append(sub)
        # heavy weight and breath hold
        elif sub.sex == MALE_SEX and sub.weight >= MALE_WEIGHT_LIMIT:
            self.queues.heavy_weight.append(sub)
        elif sub.sex == FEMALE_SEX and sub.weight >= FEMALE_WEIGHT_LIMIT:
            self.queues.heavy_weight.append(sub)
        elif sub.breath_holding: 
            self.queues.heavy_weight.append(sub)
        # all cases
        else:
            self.queues.all.append(sub)


# check
#--------------------------------------------------------------------------------≠
pat_1 = Patient(    
    name='Jora',
    last_name='Kryjovnikov',
    sex='male',
    email='test@com',
    weight=170,
    priority=False,
    fractions_number=120 
)

pat_2 = Patient(
           name='Masha',
           last_name='Testova',
           sex='female',
           email='tes1t@com',
           weight=50,
           priority=False,
           fractions_number=55           
       )

test = QueueProccess()
test.add_patient(pat_1)
test.add_patient(pat_2)
print(test.queues.all)
print(test.queues.heavy_weight)
print(test.queues.low_fraction)
    

