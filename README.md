# Student-Management-System
# Problem Statement
The core problem this project addresses is the difficulty small classes/teachers/registrars face when managing student records manually (paper registers, spreadsheets). Manual processes are slow, error-prone and hard to update or share. This simple CLI tool provides an easy, consistent way to add, view, search, update and delete student records so instructors and small admin teams can manage class data quickly without learning a heavy database system.

# Target Users
**Primary Users:**

Small-school teachers and college registrars who need a lightweight tool to track students.

**Secondary Users:**

Lab assistants or tutors who need quick lists of students and marks.

# Project Scope

**Student data management:** add, display, search, update, delete student records.

**Two modes:** in-memory mode (no persistence) and file mode (optional JSON persistence).

               Text/console interface with clear menus, prompts and tabular output.

               Usable on any system with Python 3.x and a terminal.

# Features

**Add Student:** Enter name, roll number, class, and marks (validated 0–100).

**Display All Students:** Tabular view with automatic column sizing and total count.

**Search by Roll Number:** Quickly lookup a student and show details.

**Update Student:** Edit name/class/marks while allowing blanks to keep existing values.

**Delete Student:** Confirmed deletion to avoid accidental removals.


Friendly CLI with colorized output using colorama for readability.

Simple, readable code suitable for extension (GUI, database, CSV export).

Overview
Registrar — Student Management System (CLI)
A compact console app that:

Lets you manage student records from the terminal.

Has an intuitive numbered menu and human-friendly prompts.

Provides both a transient (memory-only) demo and a persistent JSON-backed version.

Great for practice with OOP-style functions, input validation and basic data structures.

Tools Used
Python standard library: os, json (optional), sys
Third-party: colorama (for terminal colors)

Installation & Usage
Prerequisites

Python 3.x installed on your machine.

(Optional) colorama for colored text in terminal.

Install required module:

pip install colorama
