"""Project 2 starter code: Moonlight Museum After Dark.

Students should implement all required behavior in this file.
Use stdlib only.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Deque


@dataclass(frozen=True)
class Artifact:
    """A museum artifact stored in the archive BST."""

    artifact_id: int
    name: str
    category: str
    age: int
    room: str


@dataclass(frozen=True)
class RestorationRequest:
    """A request to inspect or repair an artifact."""

    artifact_id: int
    description: str


class TreeNode:
    """A node for the artifact BST."""

    def __init__(
        self,
        artifact: Artifact,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.artifact = artifact
        self.left = left
        self.right = right


class ArtifactBST:
    """Binary search tree keyed by artifact_id."""

    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def insert(self, artifact: Artifact) -> bool:
        """Insert an artifact.

        Return True if the artifact was inserted.
        Return False if an artifact with the same ID already exists.
        """
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

    def search_by_id(self, artifact_id: int) -> Artifact | None:
        """Return the matching artifact, or None if it does not exist."""
        current = self.root
        while current is not None:
            if artifact_id == current.artifact.artifact_id:
                return current.artifact
            elif artifact_id < current.artifact.artifact_id:
                current = current.left
            else:
                current = current.right
        return None

    def inorder_ids(self) -> list[int]:
        """Return a list of artifact IDs using inorder traversal."""
        result: list[int] = []

        def traverse(node: TreeNode | None) -> None:
            if node is not None:
                traverse(node.left)
                result.append(node.artifact.artifact_id)
                traverse(node.right)

        traverse(self.root)
        return result

    def preorder_ids(self) -> list[int]:
        """Return a list of artifact IDs using preorder traversal."""
        result: list[int] = []

        def traverse(node: TreeNode | None) -> None:
            if node is not None:
                result.append(node.artifact.artifact_id)
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)
        return result

    def postorder_ids(self) -> list[int]:
        """Return a list of artifact IDs using postorder traversal."""
        result: list[int] = []

        def traverse(node: TreeNode | None) -> None:
            if node is not None:
                traverse(node.left)
                traverse(node.right)
                result.append(node.artifact.artifact_id)

        traverse(self.root)
        return result


class RestorationQueue:
    """FIFO queue of restoration requests."""

    def __init__(self) -> None:
        self._items: Deque[RestorationRequest] = deque()

    def add_request(self, request: RestorationRequest) -> None:
        """Add a request to the back of the queue."""
        self._items.append(request)

    def process_next_request(self) -> RestorationRequest | None:
        """Remove and return the next request, or None if the queue is empty."""
        if self.is_empty():
            return None
        return self._items.popleft()

    def peek_next_request(self) -> RestorationRequest | None:
        """Return the next request without removing it, or None if empty."""
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self) -> bool:
        """Return True if the queue has no requests."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return the number of queued requests."""
        return len(self._items)


class ArchiveUndoStack:
    """LIFO stack of recent archive actions."""

    def __init__(self) -> None:
        self._items: list[str] = []

    def push_action(self, action: str) -> None:
        """Push an action onto the stack."""
        self._items.append(action)

    def undo_last_action(self) -> str | None:
        """Remove and return the most recent action, or None if empty."""
        if self.is_empty():
            return None
        return self._items.pop()

    def peek_last_action(self) -> str | None:
        """Return the most recent action without removing it, or None if empty."""
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        """Return True if the stack has no actions."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return the number of stored actions."""
        return len(self._items)


class ExhibitNode:
    """A node in the singly linked exhibit route."""

    def __init__(
        self,
        stop_name: str,
        next_node: ExhibitNode | None = None,
    ) -> None:
        self.stop_name = stop_name
        self.next = next_node


class ExhibitRoute:
    """Singly linked list of exhibit stops."""

    def __init__(self) -> None:
        self.head: ExhibitNode | None = None

    def add_stop(self, stop_name: str) -> None:
        """Add a stop to the end of the route."""
        new_node = ExhibitNode(stop_name)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def remove_stop(self, stop_name: str) -> bool:
        """Remove the first matching stop.

        Return True if a stop was removed.
        Return False if the stop does not exist.
        """
        current = self.head
        previous = None

        while current is not None:
            if current.stop_name == stop_name:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True

            previous = current
            current = current.next

        return False

    def list_stops(self) -> list[str]:
        """Return the route as a list of stop names in order."""
        stops: list[str] = []
        current = self.head

        while current is not None:
            stops.append(current.stop_name)
            current = current.next

        return stops

    def count_stops(self) -> int:
        """Return the number of stops in the route."""
        return len(self.list_stops())


def count_artifacts_by_category(artifacts: list[Artifact]) -> dict[str, int]:
    """Return a dictionary counting artifacts in each category."""
    counts: dict[str, int] = {}
    for artifact in artifacts:
        counts[artifact.category] = counts.get(artifact.category, 0) + 1
    return counts


def unique_rooms(artifacts: list[Artifact]) -> set[str]:
    """Return a set of all rooms used by the given artifacts."""
    return {artifact.room for artifact in artifacts}


def sort_artifacts_by_age(
    artifacts: list[Artifact],
    descending: bool = False,
) -> list[Artifact]:
    """Return a new list of artifacts sorted by age.

    If descending is False, sort from youngest to oldest.
    If descending is True, sort from oldest to youngest.
    """
    return sorted(artifacts, key=lambda artifact: artifact.age, reverse=descending)


def linear_search_by_name(
    artifacts: list[Artifact],
    name: str,
) -> Artifact | None:
    """Return the first artifact with an exact matching name, or None."""
    for artifact in artifacts:
        if artifact.name == name:
            return artifact
    return None


def demo_museum_night() -> None:
    """Run a small integration demo showing the system working together."""
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
    for artifact in artifacts:
        bst.insert(artifact)

    print("Inorder:", bst.inorder_ids())
    print("Preorder:", bst.preorder_ids())
    print("Postorder:", bst.postorder_ids())
    print("Search ID 3:", bst.search_by_id(3))
    print("Search ID 99:", bst.search_by_id(99))

    queue = RestorationQueue()
    queue.add_request(RestorationRequest(1, "Repair crack"))
    queue.add_request(RestorationRequest(3, "Clean whisper dust"))
    print("Next request:", queue.peek_next_request())
    print("Processed request:", queue.process_next_request())

    stack = ArchiveUndoStack()
    stack.push_action("Added Mirror")
    stack.push_action("Moved Golden Key")
    print("Last action:", stack.peek_last_action())
    print("Undo action:", stack.undo_last_action())

    route = ExhibitRoute()
    route.add_stop("Entrance")
    route.add_stop("Mirror Hall")
    route.add_stop("Moon Room")
    print("Route:", route.list_stops())

    print("Category counts:", count_artifacts_by_category(artifacts))
    print("Unique rooms:", unique_rooms(artifacts))


if __name__ == "__main__":
    demo_museum_night()