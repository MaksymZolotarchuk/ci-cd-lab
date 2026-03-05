from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    out = Path("artifacts/data_load")
    out.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc).isoformat()

    # приклад "результату" у CSV
    (out / "result.csv").write_text(
        "timestamp_utc,rows_loaded,source\n"
        f"{now},100,synthetic\n",
        encoding="utf-8",
    )

    (out / "summary.txt").write_text(
        f"[data_load] OK\n"
        f"timestamp_utc: {now}\n"
        f"rows_loaded: 100\n",
        encoding="utf-8",
    )

    print("data_load finished OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
