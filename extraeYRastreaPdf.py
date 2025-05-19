
import PyPDF2
import re

def extraer_texto_pdf(ruta_pdf):
    texto = ""
    try:
        with open(ruta_pdf, 'rb') as archivo_pdf:
            lector_pdf = PyPDF2.PdfReader(archivo_pdf)
            for numero_pagina in range(len(lector_pdf.pages)):
                pagina = lector_pdf.pages[numero_pagina]
                texto += pagina.extract_text()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta: {ruta_pdf}")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el PDF con PyPDF2: {e}")
        return None
    return texto

def rastrear_conceptos(texto):
    conceptos_a_rastrear = [
        "COMPRA TARJETA", "COMISION TRANSFERENCIA/GIRO", "COMISION DATANET", "TRANSFERENCIA",
        "PAGO", "BIP DB", "REV. IMP.DEBITO.-LEY 25413", "DEBITO AUTOMATICO", "IMPUESTO CREDITO -LEY 25413",
        "SALDO ANTERIOR", "IMPUESTO DEBITO -LEY 25413", "P.SERV", "SMG", "OBRA SOCIAL", "COMISION MENSUAL",
        "EXTRACCION", "CR.DEBIN", "CR.TRAN", "CRED.TRF", "AFIP"
    ]
    movimientos_rastreados = {}
    if texto:
        lineas = texto.split('\n')
        for linea in lineas:
            linea_limpia = linea.strip()
            if re.match(r'^\d{2}/\d{2}/\d{4}', linea_limpia) or "SALDO ANTERIOR" in linea_limpia or "IMPUESTO" in linea_limpia:
                for concepto in conceptos_a_rastrear:
                    if concepto.upper() in linea_limpia.upper():
                        if concepto not in movimientos_rastreados:
                            movimientos_rastreados[concepto] = []
                        movimientos_rastreados[concepto].append(linea_limpia)
                        break
    return movimientos_rastreados

def obtener_suma_concepto(concepto, movimientos):
    total = 0
    concepto_upper = concepto.upper()
    if concepto_upper in movimientos:
        for movimiento in movimientos[concepto_upper]:
            match = re.search(r"(-?\d+\.\d{2})", movimiento)
            if match:
                try:
                    monto = float(match.group(1))
                    total += monto
                except ValueError:
                    print(f"Advertencia: No se pudo convertir a número en: {movimiento}")
    return total

def calcular_impuesto_debito_neto(movimientos):
    total_impuesto_debito = obtener_suma_concepto("IMPUESTO DEBITO -LEY 25413", movimientos)
    total_rev_impuesto_debito = obtener_suma_concepto("REV. IMP.DEBITO.-LEY 25413", movimientos)

    impuesto_debito_neto = total_impuesto_debito + total_rev_impuesto_debito
    return f"El impuesto débito neto es: ${impuesto_debito_neto:.2f}"

ruta_del_pdf = "extracto.pdf"
texto_extraido = extraer_texto_pdf(ruta_del_pdf)
movimientos_rastreados = rastrear_conceptos(texto_extraido)

while True:
    consulta = input("Ingrese el concepto del cual desea sumar los montos (o 'impuesto debito neto' o 'salir'): ")
    if consulta.lower() == 'salir':
        break
    elif consulta.lower() == 'impuesto debito neto':
        resultado = calcular_impuesto_debito_neto(movimientos_rastreados)
        print(resultado)
    else:
        total = obtener_suma_concepto(consulta, movimientos_rastreados)
        print(f"La suma de los montos para el concepto '{consulta}' es: ${total:.2f}")