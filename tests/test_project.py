from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.project import (
    ArchiveUndoStack,
    Artifact,
    ArtifactBST,
    ExhibitRoute,
    RestorationQueue,
    RestorationRequest,
    count_artifacts_by_category,
    linear_search_by_name,
    sort_artifacts_by_age,
    unique_rooms,
)


def test_bst_insert_search_and_duplicate():
    bst = ArtifactBST()
    mirror = Artifact(1, "Mirror", "Cursed", 100, "A1")
    key = Artifact(2, "Key", "Rare", 50, "B1")
    duplicate = Artifact(1, "Duplicate", "Rare", 200, "B1")

    assert bst.insert(mirror) is True
    assert bst.insert(key) is True
    assert bst.insert(duplicate) is False
    assert bst.search_by_id(1) == mirror
    assert bst.search_by_id(99) is None


def test_bst_traversals():
    bst = ArtifactBST()
    artifacts = [
        Artifact(4, "D", "Rare", 10, "R4"),
        Artifact(2, "B", "Rare", 10, "R2"),
        Artifact(6, "F", "Rare", 10, "R6"),
        Artifact(1, "A", "Rare", 10, "R1"),
        Artifact(3, "C", "Rare", 10, "R3"),
        Artifact(5, "E", "Rare", 10, "R5"),
        Artifact(7, "G", "Rare", 10, "R7"),
    ]
    for artifact in artifacts:
        bst.insert(artifact)

    assert bst.inorder_ids() == [1, 2, 3, 4, 5, 6, 7]
    assert bst.preorder_ids() == [4, 2, 1, 3, 6, 5, 7]
    assert bst.postorder_ids() == [1, 3, 2, 5, 7, 6, 4]


def test_bst_empty_traversals():
    bst = ArtifactBST()
    assert bst.inorder_ids() == []
    assert bst.preorder_ids() == []
    assert bst.postorder_ids() == []


def test_queue_fifo_and_empty_behaviors():
    queue = RestorationQueue()
    first = RestorationRequest(1, "Fix mirror")
    second = RestorationRequest(2, "Repair key")

    assert queue.is_empty() is True
    assert queue.peek_next_request() is None
    assert queue.process_next_request() is None

    queue.add_request(first)
    queue.add_request(second)

    assert queue.size() == 2
    assert queue.peek_next_request() == first
    assert queue.process_next_request() == first
    assert queue.process_next_request() == second
    assert queue.process_next_request() is None
    assert queue.is_empty() is True


def test_stack_lifo_and_empty_behaviors():
    stack = ArchiveUndoStack()

    assert stack.is_empty() is True
    assert stack.peek_last_action() is None
    assert stack.undo_last_action() is None

    stack.push_action("Action1")
    stack.push_action("Action2")

    assert stack.size() == 2
    assert stack.peek_last_action() == "Action2"
    assert stack.undo_last_action() == "Action2"
    assert stack.undo_last_action() == "Action1"
    assert stack.undo_last_action() is None


def test_linked_list_remove_cases_and_count():
    route = ExhibitRoute()
    assert route.remove_stop("Missing") is False
    assert route.list_stops() == []
    assert route.count_stops() == 0

    route.add_stop("Entrance")
    assert route.remove_stop("Entrance") is True
    assert route.list_stops() == []

    route.add_stop("Entrance")
    route.add_stop("Hall")
    route.add_stop("Moon Room")
    route.add_stop("Gift Shop")

    assert route.count_stops() == 4
    assert route.remove_stop("Entrance") is True
    assert route.list_stops() == ["Hall", "Moon Room", "Gift Shop"]
    assert route.remove_stop("Moon Room") is True
    assert route.list_stops() == ["Hall", "Gift Shop"]
    assert route.remove_stop("Gift Shop") is True
    assert route.list_stops() == ["Hall"]
    assert route.remove_stop("Missing") is False


def test_category_count_and_empty():
    artifacts = [
        Artifact(1, "A", "Magic", 10, "R1"),
        Artifact(2, "B", "Magic", 20, "R2"),
        Artifact(3, "C", "Rare", 30, "R1"),
    ]
    assert count_artifacts_by_category(artifacts) == {"Magic": 2, "Rare": 1}
    assert count_artifacts_by_category([]) == {}


def test_unique_rooms_and_empty():
    artifacts = [
        Artifact(1, "A", "Magic", 10, "R1"),
        Artifact(2, "B", "Rare", 20, "R2"),
        Artifact(3, "C", "Rare", 30, "R1"),
    ]
    assert unique_rooms(artifacts) == {"R1", "R2"}
    assert unique_rooms([]) == set()


def test_sort_by_age_ascending_descending_and_equal_age():
    artifacts = [
        Artifact(1, "A", "Magic", 30, "R1"),
        Artifact(2, "B", "Rare", 10, "R2"),
        Artifact(3, "C", "Rare", 20, "R3"),
        Artifact(4, "D", "Rare", 20, "R4"),
    ]

    ascending = sort_artifacts_by_age(artifacts)
    descending = sort_artifacts_by_age(artifacts, descending=True)

    assert [artifact.age for artifact in ascending] == [10, 20, 20, 30]
    assert [artifact.age for artifact in descending] == [30, 20, 20, 10]
    assert sort_artifacts_by_age([]) == []


def test_linear_search_found_missing_and_empty():
    artifacts = [
        Artifact(1, "Mirror", "Magic", 30, "R1"),
        Artifact(2, "Key", "Rare", 10, "R2"),
    ]
    assert linear_search_by_name(artifacts, "Key").artifact_id == 2
    assert linear_search_by_name(artifacts, "Missing") is None
    assert linear_search_by_name([], "Key") is None
