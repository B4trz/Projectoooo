# app.py
import os
import time
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- Config desde environment ---
# SERVER_ID debe ser "LOCAL" o "CLOUD" según la VM
SERVER_ID = os.environ.get("SERVER_ID", "LOCAL")

# Simulación de delay: si SIMULATE_DELAY == "1" activa los sleeps
SIMULATE_DELAY = os.environ.get("SIMULATE_DELAY", "1") == "1"

# Parámetros de delay (ajustables por env)
MIN_DELAY_PRE = float(os.environ.get("MIN_DELAY_PRE", "1.0"))
MAX_DELAY_PRE = float(os.environ.get("MAX_DELAY_PRE", "1.5"))
MIN_DELAY_PROC = float(os.environ.get("MIN_DELAY_PROC", "0.1"))
MAX_DELAY_PROC = float(os.environ.get("MAX_DELAY_PROC", "0.5"))

# Función para retornar server id (usa en templates)
def get_server_id():
    return SERVER_ID

# ------------------ RUTAS ------------------

# Página A - Bienvenida
@app.route("/")
def pagina_a():
    server_id = get_server_id()
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Bienvenida - Sistema de Notas</title>
    <meta charset="utf-8">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background:#f5f5f5; }}
        .container {{ max-width:800px; margin:0 auto; background:#fff; padding:30px; border-radius:10px; box-shadow:0 2px 10px rgba(0,0,0,0.1); }}
        .server-info {{ background:#e9ecef; padding:15px; border-radius:5px; margin:20px 0; border-left:4px solid #007bff; }}
        h1 {{ color:#2c3e50; border-bottom:2px solid #3498db; padding-bottom:10px; }}
        button {{ padding:12px 24px; font-size:16px; background:#007bff; color:#fff; border:none; border-radius:5px; cursor:pointer; }}
        button:hover {{ background:#0056b3; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Sistema de Gestión de Notas</h1>
        <div class="server-info"><strong>Servidor:</strong> {server_id}</div>
        <p>Bienvenido al sistema de acceso masivo para procesos académicos.</p>
        <p>Esta demostración simula balanceo entre servidores LOCAL y CLOUD.</p>
        <a href="/login"><button>Acceder al Sistema</button></a>
    </div>
</body>
</html>"""
    return html

# Página B - Login (GET muestra el formulario, POST redirige a dashboard)
@app.route("/login", methods=["GET"])
def pagina_b():
    server_id = get_server_id()
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Inicio de Sesión - Sistema de Notas</title>
    <meta charset="utf-8">
    <style>
        body {{ font-family:Arial, sans-serif; margin:40px; background:#f5f5f5; }}
        .container {{ max-width:500px; margin:0 auto; background:#fff; padding:30px; border-radius:10px; box-shadow:0 2px 10px rgba(0,0,0,0.1); }}
        .server-info {{ background:#e9ecef; padding:15px; border-radius:5px; margin:20px 0; border-left:4px solid #28a745; }}
        input {{ padding:12px; margin:5px 0; width:100%; border:1px solid #ddd; border-radius:5px; box-sizing:border-box; }}
        button {{ padding:12px 24px; font-size:16px; background:#28a745; color:#fff; border:none; border-radius:5px; width:100%; cursor:pointer; }}
        button:hover {{ background:#218838; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Autenticación de Usuario</h1>
        <div class="server-info"><strong>Servidor:</strong> {server_id}</div>
        <form action="/dashboard" method="post">
            <label for="usuario"><strong>Usuario:</strong></label>
            <input type="text" id="usuario" name="usuario" placeholder="Ingrese su usuario" required>
            <label for="password"><strong>Contraseña:</strong></label>
            <input type="password" id="password" name="password" placeholder="Ingrese su contraseña" required>
            <div style="margin-top:15px;">
                <button type="submit">Iniciar Sesión</button>
            </div>
        </form>
        <div style="margin-top:12px; font-size:12px; color:#6c757d;">
            Nota: para pruebas usa cualquier usuario/contraseña.
        </div>
    </div>
</body>
</html>"""
    return html

# Página C - Dashboard (recibe POST desde /login)
@app.route("/dashboard", methods=["POST"])
def pagina_c():
    start_time = time.time()

    # pre-procesamiento simulado (opcional)
    if SIMULATE_DELAY:
        time.sleep(random.uniform(MIN_DELAY_PRE, MAX_DELAY_PRE))

    # procesamiento simulado
    if SIMULATE_DELAY:
        time.sleep(random.uniform(MIN_DELAY_PROC, MAX_DELAY_PROC))

    processing_time = round(time.time() - start_time, 3)
    usuario = request.form.get("usuario", "anonimo")
    session_id = random.randint(1000, 9999)
    server_id = get_server_id()

    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Dashboard - Sistema de Notas</title>
    <meta charset="utf-8">
    <style>
        body {{ font-family:Arial, sans-serif; margin:40px; background:#f5f5f5; }}
        .container {{ max-width:900px; margin:0 auto; background:#fff; padding:30px; border-radius:10px; box-shadow:0 2px 10px rgba(0,0,0,0.1); }}
        .server-info {{ background:#e9ecef; padding:15px; border-radius:5px; margin:20px 0; border-left:4px solid #6f42c1; }}
        .metric-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:15px; }}
        .metric-card {{ background:#fff; padding:15px; border-radius:5px; border:1px solid #dee2e6; text-align:center; }}
        .metric-value {{ font-size:24px; font-weight:bold; color:#495057; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Panel de Control</h1>
        <div class="server-info">
            <strong>Servidor:</strong> {server_id} |
            <strong>Usuario:</strong> {usuario} |
            <strong>Sesion ID:</strong> {session_id}
        </div>

        <div class="metric-grid">
            <div class="metric-card"><div class="metric-value">{processing_time}s</div><div>Tiempo de Respuesta</div></div>
            <div class="metric-card"><div class="metric-value">{server_id}</div><div>Servidor Actual</div></div>
            <div class="metric-card"><div class="metric-value">{session_id}</div><div>ID de Sesión</div></div>
            <div class="metric-card"><div class="metric-value">Activo</div><div>Estado</div></div>
        </div>

        <div style="margin-top:20px;">
            <a href="/login"><button style="padding:10px 18px;">Cerrar Sesión</button></a>
            <a href="/"><button style="padding:10px 18px;">Página Principal</button></a>
        </div>

        <div style="margin-top:25px; font-size:12px; color:#6c757d;">
            Nota técnica: recargue la página para ver cómo se distribuyen las solicitudes entre servidores.
        </div>
    </div>
</body>
</html>"""
    return html

# Health check para GCP
@app.route("/health")
def health_check():
    return jsonify(status="healthy", server_id=get_server_id(), timestamp=time.time()), 200

# Whoami simple (útil para conteos desde curl)
@app.route("/whoami")
def whoami():
    return f"{get_server_id()}\n", 200, {"Content-Type": "text/plain; charset=utf-8"}

# Info adicional
@app.route("/info")
def info():
    return jsonify(server_id=get_server_id(), service="balanceador-proyecto", version="1.0", status="running"), 200

if __name__ == "__main__":
    # en producción usar gunicorn; esto permite pruebas locales
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
