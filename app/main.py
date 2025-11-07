from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
from . import operations as ops
from .logger import logger
from .settings import settings

app = FastAPI(title=settings.app_name)

INDEX_HTML = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>FastAPI Calculator</title>
  <style>
    body{font-family:system-ui,Arial;padding:2rem;max-width:720px;margin:auto}
    .card{border:1px solid #eee;border-radius:12px;padding:1rem;box-shadow:0 2px 8px #0001}
    input,select,button{font-size:1rem;padding:.5rem;margin:.25rem 0}
  </style>
</head>
<body>
  <h1>FastAPI Calculator</h1>
  <div class="card">
    <label>First number</label>
    <input id="a" type="number" step="any" value="2"/>
    <label>Second number</label>
    <input id="b" type="number" step="any" value="3"/>
    <label>Operation</label>
    <select id="op">
      <option value="add">Add</option>
      <option value="subtract">Subtract</option>
      <option value="multiply">Multiply</option>
      <option value="divide">Divide</option>
    </select>
    <button id="go">Calculate</button>
    <p><strong>Result:</strong> <span id="out">—</span></p>
  </div>
  <script>
    async function calc(){
      const a = document.getElementById('a').value
      const b = document.getElementById('b').value
      const op = document.getElementById('op').value
      const url = `/api/${op}?a=${encodeURIComponent(a)}&b=${encodeURIComponent(b)}`
      const res = await fetch(url)
      const data = await res.json()
      document.getElementById('out').textContent = data.result
    }
    document.getElementById('go').addEventListener('click', calc)
  </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return INDEX_HTML

@app.get("/api/add")
async def api_add(a: float = Query(...), b: float = Query(...)):
    logger.info("ADD a=%s b=%s", a, b)
    try:
        return {"result": str(ops.add(a, b))}
    except Exception as e:
        logger.exception("Error in add")
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/subtract")
async def api_sub(a: float = Query(...), b: float = Query(...)):
    logger.info("SUB a=%s b=%s", a, b)
    try:
        return {"result": str(ops.subtract(a, b))}
    except Exception as e:
        logger.exception("Error in subtract")
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/multiply")
async def api_mul(a: float = Query(...), b: float = Query(...)):
    logger.info("MUL a=%s b=%s", a, b)
    try:
        return {"result": str(ops.multiply(a, b))}
    except Exception as e:
        logger.exception("Error in multiply")
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/divide")
async def api_div(a: float = Query(...), b: float = Query(...)):
    logger.info("DIV a=%s b=%s", a, b)
    try:
        return {"result": str(ops.divide(a, b))}
    except Exception as e:
        logger.exception("Error in divide")
        raise HTTPException(status_code=400, detail=str(e))