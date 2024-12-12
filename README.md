# Teacher-Student Management System

A Django-based web application designed to help educational administrators manage teacher and student data effectively. The system establishes a one-to-many relationship between teachers and students, where each teacher can manage multiple students, and each student is linked to a specific teacher.

---

## Features

### 1. **Teacher Management**
- Add, view, edit, and delete teacher records.
- Attributes: `name`, `email`, `subject`.
- View all students assigned to a specific teacher.

### 2. **Student Management**
- Add, view, edit, and delete student records.
- Attributes: `name`, `age`, and a ForeignKey to the Teacher model.
- Each student is linked to one teacher.

### 3. **Relationship Management**
- Each teacher can have multiple students.
- A student can only be linked to one teacher.

---

## Database Design

The application uses Django ORM to implement the following models:

### Teacher Model
- `name`: String field for the teacher's name.
- `email`: String field for the teacher's email.
- `subject`: String field for the teacher's subject.

### Student Model
- `name`: String field for the student's name.
- `age`: Integer field for the student's age.
- `teacher`: ForeignKey field linking the student to a teacher.

### ERD Diagram
![ERD Diagram](path/to/your-erd-diagram.png)

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/teacher-student-management.git
   cd teacher-student-management
