import sys
from pathlib import Path


REQUIRED_SPECS = [
    Path("specs/_meta.md"),
    Path("specs/functional.md"),
    Path("specs/technical.md"),
]


def main() -> int:
    missing = []
    for p in REQUIRED_SPECS:
        if not p.exists():
            missing.append(str(p))

    if missing:
        print("SPEC CHECK FAILED: Missing spec files:")
        for m in missing:
            print(" -", m)
        return 2

    # Basic content checks
    errors = []
    for p in REQUIRED_SPECS:
        text = p.read_text(encoding="utf-8")
        if len(text.strip()) < 20:
            errors.append(f"Spec {p} appears empty or too short")

    if errors:
        print("SPEC CHECK FAILED: Content issues:")
        for e in errors:
            print(" -", e)
        return 3

    print("SPEC CHECK OK: All required spec files present and non-empty.")
    return 0


if __name__ == "__main__":
    rc = main()
    sys.exit(rc)
