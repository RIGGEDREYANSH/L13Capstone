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

PALLETTE = {"bg": "#F7FAFC", "header_start": "#7F7FD5", "header_mid": "#86A8E7", "header_end": "#91EAE4",
    "accent": "#2563EB", "success": "#16A34A", "warn": "#F59E0B", "danger": "#DC2626",
    "muted": "#64748B", "card": "#FFFFFF", "border": "#E5E7EB",}

GRADE_TAGS = {
    "A+": ("#065F46", "#D1FAE5"),
    "A":  ("#065F46", "#D1FAE5"),
    "B":  ("#1E40AF", "#DBEAFE"),
    "C":  ("#92400E", "#FEF3C7"),
    "D":  ("#92400E", "#FEF3C7"),
    "F":  ("#7F1D1D", "#FEE2E2"),
}

class UnifiedApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Performance")
        self.geometry("1180x720")
        self.minsize(1080, 660)
        self.configure(bg=PALLETTE["bg"])
       
        self._build_styles()

        self._build_header()

        self.nb = ttk.Notebook(self)
        self.nb.pack(fill="both", expand=True, padx=12,pady=12)

        self.tab_tracker = ttk.Frame(self.nb)
        self.nb.add(self.tab_tracker, text="Tracker")
        self.tracker = TrackerFrame(self.tab_tracker)
        self.tracker.pack(fill="both", expand=True)

        self.tab_activities = ttk.Frame(self.nb)
        self.nb.add(self.tab_activities, text="Activities")
        self.activities = ActivitiesFrame(self.tab_activities)
        self.activities.pack(fill="both", expand=True)

    def _build_styles(self):
        style = ttk.style(self)
        try:
            style.theme_use("clam")
        except Exception:
            pass
        style.configure("TFrame", background=PALLETTE["bg"])
        style.configure("Card.TFrame", background=PALLETTE["card"], relief="groove")
        style.configure("TLabel", background=PALLETTE["bg"], forground="#111827", font=("Segoe UI", 10))
        style.configure("Header.TLabel", background=PALLETTE["bg"],foreground=PALLETTE["muted"], font=("Segoe UI", 14, "bold"))
        style.configure("Muted.TLabel", background=PALLETTE["bg"], foreground=PALLETTE["muted"], font=("Segoe UI", 10, "italic"))
        style.configure("TButton",font=("Segoe UI", 14, "bold"), padding=6 )
        style.configure("Treeview",
                        background=PALLETTE["card"],
                        fieldbackground=PALLETTE["card"],
                        bordercolor=PALLETTE["border"],
                        rowheight=26,
                        font=("Segoe UI", 10))
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))