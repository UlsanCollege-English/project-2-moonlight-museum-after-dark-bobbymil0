# Moonlight Museum After Dark

## 1. Team Information
- Team Name: Moonlight Coders
- Member 1: Bobby Nepali
- Worked individually (solo project)

---

## 2. Short Project Summary
This project creates a museum management system for the Moonlight Museum’s late-night exhibition.  
The system organizes strange artifacts using a Binary Search Tree (BST), manages restoration requests with a queue, tracks undo actions with a stack, builds exhibit routes using a linked list, and generates reports with helper utility functions.

---

## 3. Feature Checklist
- [x] Artifact archive BST
- [x] Insert artifact
- [x] Search artifact by ID
- [x] Inorder traversal
- [x] Preorder traversal
- [x] Postorder traversal
- [x] Duplicate ID handling
- [x] Restoration request queue
- [x] Archive undo stack
- [x] Exhibit route linked list
- [x] Category counting
- [x] Unique rooms finder
- [x] Sort artifacts by age
- [x] Linear search by name
- [x] Integration demo function

---

## 4. Design Note
This project uses different data structures based on their strengths. The Binary Search Tree is used for artifact storage because it allows efficient searching and ordered traversal by artifact ID. The queue is used for restoration requests because requests must be processed in FIFO order. The stack is used for undo actions because the most recent action should be undone first. The singly linked list is used for exhibit routes because stops are added in sequence and can be removed easily. Dictionaries and sets are used in helper functions for counting categories and tracking unique rooms efficiently. These choices make the museum system organized, efficient, and easy to maintain.

---

## 5. Complexity Reasoning
- BST Insert/Search: O(log n) average, O(n) worst case
- BST Traversals: O(n)
- Queue Add/Process: O(1)
- Stack Push/Pop: O(1)
- Linked List Add: O(n)
- Linked List Remove: O(n)
- Category Count: O(n)
- Unique Rooms: O(n)
- Sort by Age: O(n log n)
- Linear Search by Name: O(n)

---

## 6. Edge-Case Checklist
- [x] Empty BST insert
- [x] Duplicate BST ID ignored
- [x] Search missing artifact
- [x] Empty queue process
- [x] Empty queue peek
- [x] Empty stack undo
- [x] Empty stack peek
- [x] Empty linked list remove
- [x] Remove first node
- [x] Remove middle node
- [x] Remove last node
- [x] Missing stop removal
- [x] Empty artifact helper functions

---

## 7. Demo Plan / How to Run

Run project demo:
```bash
python src/project.py