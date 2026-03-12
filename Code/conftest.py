import pytest

# global counters and failure log
counters = {}
failures = []


def get_category(item):
    """Infer a category name from the test item name."""
    name = item.name.lower()
    if name.startswith("test_login") or name.startswith("test_register") or name == "test_is_logged" or "blacklist" in name:
        return "auth"
    if "dispatch" in name:
        return "dispatch"
    if any(sub in name for sub in ["email_taken", "pk_duplicate", "fk_missing", "many_to_many"]):
        return "db"
    if name.startswith("test_create_media_routing") or name.startswith("test_update_media_not_found") or "media_metadata_edit" in name or "media_service_crud" in name or (name.startswith("test_media_") and "stress" not in name):
        return "media"
    if any(sub in name for sub in ["moderate", "publisher", "admin_can", "root_has", "mod_can"]):
        return "permissions"
    if "cascade" in name:
        return "cascade"
    if "comment" in name or "note" in name:
        return "comments"
    if name.startswith("test_edge"):
        return "edge"
    if name.startswith("test_stress"):
        return "stress"
    return "other"


def pytest_runtest_setup(item):
    cat = get_category(item)
    counters.setdefault(cat, 0)
    counters[cat] += 1
    print(f"--> running {item.name} [{cat}]")


def pytest_runtest_logreport(report):
    if report.when == "call" and report.outcome != "passed":
        failures.append((report.nodeid, report.outcome, report.longrepr))


def pytest_sessionfinish(session, exitstatus):
    print("\n=== CATEGORY SUMMARY ===")
    total = sum(counters.values())
    print(f"total tests executed: {total}")
    for cat, count in counters.items():
        print(f"  {cat}: {count}")
    if failures:
        print("\n=== FAILURES DETAIL ===")
        for nodeid, outcome, longrepr in failures:
            print(f"{nodeid} -> {outcome}")
            print(longrepr)
