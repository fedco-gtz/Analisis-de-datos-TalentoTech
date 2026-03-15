from datetime import datetime
import calendar

# -------------------------------
# Configuración de eventos
# Formato: "YYYY-MM-DD": "Descripción"
eventos = {
    "2026-03-15": "Reunión con el equipo",
    "2026-03-19": "Presentación del proyecto",
    # Agregá más eventos acá
}
# -------------------------------

# Fecha de hoy
hoy = datetime.now()
anio = hoy.year
mes = hoy.month
dia = hoy.day

# Generar calendario
cal = calendar.monthcalendar(anio, mes)
dias_semana = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]

# Construir tabla Markdown
tabla = "| " + " | ".join(dias_semana) + " |\n"
tabla += "|"+ "-----|"*7 + "\n"

for semana in cal:
    fila = []
    for d in semana:
        if d == 0:
            fila.append(" ")
        elif d == dia:
            fila.append(f"**{d} ✅**")
        elif f"{anio}-{mes:02d}-{d:02d}" in eventos:
            fila.append(f"{d} 🎉")
        else:
            fila.append(str(d))
    tabla += "| " + " | ".join(fila) + " |\n"

# Lista de eventos
lista_eventos = "### 📌 Eventos\n"
for fecha, desc in eventos.items():
    lista_eventos += f"- {fecha}: {desc}\n"

# Contenido final del README
contenido = f"""# 📅 Calendario {hoy.strftime('%B %Y')}

{tabla}

{lista_eventos}
"""

# Guardar README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(contenido)

print("README.md actualizado ✅")