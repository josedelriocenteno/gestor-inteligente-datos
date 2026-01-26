from dataclasses import dataclass, field

@dataclass
class productos():
    nombre:str
    precio:float
    dict_productos = dict(default_factory=dict)

