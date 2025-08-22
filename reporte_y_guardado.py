import json

from datetime import datetime
from estadisticas_ciclos import estadisticas
from ingesta_y_validacion import cargar_compras

def generar_reporte(resumen, ruta_salida):
    
    resportes = {
        "fecha_reporte": datetime.now().strftime("%y - %m - %d %H: %M: %S"),
        "total_ingresos":resumen["total_ingresos"],
        "top_producto_ingresos": resumen["top_producto_ingresos"],
        "compras_cliente": resumen["compras_cliente"],
        "si_aplica_bono":resumen["bono"]
    }
    
    if resumen["bono"]:
        resportes["mensaje_bono"] = "Umbral superado, aplicar descuento corporativo 5% en próxima compra"
    
    try:
        with open(ruta_salida, "w", encoding="utf-8") as f:
            json.dump(resportes, f, indent=2, ensure_ascii=False)
        print(f"Reporte guardado en: {ruta_salida}")
    except:
        print("Error al guardar el reporte")
        
def main():
    
    print("ANALISIS DE COMPRAS")
    print("=" * 40)
    
    print("Cargar datos... ")
    compras = cargar_compras("compras.csv")
    
    if len(compras) == 0:
        print("No se cargaron los datos")
        return
    
    print("Calculando estadisticas... ")
    resumen_estadisticas = estadisticas(compras)
    
    print("Generando resporte... ")
    generar_reporte(resumen_estadisticas, "reportes.json")
    
    print("\n" + "=" * 40)
    print("RESUMEN DE ESTADÍSTICAS")
    print("=" * 40)
    
    print(f"Total de ingresos: ${resumen_estadisticas["total_ingresos"]:,.0f}")
    print(f"Producto top: {resumen_estadisticas["top_producto_ingresos"]}")
    
    print("\nCompras por cliente:")
    for cliente, cantidad in resumen_estadisticas["compras_cliente"].items():
        print(f"  {cliente}: {cantidad} items")

    if resumen_estadisticas["bono"] == True:
        print("\nBONO: SÍ - Umbral superado")
    else:
        print("\nBONO: NO - Umbral no alcanzado")
    
    print("\nProceso completado!")

if __name__ == "__main__":
    main()