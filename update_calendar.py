import calendar
from datetime import datetime, date
import re
import os

# 1. Fechas de entregas
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
    
    txt = f"### 📅 {meses[hoy.month-1]} {hoy.year}\n\n"
    txt += "| Lun | Mar | Mié | Jue | Vie | Sáb | Dom |\n|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n"
    
    entregas_mes = {f.day: n for f, n in FECHAS_ENTREGA if f.month == hoy.month}

    for week in cal:
        row = "|"
        for day in week:
            if day == 0: row += "   |"
            else:
                celda = f"**{day}**" if day == hoy.day else str(day)
                if day in entregas_mes: celda += "🚀"
                row += f" {celda} |"
        txt += row + "\n"
    
    return txt

def actualizar_readme(nuevo_contenido):
    file_path = "README.md"
    
    # Intentamos leer el archivo con la codificación que causaba error
    try:
        with open(file_path, "rb") as f:
            content_bytes = f.read()
            # Detectamos si tiene el molesto BOM de Windows y lo decodificamos bien
            content = content_bytes.decode("utf-16" if content_bytes.startswith((b'\xff\xfe', b'\xfe\xff')) else "utf-8-sig")
    except Exception:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

    # Definimos las marcas exactas
    start_tag = ""
    end_tag = ""
    
    # Esta es la parte de "cirujano": Reemplaza SOLO lo que hay entre medio
    pattern = re.compile(f"{re.escape(start_tag)}.*?{re.escape(end_tag)}", re.DOTALL)
    replacement = f"{start_tag}\n\n{nuevo_contenido}\n{end_tag}"
    
    if pattern.search(content):
        updated_content = pattern.sub(replacement, content)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print("✅ Calendario inyectado con éxito.")
    else:
        print("❌ No encontré las marcas en tu README.")

if __name__ == "__main__":
    actualizar_readme(generar_calendario())