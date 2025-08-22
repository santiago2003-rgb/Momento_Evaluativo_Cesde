def cargar_compras(ruta):
    compras_validas = []

    with open(ruta, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        

    for i, linea in enumerate(lineas[1:], start=2): # Saltar encabezado
        if not linea.strip():
            continue

        partes = linea.strip().split(",")

        cliente, fecha, producto, cantidad_str, precio_str = partes
        
        # Maneja las exepciones verificando si no son numeros
        try:
            cantidad = int(cantidad_str)
            precio_unitario = float(precio_str)
        except:
            print(f"⚠️ Línea {i}: cantidad o precio no son números.")
            continue
        
        if cantidad <= 0 or precio_unitario <= 0:
            print(f"⚠️ Línea {i}: cantidad o precio <= 0.")
            continue

        if len(fecha) != 10 or fecha[4] != "-" or fecha[7] != "-":
            print(f"⚠️ Línea {i}: fecha con formato incorrecto.")
            continue

        compra = {
            "cliente": cliente,
            "fecha": fecha,
            "producto": producto,
            "cantidad": cantidad,
            "precio_unitario": precio_unitario
        }

        compras_validas.append(compra)

    return compras_validas

compras = cargar_compras("compras.csv")

print("\n✅ Compras válidas:")
for compra in compras:
    print(compra)

