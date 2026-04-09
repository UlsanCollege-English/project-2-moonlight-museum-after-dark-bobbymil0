# Moonlight Museum After Dark

## 1. Team Information
- Team Name: Moonlight Coders
- Member 1: Bobby Nepali
- Worked individually (solo project)

---

## 2. Short Project Summary
This project builds a museum archive and operations toolkit for the Moonlight Museum's late-night exhibit. It uses multiple core data structures to solve different problems: a Binary Search Tree for storing artifacts by ID, a queue for restoration requests, a stack for undo history, and a singly linked list for guided route stops. Utility functions provide category counts, unique room reports, sorting by age, and name-based searching. A demo function ties everything together and prints sample outputs so behavior can be seen quickly.

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
The design uses each data structure where it naturally fits the museum workflow. The Binary Search Tree stores artifacts by `artifact_id`, which keeps IDs organized for fast average-case lookup and supports recursive traversals that return meaningful display orders. This is useful for administrative views that need sorted IDs (`inorder`) or structural snapshots (`preorder` and `postorder`). Restoration tasks are time-ordered, so a FIFO queue is the right model: newly submitted work goes to the back while the oldest pending request is processed first. Undo history is fundamentally last-in-first-out, so a stack gives the cleanest way to reverse recent archive changes safely.  

The guided exhibit route is modeled as a singly linked list because stops are visited in sequence and removals often target the first matching stop. This keeps pointer logic explicit for list operations covered in class. Utility helpers then use built-in Python collections for concise reporting: a dictionary for counting categories, a set for unique rooms, `sorted()` for age ordering, and linear search for exact-name lookup. Together, this architecture balances readability, correctness, and alignment with course goals, while keeping implementations small and testable.

---

## 5. Complexity Reasoning
- BST insert/search: `O(log n)` average, `O(n)` worst case
- BST traversals: `O(n)`
- Queue add/process/peek: `O(1)`
- Stack push/undo/peek: `O(1)`
- Linked list add stop: `O(n)`
- Linked list remove stop: `O(n)`
- Category count: `O(n)`
- Unique rooms: `O(n)`
- Sort by age: `O(n log n)`
- Linear search by name: `O(n)`

---

## 6. Edge-Case Checklist
- [x] Empty BST traversals return empty lists
- [x] Insert into empty BST
- [x] Duplicate BST ID ignored
- [x] Search missing artifact ID
- [x] Empty queue process returns `None`
- [x] Empty queue peek returns `None`
- [x] Empty stack undo returns `None`
- [x] Empty stack peek returns `None`
- [x] Empty linked list remove returns `False`
- [x] Remove first linked-list node
- [x] Remove middle linked-list node
- [x] Remove last linked-list node
- [x] Remove from one-stop route
- [x] Missing stop removal returns `False`
- [x] Empty helper inputs return empty results
- [x] Missing artifact name search returns `None`

---

## 7. Demo Plan / How to Run
Run the integration demo:

```bash
python src/project.py
```

Run tests:

```bash
python -m pytest -q
```

---

## 8. Assistance & Sources
- Course lecture notes and project brief (`PROJECT_2_BRIEF.md`)
- Python standard library docs:
  - `dataclasses`: https://docs.python.org/3/library/dataclasses.html
  - `collections.deque`: https://docs.python.org/3/library/collections.html#collections.deque
- Development/testing support: Codex CLI assistant used for debugging and README/test cleanup
