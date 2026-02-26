#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de validación para verificar que la aplicación está lista
"""

import json
import os
from pathlib import Path
import sys

# Configurar encoding para Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def validar_aplicacion():
    """Validar que todos los archivos necesarios existen y son correctos"""
    
    print("=" * 70)
    print("[VALIDACION DE LA APLICACION]")
    print("=" * 70)
    
    directorio_base = Path(__file__).parent
    errores = []
    advertencias = []
    
    # Verificar archivos necesarios
    archivos_necesarios = {
        'docente XLSX.xlsx': 'Archivo fuente de datos (Excel)',
        'datos.json': 'Archivo JSON procesado',
        'index.html': 'Página web principal',
        'procesar_datos.py': 'Script de procesamiento',
        'servidor.py': 'Servidor Python',
        'README.md': 'Documentación'
    }
    
    print("\n[VERIFICANDO ARCHIVOS NECESARIOS]")
    print("-" * 70)
    
    for archivo, descripcion in archivos_necesarios.items():
        ruta = directorio_base / archivo
        if ruta.exists():
            tamaño = ruta.stat().st_size
            if tamaño > 0:
                print(f"  [OK] {archivo:25} ({tamaño:,} bytes) - {descripcion}")
            else:
                errores.append(f"El archivo {archivo} está vacío")
                print(f"  [WRN] {archivo:25} (VACIO) - {descripcion}")
        else:
            errores.append(f"El archivo {archivo} no existe")
            print(f"  [ERR] {archivo:25} (NO ENCONTRADO) - {descripcion}")
    
    # Validar contenido de JSON
    print("\n[VALIDANDO CONTENIDO DE DATOS.JSON]")
    print("-" * 70)
    
    try:
        ruta_json = directorio_base / 'datos.json'
        with open(ruta_json, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        
        # Verificar estructura
        if 'regionales' in datos and 'estadisticas' in datos:
            print(f"  [OK] Estructura JSON es válida")
            
            stats = datos['estadisticas']
            
            # Mostrar estadísticas
            print(f"\n  [ESTADISTICAS DEL DATASET]")
            print(f"     Regionales: {stats.get('total_regionales', 0)}")
            print(f"     Distritos: {stats.get('total_distritos', 0)}")
            print(f"     Centros: {stats.get('total_centros', 0)}")
            print(f"     Docentes Inicial: {stats.get('total_docentes_inicial', 0):,}")
            print(f"     Docentes Primario: {stats.get('total_docentes_primario', 0):,}")
            print(f"     Docentes Secundario: {stats.get('total_docentes_secundario', 0):,}")
            print(f"     Total Docentes: {stats.get('total_docentes', 0):,}")
            
            # Verificar que al menos hay datos
            if stats.get('total_docentes', 0) == 0:
                advertencias.append("No hay docentes en los datos")
        else:
            errores.append("El JSON no tiene la estructura esperada (falta 'regionales' o 'estadisticas')")
    
    except json.JSONDecodeError as e:
        errores.append(f"Error al parsear JSON: {e}")
    except Exception as e:
        errores.append(f"Error al leer datos.json: {e}")
    
    # Validar HTML
    print("\n[VALIDANDO INDEX.HTML]")
    print("-" * 70)
    
    try:
        ruta_html = directorio_base / 'index.html'
        with open(ruta_html, 'r', encoding='utf-8') as f:
            contenido_html = f.read()
        
        if 'datos.json' in contenido_html:
            print(f"  [OK] HTML contiene referencia a datos.json")
        else:
            advertencias.append("HTML no contiene referencia a datos.json")
        
        if '<canvas id="chartNiveles">' in contenido_html:
            print(f"  [OK] HTML contiene elementos de gráficos")
        else:
            advertencias.append("HTML no contiene elementos de gráficos")
        
        if 'chart.js' in contenido_html.lower():
            print(f"  [OK] HTML tiene cargada librería Chart.js")
        else:
            advertencias.append("HTML no carga Chart.js")
    
    except Exception as e:
        errores.append(f"Error al leer index.html: {e}")
    
    # Resumen
    print("\n" + "=" * 70)
    print("[RESUMEN DE VALIDACION]")
    print("=" * 70)
    
    if errores:
        print(f"\n[ERRORES] Se encontraron {len(errores)} ERROR(ES):")
        for i, error in enumerate(errores, 1):
            print(f"   {i}. {error}")
    
    if advertencias:
        print(f"\n[ADVERTENCIAS] Se encontraron {len(advertencias)} ADVERTENCIA(S):")
        for i, adv in enumerate(advertencias, 1):
            print(f"   {i}. {adv}")
    
    if not errores and not advertencias:
        print("\n[OK] VALIDACION EXITOSA! La aplicación está lista para usar.\n")
        print("[PROXIMOS PASOS]")
        print("   1. Abre tu navegador")
        print("   2. Accede a: http://localhost/DatosDoc/index.html")
        print("      o ejecuta: .venv\\Scripts\\python.exe servidor.py")
        print("      y accede a: http://localhost:8000/index.html")
        return True
    else:
        print("\n[ERROR] La aplicación tiene problemas. Ver detalles arriba.")
        return False

if __name__ == '__main__':
    exito = validar_aplicacion()
    exit(0 if exito else 1)
