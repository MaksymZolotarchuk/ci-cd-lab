from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    out = Path("artifacts/visualization")
    out.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc).isoformat()

    html = f"""<!doctype html>
<html lang="uk">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Visualization</title>
  <style>
    body {{ font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 24px; }}
    .card {{ padding: 16px; border: 1px solid #ddd; border-radius: 12px; max-width: 720px; }}
    code {{ background: #f6f8fa; padding: 2px 6px; border-radius: 6px; }}
  </style>
</head>
<body>
  <div class="card">
    <h1>Visualization OK</h1>
    <p>Generated at <code>{now}</code> (UTC)</p>
    <p>Artifact path: <code>artifacts/visualization/index.html</code></p>
  </div>
</body>
</html>
"""

    (out / "index.html").write_text(html, encoding="utf-8")
    (out / "summary.txt").write_text(f"[visualization] OK\ntimestamp_utc: {now}\n", encoding="utf-8")

    print("visualization finished OK (index.html generated)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
