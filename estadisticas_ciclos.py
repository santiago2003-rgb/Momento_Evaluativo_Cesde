from ingesta_y_validacion import cargar_compras

def estadisticas(data):
    total_ingresos = 0
    ingreso_producto = {}
    compras_cliente = {}
    
    for compra in data:
        cliente = compra["cliente"]
        producto = compra["producto"]
        cantidad = compra["cantidad"]
        precio_unitario = compra["precio_unitario"]
        
        ingreso = cantidad * precio_unitario
        total_ingresos += ingreso
        
        if producto in ingreso_producto:
            ingreso_producto[producto] += ingreso
            
        else:
            ingreso_producto[producto] = ingreso
            
        if cliente not in compras_cliente:
            compras_cliente[cliente] = cantidad
            
        else:
            compras_cliente[cliente] += cantidad
            
    top_producto = None
    max_ingreso = 0
    
    for producto in ingreso_producto:
        if ingreso_producto[producto] > max_ingreso:
            max_ingreso = ingreso_producto[producto]
            top_producto = producto
            
    if total_ingresos > 6000000:
        bono = True
    
    else:
        bono = False
        
    resultado = {
        "total_ingresos": total_ingresos,
        "top_producto_ingresos": top_producto,
        "compras_cliente": compras_cliente,
        "bono": bono
    }
    
    return resultado

compras = cargar_compras("compras.csv")
resultado = estadisticas(compras)

print("\nEstadisticas: ")
for clave, valor in resultado.items():
    print(f"{clave}: {valor}")
    