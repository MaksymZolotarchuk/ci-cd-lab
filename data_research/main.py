from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import statistics


def main() -> int:
    out = Path("artifacts/data_research")
    out.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc).isoformat()

    data = [10, 12, 9, 11, 13, 8, 10, 12]
    mean = statistics.mean(data)
    stdev = statistics.pstdev(data)

    (out / "stats.txt").write_text(
        f"[data_research] OK\n"
        f"timestamp_utc: {now}\n"
        f"n: {len(data)}\n"
        f"mean: {mean:.3f}\n"
        f"stdev: {stdev:.3f}\n",
        encoding="utf-8",
    )

    print("data_research finished OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
