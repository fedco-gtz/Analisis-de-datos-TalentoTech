import calendar
from datetime import datetime, date
import re

# 1. Configuración de Fechas de Coderhouse (Día, Mes, Año)
# Usamos una lista de tuplas para poder iterar y encontrar la más cercana
FECHAS_ENTREGA = [
    (date(2026, 4, 15), "Pre-Entrega #1 🚀"),
    (date(2026, 5, 10), "Pre-Entrega #2 🚀"),
    (date(2026, 6, 5), "Pre-Entrega #3 🚀"),
    (date(2026, 6, 30), "Entrega Final 🏆")
]

ahora = datetime.now()
hoy_date = ahora.date()
año, mes, dia_hoy = ahora.year, ahora.month, ahora.day
nombre_mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
              "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"][mes-1]

def obtener_proxima_entrega():
    for fecha, nombre in FECHAS_ENTREGA:
        if fecha >= hoy_date:
            dias_restantes = (fecha - hoy_date).days
            if dias_restantes == 0:
                return f"⚠️ **¡Hoy es el día de: {nombre}!**"
            return f"Próximo hito: **{nombre}** (en {dias_restantes} días)"
    return "✅ ¡Todas las entregas completadas!"

def generar_calendario():
    cal = calendar.monthcalendar(año, mes)
    header = f"### 📅 {nombre_mes} {año}\n\n"
    table = "| Lun | Mar | Mié | Jue | Vie | Sáb | Dom |\n"
    table += "|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n"
    
    # Diccionario para búsqueda rápida en el renderizado del calendario
    entregas_del_mes = {f.day: n for f, n in FECHAS_ENTREGA if f.month == mes and f.year == año}
    
    for week in cal:
        row = "|"
        for day in week:
            if day == 0:
                row += "   |"
            else:
                contenido = str(day)
                if day == dia_hoy:
                    contenido = f"**{day}**"
                
                if day in entregas_del_mes:
                    # Agregamos el cohete si hay entrega ese día
                    contenido += "🚀"
                
                row += f" {contenido} |"
        table += row + "\n"
    
    # Agregamos la leyenda y el contador
    countdown = obtener_proxima_entrega()
    footer = f"\n> 💡 **Leyenda:** `**Día**` = Hoy | `🚀` = Entrega Coderhouse\n\n"
    footer += f"### ⏳ Status\n{countdown}\n"
    
    return header + table + footer

def actualizar_readme(contenido_cal):
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            readme = f.read()

        start_tag = ""
        end_tag = ""
        pattern = f"{re.escape(start_tag)}.*?{re.escape(end_tag)}"
        nuevo_bloque = f"{start_tag}\n{contenido_cal}\n{end_tag}"
        
        if re.search(pattern, readme, flags=re.DOTALL):
            updated_readme = re.sub(pattern, nuevo_bloque, readme, flags=re.DOTALL)
        else:
            updated_readme = readme + "\n\n" + nuevo_bloque

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(updated_readme)
        print("✅ README actualizado con éxito.")
    except FileNotFoundError:
        print("❌ No se encontró el archivo README.md")

if __name__ == "__main__":
    cal_md = generar_calendario()
    actualizar_readme(cal_md)