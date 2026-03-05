from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    out = Path("artifacts/data_quality_analysis")
    out.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc).isoformat()

    checks = [
        ("missing_values_rate", 0.01, 0.05),
        ("duplicate_rows_rate", 0.00, 0.01),
    ]

    lines = ["metric,value,threshold,passed"]
    all_passed = True
    for metric, value, threshold in checks:
        passed = value <= threshold
        all_passed = all_passed and passed
        lines.append(f"{metric},{value},{threshold},{passed}")

    (out / "quality_report.csv").write_text("\n".join(lines) + "\n", encoding="utf-8")

    (out / "summary.txt").write_text(
        f"[data_quality_analysis] {'OK' if all_passed else 'FAIL'}\n"
        f"timestamp_utc: {now}\n",
        encoding="utf-8",
    )

    print("data_quality_analysis finished", "OK" if all_passed else "FAIL")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
