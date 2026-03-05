from datetime import datetime
from pathlib import Path

out = Path("artifacts/visualization")
out.mkdir(parents=True, exist_ok=True)

# мінімальна "візуалізація" як HTML
(out / "index.html").write_text(
    f"<html><body><h1>Visualization OK</h1><p>{datetime.now()}</p></body></html>",
    encoding="utf-8",
)
print("visualization finished (generated index.html)")
