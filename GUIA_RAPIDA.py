#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GUÍA RÁPIDA DE USO - Lee esto primero
"""

GUIA_RAPIDA = """
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║           📊 GUÍA RÁPIDA - SISTEMA DE ANÁLISIS DE DOCENTES 📊             ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝

╭────────────────────────────────────────────────────────────────────────────╮
│ 🚀 INICIO INMEDIATO (EN 3 PASOS)                                          │
╰────────────────────────────────────────────────────────────────────────────╯

PASO 1: Abre PowerShell/CMD
    • Win + R
    • Escribe: cmd
    • Presiona Enter

PASO 2: Navega a la carpeta del proyecto
    cd c:\\xampp\\htdocs\\DatosDoc

PASO 3: Ejecuta (OPCIÓN A - RECOMENDADA):
    
    ✅ AUTOMÁTICA (abre navegador automáticamente):
       .venv\\Scripts\\python.exe inicio.py
    
    📱 CON XAMPP:
       Abre en navegador: http://localhost/DatosDoc/index.html
    
    ⚙️ MANUAL:
       .venv\\Scripts\\python.exe servidor.py
       Abre en navegador: http://localhost:8000/index.html

╭────────────────────────────────────────────────────────────────────────────╮
│ 🎯 FUNCIONES PRINCIPALES EXPLICADAS                                       │
╰────────────────────────────────────────────────────────────────────────────╯

┌─ SECCIÓN DE FILTROS ────────────────────────────────────────────────────┐
│                                                                         │
│  • Selecciona una REGIONAL en el primer dropdown                       │
│    → El segundo dropdown se actualiza automáticamente                  │
│                                                                         │
│  • Selecciona un DISTRITO en el segundo dropdown                       │
│                                                                         │
│  • Haz clic en "APLICAR FILTROS"                                       │
│    → La página se actualiza con datos filtrados                        │
│                                                                         │
│  • Haz clic en "LIMPIAR FILTROS"                                       │
│    → Vuelve a ver todos los datos                                      │
│                                                                         │
│  EJEMPLO:                                                               │
│  Regional: "01 - BARAHONA"                                             │
│  Distrito: "0101 - PEDERNALES"                                         │
│  [Aplicar Filtros]                                                     │
│  → Ve todos los centros de ese distrito                                │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─ ESTADÍSTICAS (LAS 6 TARJETAS COLORIDAS) ──────────────────────────────┐
│                                                                         │
│  Mostradas en TIEMPO REAL según tus filtros:                           │
│                                                                         │
│  👨‍🏫 TOTAL DE DOCENTES       → Suma de todos los niveles              │
│  👶 NIVEL INICIAL           → 19,013 docentes (nacional)              │
│  📚 NIVEL PRIMARIO          → 90,791 docentes (nacional)              │
│  🎓 NIVEL SECUNDARIO        → 64,443 docentes (nacional)              │
│  🏫 TOTAL DE CENTROS        → 7,814 centros (nacional)                │
│  📍 TOTAL DE DISTRITOS      → 122 distritos (nacional)                │
│                                                                         │
│  💡 Si aplicas filtros, estos números cambian                          │
│     para mostrar solo datos del filtro seleccionado                    │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─ GRÁFICOS INTERACTIVOS ────────────────────────────────────────────────┐
│                                                                         │
│  GRÁFICO 1: Distribución de Docentes por Nivel (PASTEL)               │
│             └─ Muestra el % de cada nivel                             │
│                                                                         │
│  GRÁFICO 2: Top 10 Regionales (BARRAS)                                │
│             └─ Las 10 regionales con más docentes                     │
│                                                                         │
│  💡 Ambos se actualizan según los filtros que apliques                │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─ TABLA DE CENTROS EDUCATIVOS ──────────────────────────────────────────┐
│                                                                         │
│  Columnas:                                                              │
│  • Código: Código SIGERD del centro (ej: 2334)                        │
│  • Centro: Nombre del centro educativo                                │
│  • Regional: A qué regional pertenece                                 │
│  • Distrito: A qué distrito pertenece                                 │
│  • Docentes Inicial: Cantidad (color VERDE)                           │
│  • Docentes Primario: Cantidad (color NARANJA)                        │
│  • Docentes Secundario: Cantidad (color ROJO)                         │
│                                                                         │
│  BUSCAR: Escribe en el campo de búsqueda                              │
│          • Código del centro (ej: 2334)                               │
│          • Nombre del centro (ej: HERNANDO)                           │
│          • Regional (ej: BARAHONA)                                    │
│          → Filtra la tabla en tiempo real                             │
│                                                                         │
│  💡 La tabla respeta los filtros de Regional/Distrito                 │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

╭────────────────────────────────────────────────────────────────────────────╮
│ 📋 EJEMPLOS DE USO PRÁCTICO                                               │
╰────────────────────────────────────────────────────────────────────────────╯

