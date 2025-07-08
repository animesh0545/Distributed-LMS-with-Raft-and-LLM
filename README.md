# 📚 Distributed LMS with Raft-based Consistency and LLM Tutoring

This repository contains the implementation of a distributed Learning Management System (LMS) built as part of the **Advanced Operating Systems (CS G623)** course assignment at BITS Pilani (Semester 1, 2024-25).

It features:
- Real-time student-instructor interactions via gRPC
- A lightweight LLM-based tutoring server
- A simplified Raft consensus protocol for consistent and fault-tolerant grade storage

---

## 🚀 Features

### 👨‍🎓 Student
- Login/logout with token
- Submit assignments
- View grades and course materials
- Ask course-related questions (to instructor or LLM)

### 👩‍🏫 Instructor
- Login/logout with token
- Upload materials
- Grade assignments and provide feedback
- Answer student queries

### 🤖 Tutoring Server (LLM)
- Lightweight NLP-based tutoring responses using spaCy or NLTK
- Context-aware answering via `getLLMAnswer`

### 🔁 Raft Consensus
- Ensures consistency of critical data (grades, feedback) across LMS nodes
- Supports leader election, log replication, and node failure recovery

---

## 🧩 System Architecture

| Node | Role |
|------|------|
| Node 1 | Tutoring Server (LLM) |
| Node 2 | LMS Server (Raft Leader) |
| Node 3 | LMS Server (Raft Follower) |
| Node 4 | Additional LMS Follower |
| Node 5 | Client (Student or Instructor) |

---

## 🗂️ Folder Structure

```text
.
├── client/
│   ├── student_client.py
│   └── instructor_client.py
├── server/
│   ├── lms_server.py
│   ├── tutoring_server.py
│   └── raft/
│       ├── raft_node.py
│       └── raft_utils.py
├── proto/
│   └── lms.proto
├── data/
│   ├── assignments/
│   ├── grades/
│   └── materials/
├── requirements.txt
├── .gitignore
└── README.md


