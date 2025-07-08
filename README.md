# Distributed LMS with Raft-based Consistency and LLM Tutoring

This project is a distributed Learning Management System (LMS) implemented as part of the Advanced Operating Systems (CS G623) Assignment (Semester 1, 2024-25). It integrates core LMS functionalities, lightweight LLM-based tutoring support, and ensures data consistency using the Raft consensus protocol.

## 🧩 Components

### 1. **Client Nodes (Student & Instructor)**
- Authenticate via login/logout using token-based session management.
- Students can:
  - Submit assignments
  - Ask queries (to either instructor or LLM)
  - View course materials and grades
- Instructors can:
  - Grade student assignments
  - Upload course materials
  - Respond to queries

### 2. **LMS Server**
- Handles all student and instructor interactions.
- Stores grades, feedback, materials, and assignments.
- Communicates with tutoring server for LLM-based answers.
- Implements a simplified **Raft protocol** for consistent replication of grades and critical data across distributed servers.

### 3. **Tutoring Server**
- Uses a lightweight LLM (e.g., spaCy/NLTK) to provide real-time, context-aware tutoring responses to student queries.

### 4. **Raft Consensus Module**
- Implements core Raft RPCs:
  - `requestVote`, `requestVoteReply`
  - `appendEntries`, `appendEntriesReply`
- Handles leader election and log replication.
- Ensures fault-tolerant grade syncing across multiple LMS server nodes.

---

## ⚙️ Setup Instructions

### 🔧 Prerequisites
- Python 3.10+
- gRPC & Protocol Buffers
- spaCy/NLTK for the LLM module

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
python -m nltk.downloader all    # If using NLTK
python -m spacy download en_core_web_sm   # If using spaCy
