import csv
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Student:
    roll: str
    name: str
    marks: List[int] = field(default_factory=lambda: [0, 0, 0])

def total(self) -> int:
    return sum(self.marks)

def average(self) -> float:
    return round(self.total() / len(self.marks), 2) if self.marks else 0.0

def grade(self) -> str:
    avg = self.average()
    if avg >= 90:      return 'A'
    elif avg >= 80:    return 'B'
    elif avg >= 70:    return 'C'
    elif avg >= 60:    return 'D'
    else:              return 'F'