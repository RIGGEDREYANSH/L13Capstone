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

    def _build_header(self):
        header_h = 90
        self.header_canvas = tk.Canvas(self, height=header_h, highlightthickness=0, bd=0)
        self.header_canvas.pack(fill="x")
        self._draw_gradient(self.header_canvas,0,0, self.winfo_screenmmwidth(), header_h,
                            PALLETTE["header_start"], PALLETTE["header_mid"], PALLETTE["header_end"])
        self.header_canvas.create_text(24, header_h//2 - 10, anchor="w",
                                       text="Student Performance Tracker - Unified Window",
                                       font=("Segoe UI", 20, "bold"), fill="white")
        self.header_canvas.create_text(24, header_h//2 + 16, anchor="w",
                                       text="Tracker, Search, Topper, CSV, Reports + All Activities in tabs",
                                       fint=("Segoe UI", 11), fill="#435C76")
        
    def _draw_gradient(Self, canas, x1, y1, x2, y2, c1, c2, c3, steps=256):
        r1, g1, b1 = self.winfo_rgb(c1); r2, g2, b2, = self.winfo_rgb(c2); r3, g3, b3 = self.winfo_rgb(c3)
        for i in range(steps//2):
            r = int(r1 + (r2-r1) * i / (steps//2)); g = (g1 + (g2-g1) * i / (steps//2)); b = (b1 + (b2-b1) * i / (steps//2));
            color = f"#{r//256:02x}{g//256:02x}{b//256:02x}"
            y = y1 + (y2 - y1) * i / steps
            canvas.create_rectangle(x1, y, x2, y + (y2-y1)/steps, outline="", fill=color)
        for i in range(steps//2):
            r = int(r2 + (r3-r2) * i / (steps//2)); g = (g2 + (g3-g2) * i / (steps//2)); b = (b2 + (b3-b2) * i / (steps//2));
            color = f"#{r//256:02x}{g//256:02x}{b//256:02x}"
            y = y1 + (y2 - y1) * (i+steps//2) / steps
            canvas.create_rectangle(x1, y, x2, y + (y2-y1)/steps, outline="", fill=color)

class TrackerFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, style="TFrame")
        self.students: List[Student] = []

        self._build.body()
        self._build_events()
    
def _build_body(self):
    root = ttk.Frame(self, style="TFrame")
     
    left = ttk.Frame(root, style="TFrame"); root.pack(side="left", fill="y", padx=(0,10), pady=8)
    right = ttk.Frame(root, style="TFrame"); root.pack(side="left", fill="both", expand=True, pady=8)

    title = ttk.Label(left, text="Student Input", font=("Segoe UI", 12, "bold")); title.pack(anchor="w", pady=(6,6), padx=8)
    frm = ttk.Frame(left, style="Tframe"); frm.pack(fill="x", padx=8)

    ttk.Label(frm, text="Roll No.").grid(row=0, column=0, sticky="w", padx=6, pady=6)
    self.roll_var = tk.StringVar(); ttk.Entry(frm, textvariable=self.roll_var, width=22).grid(row=0, column=1, padx=6, pady=6)

    ttk.Label(frm, text="Name").grid(row=0, column=2, sticky="w", padx=6, pady=6)
    self.name_var = tk.StringVar(); ttk.Entry(frm, textvariable=self.name_var, width=22).grid(row=0, column=3, padx=6, pady=6)

    ttk.Label(frm, text="Marks (0-100)").grid(row=1, column=0, sticky="w", padx=6, pady=(6,2))
    self.m1_var = tk.StringVar(); self.m2_var = tk.StringVar(); self.m3_var=tk.StringVar()
    ttk.Entry(frm, textvariable=self.m1_var, width=8).grid(row=1, column=1, sticky="w", padx=6, pady=2)
    ttk.Entry(frm, textvariable=self.m2_var, width=8).grid(row=1, column=2, sticky="w", padx=6, pady=2)
    ttk.Entry(frm, textvariable=self.m3_var, width=8).grid(row=1, column=3, sticky="w", padx=6, pady=2)
    
    btns = ttk.Frame(left, style="Tframe"); btns.pack(fill="x", pady=(10,6), padx=8)
    self.add_update_btn = ttk.Buttons(btns, text="Add / Update", command=self.add_or_update_student);
    self.add_update_btn.grid(row=0, column=0, padx=4, pady=4 sticky="ew)
    self.delete_btn = ttk.Buttons(btns, text="Delete", command=self.delete_student);
    self.delete_btn.grid(row=0, column=1, padx=4, pady=4 sticky="ew)
    self.clear_btn = ttk.Buttons(btns, text="Clear Inputs", command=self.clear_student);
    self.clear_btn.grid(row=0, column=2, padx=4, pady=4 sticky="ew)

    self.search_btn = ttk.Buttons(btns, text="Search", command=self.search_student);
    self.search_btn.grid(row=1, column=0, padx=4, pady=4 sticky="ew)

    self.topper_btn = ttk.Buttons(btns, text="Show Topper", command=self.show_topper);
    self.topper_btn.grid(row=1, column=1, padx=4, pady=4 sticky="ew)

    self.reset_btn = ttk.Buttons(btns, text="Reset All", command=self.reset_all);
    self.reset_btn.grid(row=1, column=2, padx=4, pady=4 sticky="ew)

    self.save_btn = ttk.Button(btns, text="Save CSV", command=self.save_to_csv);
    self.save_btn.grid(row=2, column=0, padx=4 pady=4, sticky="ew")    
    self.load_btn = ttk.Button(btns, text="Load CSV", command=self.load_from_csv);
    self.load_btn.grid(row=2, column=1, padx=4 pady=4, sticky="ew")    
    self.export_btn = ttk.Button(btns, text="Export Report", command=self.export_report);
    self.save_btn.grid(row=2, column=2, padx=4 pady=4, sticky="ew")    

