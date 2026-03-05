from datetime import datetime
from pathlib import Path

out = Path("artifacts/data_load")
out.mkdir(parents=True, exist_ok=True)

(out / "run.txt").write_text(f"data_load ok @ {datetime.now()}\n", encoding="utf-8")
print("data_load finished")
