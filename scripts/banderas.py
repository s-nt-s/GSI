import requests
import xlrd
import re

URL="https://www.hacienda.gob.es/Documentacion/Publico/GobiernoAbierto/Transparencia/Planes-y-programas/BANDERAS-ROJAS.xlsx"

r = requests.get(URL)

book = xlrd.open_workbook(file_contents=r.content)
sheet = book.sheet_by_index(0)

def get_row(rx, start_colx=0, end_colx=end_colx):
    vals = sheet.row_values(rx, start_colx=start_colx, end_colx=end_colx)
    for i, v in enumerate(vals):
        if isinstance(v, str):
            v = v.strip()
            if len(v) == 0:
                v = None
            vals[i] = v
    return tuple(vals)

for rx in range(sheet.nrows):
    vals = get_row(rx, start_colx=1)
    if len(vals)<1 or vals[0] is None:
        continue
    cod = vals[0]
    if re.match(r"^[A-Z]+$", cod):
        print("\n### {}\n".format(vals[1]))
    if re.match(r"^[A-Z]+\.R\d+$", cod):
        print("* {} {}".format(cod, vals[1]))
        continue
    if re.match(r"^\d+\.\d+$", cod):
        print("    * {} {}".format(cod, vals[2]))
        continue
