from src.project import *

def test_bst_insert_search():
    bst = ArtifactBST()
    a1 = Artifact(1, "Mirror", "Cursed", 100, "A1")
    a2 = Artifact(2, "Key", "Rare", 50, "B1")

    assert bst.insert(a1) is True
    assert bst.insert(a2) is True
    assert bst.search_by_id(1) == a1
    assert bst.search_by_id(99) is None


def test_bst_duplicate():
    bst = ArtifactBST()
    a1 = Artifact(1, "Mirror", "Cursed", 100, "A1")
    a2 = Artifact(1, "Duplicate", "Rare", 200, "B1")

    assert bst.insert(a1) is True
    assert bst.insert(a2) is False


def test_queue_fifo():
    q = RestorationQueue()
    r1 = RestorationRequest(1, "Fix mirror")
    r2 = RestorationRequest(2, "Repair key")

    q.add_request(r1)
    q.add_request(r2)

    assert q.process_next_request() == r1
    assert q.process_next_request() == r2
    assert q.process_next_request() is None


def test_stack_lifo():
    s = ArchiveUndoStack()
    s.push_action("Action1")
    s.push_action("Action2")

    assert s.undo_last_action() == "Action2"
    assert s.undo_last_action() == "Action1"
    assert s.undo_last_action() is None


def test_linked_list_remove():
    route = ExhibitRoute()
    route.add_stop("Entrance")
    route.add_stop("Hall")
    route.add_stop("Moon Room")

    assert route.remove_stop("Hall") is True
    assert route.list_stops() == ["Entrance", "Moon Room"]
    assert route.remove_stop("Missing") is False


def test_category_count():
    artifacts = [
        Artifact(1, "A", "Magic", 10, "R1"),
        Artifact(2, "B", "Magic", 20, "R2"),
        Artifact(3, "C", "Rare", 30, "R1"),
    ]
    result = count_artifacts_by_category(artifacts)
    assert result == {"Magic": 2, "Rare": 1}


def test_unique_rooms():
    artifacts = [
        Artifact(1, "A", "Magic", 10, "R1"),
        Artifact(2, "B", "Rare", 20, "R2"),
        Artifact(3, "C", "Rare", 30, "R1"),
    ]
    assert unique_rooms(artifacts) == {"R1", "R2"}


def test_sort_by_age():
    artifacts = [
        Artifact(1, "A", "Magic", 30, "R1"),
        Artifact(2, "B", "Rare", 10, "R2"),
        Artifact(3, "C", "Rare", 20, "R3"),
    ]
    sorted_list = sort_artifacts_by_age(artifacts)
    assert [a.age for a in sorted_list] == [10, 20, 30]


def test_linear_search():
    artifacts = [
        Artifact(1, "Mirror", "Magic", 30, "R1"),
        Artifact(2, "Key", "Rare", 10, "R2"),
    ]
    assert linear_search_by_name(artifacts, "Key").artifact_id == 2
    assert linear_search_by_name(artifacts, "Missing") is None