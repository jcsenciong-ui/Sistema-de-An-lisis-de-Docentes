#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INICIO RÁPIDO - Ejecuta esto para iniciar la aplicación
"""

import subprocess
import sys
import time
import webbrowser
from pathlib import Path

print("""
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║     📊 SISTEMA DE ANÁLISIS DE DOCENTES - INICIO RÁPIDO 📊          ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""")

# Pasos de startup
print("⏳ Iniciando aplicación...\n")

print("1️⃣  Verificando validación...")
resultado = subprocess.run([sys.executable, 'validar.py'], capture_output=True, text=True)
print(resultado.stdout)

if "VALIDACIÓN EXITOSA" in resultado.stdout:
    print("✅ Validación completada correctamente\n")
    
    print("2️⃣  Iniciando servidor web...")
    print("   🌐 Servidor iniciado en: http://localhost:8000")
    print("   📂 Abriendo navegador automáticamente...\n")
    
    # Pequeño delay para asegurar que el servidor está listo
    print("3️⃣  Abriendo navegador en 2 segundos...\n")
    
    try:
        # Iniciar servidor en background
        servidor_proceso = subprocess.Popen(
            [sys.executable, 'servidor.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Esperar a que el servidor se inicie
        time.sleep(2)
        
        # Abrir navegador
        url = "http://localhost:8000/index.html"
        webbrowser.open(url)
        
        print(f"✅ Navegador abierto con: {url}\n")
        print("╔════════════════════════════════════════════════════════════════════╗")
        print("║                                                                    ║")
        print("║  🎉 ¡APLICACIÓN LISTA PARA USAR!                                 ║")
        print("║                                                                    ║")
        print("║  📋 Funcionalidades:                                              ║")
        print("║     • Filtros por Regional y Distrito                             ║")
        print("║     • Estadísticas en tiempo real                                 ║")
        print("║     • Gráficos interactivos (Pastel y Barras)                     ║")
        print("║     • Tabla filtrable de Centros Educativos                       ║")
        print("║     • Búsqueda integrada                                          ║")
        print("║                                                                    ║")
        print("║  📊 Datos disponibles:                                            ║")
        print("║     • 19 Regionales                                               ║")
        print("║     • 122 Distritos                                               ║")
        print("║     • 7,814 Centros Educativos                                    ║")
        print("║     • 174,247 Docentes totales                                    ║")
        print("║                                                                    ║")
        print("║  ℹ️  Para detener el servidor: Presiona Ctrl+C                    ║")
        print("║                                                                    ║")
        print("╚════════════════════════════════════════════════════════════════════╝\n")
        
        # Mantener el servidor ejecutándose
        servidor_proceso.wait()
    
    except KeyboardInterrupt:
        print("\n\n⛔ Servidor detenido por el usuario")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nIntenta ejecutar manualmente:")
        print("  .venv\\Scripts\\python.exe servidor.py")
else:
    print("❌ Validación falló. Revisa los errores arriba.")
    sys.exit(1)
