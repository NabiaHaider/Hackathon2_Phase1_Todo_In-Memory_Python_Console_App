from dataclasses import dataclass, field

@dataclass
class Task:
    id: int
    title: str
    description: str = field(default="")
    is_completed: bool = field(default=False)
