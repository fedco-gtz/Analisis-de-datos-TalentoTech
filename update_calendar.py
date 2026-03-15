import calendar
from datetime import datetime, date
import re
import os

# 1. Configuración de Fechas de Coderhouse
FECHAS_ENTREGA = [
    (date(2026, 4, 15), "Pre-Entrega #1 🚀"),
    (date(2026, 5, 10), "Pre-Entrega #2 🚀"),
    (date(2026, 6, 5), "Pre-Entrega #3 🚀"),
    (date(2026, 6, 30), "Entrega Final 🏆")
]

ahora = datetime.now()
hoy = ahora.date()

def generar_calendario():
    cal = calendar.monthcalendar(hoy.year, hoy.month)
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    mes_nombre = meses[hoy.month-1]
    
    # Construcción de la tabla
    txt = f"### 📅 {mes_nombre} {hoy.year}\n\n"
    txt += "| Lun | Mar | Mié | Jue | Vie | Sáb | Dom |\n"
    txt += "|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n"
    
    entregas_mes = {f.day: n for f, n in FECHAS_ENTREGA if f.month == hoy.month and f.year == hoy.year}

    for week in cal:
        row = "|"
        for day in week:
            if day == 0:
                row += "   |"
            else:
                # Si es hoy, negrita. Si hay entrega, cohete.
                celda = f"**{day}**" if day == hoy.day else str(day)
                if day in entregas_mes:
                    celda += "🚀"
                row += f" {celda} |"
        txt += row + "\n"
    
    # Cálculo de próxima entrega
    proxima = "✅ ¡Entregas finalizadas!"
    for fecha, nombre in FECHAS_ENTREGA:
        if fecha >= hoy:
            diff = (fecha - hoy).days
            proxima = f"Próximo hito: **{nombre}** (en {diff} días)"
            break
            
    txt += f"\n> {proxima}\n"
    return txt

def actualizar_readme(contenido_nuevo):
    # Intentamos abrir el archivo en la raíz
    file_name = "README.md"
    if not os.path.exists(file_name):
        print(f"Error: No se encontró {file_name}")
        return

    with open(file_name, "r", encoding="utf-8") as f:
        readme_content = f.read()

    # Reemplazo por etiquetas
    start_tag = ""
    end_tag = ""
    pattern = f"{re.escape(start_tag)}.*?{re.escape(end_tag)}"
    replacement = f"{start_tag}\n{contenido_nuevo}\n{end_tag}"
    
    if re.search(pattern, readme_content, flags=re.DOTALL):
        new_readme = re.sub(pattern, replacement, readme_content, flags=re.DOTALL)
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(new_readme)
        print("✅ Calendario actualizado correctamente.")
    else:
        print("❌ No se encontraron las etiquetas ")

if __name__ == "__main__":
    actualizar_readme(generar_calendario())