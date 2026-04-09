from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from typing import Deque


@dataclass(frozen=True)
class Artifact:
    artifact_id: int
    name: str
    category: str
    age: int
    room: str


@dataclass(frozen=True)
class RestorationRequest:
    artifact_id: int
    description: str


class TreeNode:
    def __init__(self, artifact, left=None, right=None):
        self.artifact = artifact
        self.left = left
        self.right = right


class ArtifactBST:
    def __init__(self):
        self.root = None

    def insert(self, artifact):
        if self.root is None:
            self.root = TreeNode(artifact)
            return True

        current = self.root
        while True:
            if artifact.artifact_id == current.artifact.artifact_id:
                return False
            elif artifact.artifact_id < current.artifact.artifact_id:
                if current.left is None:
                    current.left = TreeNode(artifact)
                    return True
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(artifact)
                    return True
                current = current.right

    def search_by_id(self, artifact_id):
        current = self.root
        while current:
            if artifact_id == current.artifact.artifact_id:
                return current.artifact
            elif artifact_id < current.artifact.artifact_id:
                current = current.left
            else:
                current = current.right
        return None

    def inorder_ids(self):
        result = []

        def traverse(node):
            if node:
                traverse(node.left)
                result.append(node.artifact.artifact_id)
                traverse(node.right)

        traverse(self.root)
        return result

    def preorder_ids(self):
        result = []

        def traverse(node):
            if node:
                result.append(node.artifact.artifact_id)
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)
        return result

    def postorder_ids(self):
        result = []

        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                result.append(node.artifact.artifact_id)

        traverse(self.root)
        return result


class RestorationQueue:
    def __init__(self):
        self._items = deque()

    def add_request(self, request):
        self._items.append(request)

    def process_next_request(self):
        if self.is_empty():
            return None
        return self._items.popleft()

    def peek_next_request(self):
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)


class ArchiveUndoStack:
    def __init__(self):
        self._items = []

    def push_action(self, action):
        self._items.append(action)

    def undo_last_action(self):
        if self.is_empty():
            return None
        return self._items.pop()

    def peek_last_action(self):
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)


class ExhibitNode:
    def __init__(self, stop_name, next_node=None):
        self.stop_name = stop_name
        self.next = next_node


class ExhibitRoute:
    def __init__(self):
        self.head = None

    def add_stop(self, stop_name):
        new_node = ExhibitNode(stop_name)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_stop(self, stop_name):
        current = self.head
        previous = None

        while current:
            if current.stop_name == stop_name:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        return False

    def list_stops(self):
        stops = []
        current = self.head
        while current:
            stops.append(current.stop_name)
            current = current.next
        return stops

    def count_stops(self):
        return len(self.list_stops())


def count_artifacts_by_category(artifacts):
    counts = {}
    for artifact in artifacts:
        counts[artifact.category] = counts.get(artifact.category, 0) + 1
    return counts


def unique_rooms(artifacts):
    return {artifact.room for artifact in artifacts}


def sort_artifacts_by_age(artifacts, descending=False):
    return sorted(artifacts, key=lambda x: x.age, reverse=descending)


def linear_search_by_name(artifacts, name):
    for artifact in artifacts:
        if artifact.name == name:
            return artifact
    return None


def demo_museum_night():
    print("Moonlight Museum Demo Running")

    artifacts = [
        Artifact(1, "Mirror", "Cursed", 100, "A1"),
        Artifact(2, "Clock Bird", "Clockwork", 50, "B1"),
        Artifact(3, "Whisper Map", "Magic", 75, "C1"),
        Artifact(4, "Golden Key", "Rare", 200, "A2"),
        Artifact(5, "Silver Mask", "Ancient", 300, "D1"),
        Artifact(6, "Ghost Lamp", "Haunted", 90, "E1"),
        Artifact(7, "Moon Stone", "Rare", 500, "F1"),
        Artifact(8, "Shadow Ring", "Magic", 150, "G1"),
    ]

    bst = ArtifactBST()
    for a in artifacts:
        bst.insert(a)

    print("Inorder:", bst.inorder_ids())
    print("Search ID 3:", bst.search_by_id(3))
    print("Search ID 99:", bst.search_by_id(99))

    queue = RestorationQueue()
    queue.add_request(RestorationRequest(1, "Repair crack"))
    print(queue.process_next_request())

    stack = ArchiveUndoStack()
    stack.push_action("Added Mirror")
    print(stack.undo_last_action())

    route = ExhibitRoute()
    route.add_stop("Entrance")
    route.add_stop("Mirror Hall")
    route.add_stop("Moon Room")
    print(route.list_stops())

    print(count_artifacts_by_category(artifacts))
    print(unique_rooms(artifacts))

if __name__ == "__main__":
    demo_museum_night()