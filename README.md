# Flask LB Demo

App sencilla que simula un sistema de gestión de notas y permite evidenciar balanceo entre servidores LOCAL y CLOUD.

Rutas:
- `/` → bienvenida
- `/login` → formulario
- `/dashboard` → dashboard (POST)
- `/health` → healthcheck (JSON)
- `/whoami` → texto plano con el identificador del servidor

Variables de entorno útiles:
- `SERVER_ID` (LOCAL o CLOUD)
- `SIMULATE_DELAY` (1 para activar sleeps, 0 para desactivar)
- `MIN_DELAY_PRE`, `MAX_DELAY_PRE`, `MIN_DELAY_PROC`, `MAX_DELAY_PROC` (floats)

