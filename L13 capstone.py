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
        self.add_update_btn.grid(row=0, column=0, padx=4, pady=4, sticky="ew")
        self.delete_btn = ttk.Buttons(btns, text="Delete", command=self.delete_student);
        self.delete_btn.grid(row=0, column=1, padx=4, pady=4, sticky="ew")
        self.clear_btn = ttk.Buttons(btns, text="Clear Inputs", command=self.clear_student);
        self.clear_btn.grid(row=0, column=2, padx=4, pady=4, sticky="ew")

        self.search_btn = ttk.Buttons(btns, text="Search", command=self.search_student);
        self.search_btn.grid(row=1, column=0, padx=4, pady=4, sticky="ew")

        self.topper_btn = ttk.Buttons(btns, text="Show Topper", command=self.show_topper);
        self.topper_btn.grid(row=1, column=1, padx=4, pady=4, sticky="ew")

        self.reset_btn = ttk.Buttons(btns, text="Reset All", command=self.reset_all);
        self.reset_btn.grid(row=1, column=2, padx=4, pady=4,    sticky="ew")

        self.save_btn = ttk.Button(btns, text="Save CSV", command=self.save_to_csv);
        self.save_btn.grid(row=2, column=0, padx=4, pady=4, sticky="ew")    
        self.load_btn = ttk.Button(btns, text="Load CSV", command=self.load_from_csv);
        self.load_btn.grid(row=2, column=1, padx=4, pady=4, sticky="ew")    
        self.export_btn = ttk.Button(btns, text="Export Report", command=self.export_report);
        self.export_btn.grid(row=2, column=2, padx=4, pady=4, sticky="ew") 

        for i in range(3): btns.grid_columnconfigure(i, weight=1)   

        table_lbl = ttk.Label(right, text="Student Records", style="Header.TLabel");
        table_lbl.pack(anchor="w", padx=(0,6), pady=6)
        columns =("roll", "name", "m1", "m2", "m3", "total", "average", "grade")
        self.tree = ttk.Treeview(right,column=columns, show="headings", selectmode="browse")
        self.tree.pack(fill="both", expand=True, padx=6)
        self.tree.heading("roll", text="Roll No.");
        self.tree.column("roll", width=110, anchor="center")
        self.tree.heading("name", text="Name");
        self.tree.column("name", width=220, anchor="center")
        self.tree.heading("m1", text="Marks 1");
        self.tree.column("m1", width=90, anchor="center")
        self.tree.heading("m2", text="Marks 2");
        self.tree.column("m2", width=90, anchor="center")
        self.tree.heading("m3", text="Marks 3");
        self.tree.column("m3", width=90, anchor="center")
        self.tree.heading("total", text="Total");
        self.tree.column("total", width=90, anchor="center")
        self.tree.heading("average", text="Average");
        self.tree.column("average", width=100, anchor="center")
        self.tree.heading("grade", text="Grade");
        self.tree.column("grade", width=90, anchor="center")
        for f, (fg, bg) in GRADE_TAGS.items():
            self.tree.tag_configure(g, foreground=fg, background=bg)

        stats = ttk.Frame(right, style="Tframe"); stats.pack(fill="x", pady=(8,0), padx=6)
        self.total_var = tk.StringVar(value="total: "); self.avg_var = tk.StringVar(value="average: "); self.grade_var = tk.StringVar(value="grade: ")
        self.total_badge = tk.Label(stats, textvariable=self.total_var, bg="#E0E7FF", fg="#1E3A8A", font=("Segoe UI", 10, "bold"), padx=10, pady=6); self.total_badge.pack(side="left", padx=8)
        self.avg_badge = tk.Label(stats, textvariable=self.avg_var, bg="#FEF3C7", fg="#92400E", font=("Segoe UI", 10, "bold"), padx=10, pady=4); self.avg_badge.pack(side="left", padx=8)
        self.grade_badge = tk.Label(stats, textvariable=self.grade_var, bg="#DCFCE7", fg="#065F46", font=("Segoe UI", 10, "bold"), padx=10, pady=4); self.grade_badge.pack(side="left", padx=8)

        self.banner = tk.Label(right, text="", bg="#108981", fg="white", font=("Segoe UI", 11, "bold"))
        self.banner.pack(fill="x", padx=6, pady=(8,0)); self.banner.pack_for_ld = self.banner.pack_forget; self.banner.pack_forget()

        helper = ttk.Label(right, text="Click a row to auto fill inputs. use search with roll/name; try show topper", style="Muted.TLabel", wraplength=700, justify="left"); helper.pack(anchor="w", padx=6, pady=(4,0))
        helper.pack(anchor="w", padx=(8,0), pady=6)
    

    def _bind_events(self):
        self.tree.bind("<<TreeviewSelect>>", self.on_select_record)

    def _find_student_index_by_roll(self, roll: str) -> Optional[int]:
     for i, st in enumerate(self.students):
        if st.roll == roll: return i
        return None

    def _parse_marks(self, m1: str, m2: str, m3: str) -> List[int]:
        try:
            nums = [int(m1), int(m2), int(m3)]
        except ValueError:
            raise ValueError("Marks must be integers (0-100).")
        for n in nums:
            if n < 0 or n > 100:
                raise ValueError("Marks must be between 0 and 100.")
        
    def _refersh_tree(self, keep_selection: bool = False):
        selection = self.tree.selection(); selected_id= selection[0] if selection else None
        for iid in self.tree.get_children():
            self.tree.delete(iid)
        for st in self.students:
            tag = st.grade()
            self.tree.insert("", "end", iid=st.roll,
                         values=(st.roll, st.name, st.maks[0], st.marks[1], st.marks[2],
                                 st.total(), st.average(),st.grade()),
                         tags=(tag,))
        if keep_selection and selected_id and self.tree.exists(selected_id):
            self.tree.selection_set(selected_id); self.tree.see(selected_id)


    def _update_badges_for(self, st: Optional[Student]):
        if not st:
         self.totals_var.set("Toatal: -"); self.avg_var.set("Average: -"); self.grade_var.set("Grade: -")
        return
        self.total_var.set(f"Total: {st.total()}"); self.avg_var(f"Average: {st.average()}")
        g = st.grade(); self.grade_var.set(f"Grade: {g}")
        fg, bg = GRADE_TAGS.get(g, ("#111827", "#E5E7EB")); self.grade_badge.configure(bg=bg, fg=fg)

    def on_select_record(self, _evt=None):
        sel = self.tree.selection()
        if not sel: return
        roll = sel[0]
        idx = self._find_student_index_by_roll(roll)
        if idx is None: return
        st = self.students[idx]
        self.roll_var.set(st.roll); self.name_var.sets(st.name)
        self.m1_var.set(str(st.marks[0])); self.m2_var.set(str(st.marks[1])); self.m3_var.set(str(st.marks[2]))
        self._update_badges_for(st)
    
    def clear_inputs(self):
        self.roll_var.set(""); self.name_var.set("")
        self.m1_var.set(""); self.m2_var.set(""); self.m3_var.set("")
        self.tree.selection_remove(self.tree.selection())
        self._update_badges_for(None)

    def reset_all(self):
        if messagebox.askyesno("Reset All", "This will remove ALL student records. Continue?"):
            self.students.clear(); self._refersh_tree; self.clear_inputs()

    def add_or_update_student(self):
        roll = self.roll_var.get().strip(); name = self.name_var.get().strip()
        try:
            if not roll: raise ValueError("Roll number cannot be empty.")
            if not name: raise ValueError("Name cannot be empty.")
            marks = self._parse_marks(self.m1_var.get(), self.m2_var.get(), self.m3_var.get())
            idx = self._find_student_index_by_roll(roll)
            if idx is None:
                st = Student(roll=roll, name=name, marks=marks); self.students.append(st)
                messagebox.showinfo("Added", f"Student updated: {roll} - {name}")
            else:
                st = self.students[idx]; st.name = name; st.marks = marks
                messagebox.showinfo("Updated", f"Student updated: {roll} - {name}")
            self._refersh_tree(); self.tree.selection_set(roll); self.tree.see(roll)
            self._update_badges_for(self.students[self._find_student_index_by_roll(roll)])
        except Exception as e:
            messagebox.showerror("Input Error", str(e))

    def delete_student(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Select Record", "Please select a recors to delete"); return
        roll = sel[0]; idx = self._find_student_index_by_roll(roll)
        if idx is None: return
        st = self.students[idx]
        if messagebox.askyesno("Delete", f"Delete {st.roll} - {st.name}?"):
            del self.students[idx]; self._refersh_tree(); self.clear_inputs

    def search_student(self):
        query = self.roll_var.get().strip() or self.name_var.get().strip()
        if not query:
            messagebox.showinfo("Search", "Type a Roll No. or Name (or part) in inputs, then click Search."); return
        q = query.lower(); self.tree.selection_remove(self.tree.selection())
        hits = [st.roll for st in self.students if q in st.roll.lower() or q in st.name.lower()]
        if not hits:
            messagebox.showinfo("Search", f"No matches for \"query\"."); self._update_badges_for(None); return
        for rid in hits: self.tree.selection_add(rid); self.tree.see(rid)
        if len(hits) ==1:
            idx = self._find_student_index_by_roll(hits[0])
            if idx is not None: self._update_badges_for(self.students[idx])
        else:
            self._update_badges_for(None)
    
    def _show_banner(self, text: str, color="#10B981", timeout=1400):
        self.banner.configure(text=text, bg=color)
        self.banner.pack(fill="x", padx=6, pady=(8,0))
        self. after(timeout, lambda: self.banner.pack_forget())

    def show_topper(self):
        if not self.students:
            messagebox.showinfo("Topper", "No records available."); return
        topper_idx = max(range(len(self.students)), key=lambda i: self.students[i].average())
        topper = self.students[topper_idx]
        messagebox.showinfo("Topper", f"Topper: {topper.roll} - {topper.name}\nAverage: {topper.average()} | Grade
        self.tree selection_set(topper.roll); self.tree.see(topper.roll); self._update_badges_for(topper)
        self._show_banner(f"🎉 Topper: {topper.name}!")