EJEMPLO 1: ¿Cuántos docentes hay en Regional Barahona?
─────────────────────────────────────────────────────
  1. Regional: "01 - BARAHONA"
  2. Distrito: (dejar en blanco)
  3. [Aplicar Filtros]
  4. Mira las tarjetas de estadísticas
     → Total Docentes Inicial: X
     → Total Docentes Primario: X
     → Total Docentes Secundario: X

EJEMPLO 2: ¿Qué centros hay en el distrito Pedernales?
─────────────────────────────────────────────────────
  1. Regional: "01 - BARAHONA"
  2. Distrito: "0101 - PEDERNALES"
  3. [Aplicar Filtros]
  4. Desplázate hacia abajo a la tabla
  5. Verás solo los centros de ese distrito
  6. Puedes ver docentes por nivel en cada centro

EJEMPLO 3: ¿Qué centros tienen mucho docentes en primaria?
──────────────────────────────────────────────────────────
  1. Limpiar todos los filtros
  2. Ir a la tabla
  3. Buscar por nombre o código si lo sabes
  4. O simplemente revisar la columna "Docentes Primario"
     y buscar los números más altos

EJEMPLO 4: Comparar docentes entre niveles
──────────────────────────────────────────
  1. Limpiar filtros
  2. Mirar el gráfico de pastel
  3. Verá que Primaria tiene muchos más docentes
     que Inicial y Secundaria

EJEMPLO 5: Ver los 10 distritos con más docentes
─────────────────────────────────────────────
  1. Limpiar filtros
  2. Mirar el gráfico de barras (Top 10 Regionales)
  3. Puedes ver cuáles tienen más concentración

╭────────────────────────────────────────────────────────────────────────────╮
│ 🔧 SOLUCIÓN RÁPIDA DE PROBLEMAS                                          │
╰────────────────────────────────────────────────────────────────────────────╯

❌ "No veo datos en la página"
   ✅ Solución:
      • Recarga la página (Ctrl+F5)
      • Si persiste: ejecuta .venv\\Scripts\\python.exe procesar_datos.py

❌ "El filtro de Distrito está vacío"
   ✅ Solución:
      • Asegúrate de seleccionar primero una Regional
      • Los distritos se cargan automáticamente

❌ "La tabla está vacía después de filtrar"
   ✅ Solución:
      • Quizás no hay centros en esa combinación
      • Prueba [Limpiar Filtros]
      • Intenta otra Regional/Distrito

❌ "El navegador no se abre automáticamente"
   ✅ Solución:
      • Copia y pega en el navegador: http://localhost:8000
      • O abre: http://localhost/DatosDoc (si XAMPP está corriendo)

❌ "Puerto 8000 en uso"
   ✅ Solución:
      • Abre servidor.py con editor de texto
      • Cambia: PORT = 8000  →  PORT = 8001
      • Accede a: http://localhost:8001

╭────────────────────────────────────────────────────────────────────────────╮
│ 📊 NÚMEROS CLAVE A RECORDAR                                              │
╰────────────────────────────────────────────────────────────────────────────╯

Total Nacional (sin filtros):
  ├─ Regionales: 19
  ├─ Distritos: 122
  ├─ Centros: 7,814
  └─ Docentes: 
      ├─ Inicial: 19,013 👶
      ├─ Primario: 90,791 📚
      ├─ Secundario: 64,443 🎓
      └─ TOTAL: 174,247 👨‍🏫

╭────────────────────────────────────────────────────────────────────────────╮
│ 📚 ARCHIVOS IMPORTANTES                                                  │
╰────────────────────────────────────────────────────────────────────────────╯

USAR DIARIAMENTE:
  • index.html          ← La página que ves en la web

ACTUALIZAR DATOS (si cambias el Excel):
  • procesar_datos.py   ← Ejecuta cuando cambies el Excel

VALIDAR APLICACIÓN:
  • validar.py          ← Verifica que todo está bien

INICIAR AUTOMÁTICO:
  • inicio.py           ← Abre todo automáticamente

DOCUMENTACIÓN COMPLETA:
  • README.md               ← Guía técnica completa
  • PROYECTO_COMPLETADO.md  ← Resumen técnico

╭────────────────────────────────────────────────────────────────────────────╮
│ 🎓 TIP FINAL                                                              │
╰────────────────────────────────────────────────────────────────────────────╯

💡 La aplicación es TOTALMENTE LOCAL
   • No necesita internet
   • No sube datos a ningún servidor
   • Todo funciona en tu navegador
   • Rápido y seguro

💡 Los datos se actualizan instantáneamente
   • Los filtros funcionan en el navegador
   • No hay esperas
   • Cambios inmediatos en gráficos y tabla

💡 Puedes abrir múltiples ventanas
   • Abre 2 regionales diferentes en 2 navegadores
   • Compara los datos lado a lado

╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║  ¡LISTO PARA EMPEZAR! Ejecuta: .venv\\Scripts\\python.exe inicio.py     ║
║                                                                            ║
║  Presiona Ctrl+C para detener el servidor cuando termines                 ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

if __name__ == '__main__':
    print(GUIA_RAPIDA)
    input("\n\nPresiona Enter para cerrar esta ventana...")
