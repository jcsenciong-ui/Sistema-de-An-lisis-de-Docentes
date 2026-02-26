# 📊 Sistema de Análisis de Docentes - Documentación Completa

## 🎯 Descripción General

Este es un proyecto integrado que combina **Python**, **HTML/CSS** y **JavaScript** para analizar y visualizar datos de docentes por nivel educativo (Inicial, Primario, Secundario) en diferentes regionales, distritos y centros educativos.

La aplicación procesa un archivo Excel con información educativa y genera una interfaz web interactiva con filtros, estadísticas y gráficos en tiempo real.

---

## 📁 Estructura del Proyecto

```
c:\xampp\htdocs\DatosDoc\
├── docente XLSX.xlsx          # Archivo Excel original con datos
├── procesar_datos.py          # Script Python que procesa los datos
├── datos.json                 # Archivo JSON generado con datos procesados
├── index.html                 # Página web principal
├── servidor.py                # Servidor Python para servir la aplicación
├── analizar_datos.py          # Script de análisis (opcional)
└── README.md                  # Este archivo
```

---

## ⚙️ Requisitos Previos

- **Python 3.14+** (incluido en el proyecto)
- **Entorno Virtual** (ya configurado en `.venv/`)
- **Dependencias Python**: 
  - `pandas`
  - `openpyxl`

Todas las dependencias están ya instaladas en el entorno virtual.

---

## 🚀 Cómo Usar la Aplicación

### Opción 1: Usando XAMPP (Recomendado)

1. **Accede a la carpeta del proyecto**:
   ```bash
   cd c:\xampp\htdocs\DatosDoc
   ```

2. **Abre en tu navegador**:
   ```
   http://localhost/DatosDoc/index.html
   ```

> **Nota**: Si XAMPP está ejecutándose, la aplicación estará disponible automáticamente.

### Opción 2: Usar el Servidor Python Incluido

1. **Abre PowerShell/CMD en la carpeta del proyecto**:
   ```bash
   cd c:\xampp\htdocs\DatosDoc
   ```

2. **Inicia el servidor**:
   ```bash
   .venv\Scripts\python.exe servidor.py
   ```

3. **Accede en tu navegador**:
   ```
   http://localhost:8000/index.html
   ```

4. **Para detener el servidor**: Presiona `Ctrl+C`

---

## 🔄 Actualizar Datos (Si cambias el Excel)

Si modificas el archivo `docente XLSX.xlsx`, debes regenerar el archivo JSON:

1. **Abre PowerShell en la carpeta del proyecto**:
   ```bash
   cd c:\xampp\htdocs\DatosDoc
   ```

2. **Ejecuta el procesador de datos**:
   ```bash
   .venv\Scripts\python.exe procesar_datos.py
   ```

3. **Recarga la página web** en tu navegador (Ctrl+F5)

El script procesará automáticamente los datos y generará un nuevo archivo `datos.json`.

---

## 🎨 Características de la Aplicación Web

### 1. **Filtros Interactivos**
   - Filtrar por **Regional Educativa**
   - Filtrar por **Distrito Educativo**
   - Los distritos se actualizan dinámicamente según la regional seleccionada
   - Botones para aplicar o limpiar filtros

### 2. **Estadísticas en Tiempo Real**
   - **Total de Docentes**: Suma de todos los niveles
   - **Docentes por Nivel**:
     - 👶 Nivel Inicial
     - 📚 Nivel Primario
     - 🎓 Nivel Secundario
   - **Total de Centros Educativos**
   - **Total de Distritos**

### 3. **Visualizaciones (Gráficos)**
   - **Gráfico de Pastel**: Distribución de docentes por nivel
   - **Gráfico de Barras**: Top 10 regionales con más docentes

### 4. **Tabla de Centros Educativos**
   - Vista completa de todos los centros y sus docentes
   - Búsqueda en tiempo real por código, nombre o regional
   - Colores codificados por nivel:
     - 🟢 Verde: Docentes Inicial
     - 🟠 Naranja: Docentes Primario
     - 🔴 Rojo: Docentes Secundario

---

## 📊 Datos Disponibles

El archivo Excel contiene información de:

| Campo | Descripción |
|-------|-------------|
| **Regional** | Dirección Regional (19 total) |
| **Distrito** | Distrito Educativo (122 total) |
| **Centro** | Nombre del Centro Educativo |
| **Código SIGERD** | Código único del centro |
| **Docentes Inicial** | Cantidad de docentes en Nivel Inicial |
| **Docentes Primario** | Cantidad de docentes en Nivel Primario |
| **Docentes Secundario** | Cantidad de docentes en Nivel Secundario |

### Totales Agregados:
- **19** Regionales Educativas
- **122** Distritos Educativos
- **7,814** Centros Educativos
- **174,247** Docentes totales en todo el país

---

## 🔍 Cómo Usar los Filtros

### Ejemplo 1: Ver todos los distritos de una regional

1. Selecciona la regional en el dropdown "Regional Educativa"
2. El dropdown "Distrito" se actualiza automáticamente
3. Haz clic en "Aplicar Filtros"
4. Verás solo los datos de esa regional

### Ejemplo 2: Ver centros específicos de un distrito

1. Selecciona la regional
2. Selecciona el distrito
3. Haz clic en "Aplicar Filtros"
4. La tabla mostrará solo los centros de ese distrito

### Ejemplo 3: Buscar en la tabla

1. Usa el campo de búsqueda debajo de la tabla
2. Escribe un código, nombre de centro o regional
3. La tabla se filtra en tiempo real

---

## 🛠️ Estructura de Datos (JSON)

El archivo `datos.json` tiene esta estructura:

```json
{
  "regionales": [
    {
      "nombre": "01 - BARAHONA",
      "codigo": "01",
      "distritos": [
        {
          "nombre": "0101 - PEDERNALES",
          "codigo": "0101",
          "total_docentes_inicial": 100,
          "total_docentes_primario": 500,
          "total_docentes_secundario": 300,
          "centros": [
            {
              "codigo": "2334",
              "nombre": "CENTRO XYZ",
              "docentes_inicial": 3,
              "docentes_primario": 22,
              "docentes_secundario": 5
            }
          ]
        }
      ]
    }
  ],
  "estadisticas": {
    "total_docentes": 174247,
    "total_docentes_inicial": 19013,
    "total_docentes_primario": 90791,
    "total_docentes_secundario": 64443,
    "total_centros": 7814,
    "total_distritos": 122,
    "total_regionales": 19
  }
}
```

---

## 🐛 Solución de Problemas

### Problema: "No se carga el archivo datos.json"

**Solución**:
1. Verifica que el archivo existe en la carpeta
2. Executa nuevamente: `.venv\Scripts\python.exe procesar_datos.py`
3. Recarga la página web (Ctrl+F5)

### Problema: Los datos no se actualizan después de cambiar el Excel

**Solución**:
1. Asegúrate de haber ejecutado: `.venv\Scripts\python.exe procesar_datos.py`
2. Cierra completamente el navegador y vuelve a abrir
3. Borra la caché del navegador (Ctrl+Shift+Delete)

### Problema: El puerto 8000 está en uso

**Solución**: 
1. Edita `servidor.py`
2. Cambia `PORT = 8000` a otro puerto (ej: `PORT = 8001`)
3. Inicia el servidor nuevamente

---

## 📱 Responsive Design

La aplicación funciona correctamente en:
- 🖥️ Computadoras de escritorio (1920x1080 y superiores)
- 📱 Tablets (768px y superiores)
- 📱 Celulares (ajustado automáticamente)

---

## 🎓 Información Técnica

### Stack Tecnológico:
- **Backend**: Python (pandas, openpyxl)
- **Frontend**: HTML5, CSS3, JavaScript Vanilla
- **Gráficos**: Chart.js
- **Servidor**: Python http.server

### Navegadores Soportados:
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+

---

## 📝 Notas Importantes

✅ Los datos se procesan **una sola vez** al iniciar
✅ Las operaciones de filtrado se hacen **en el navegador** (muy rápido)
✅ No requiere conexión a internet para funcionar
✅ Los datos se cargan desde `datos.json` de forma local
✅ Es seguro modificar el Excel - basta procesar nuevamente

---

## 👤 Soporte

Si encuentras algún problema o tienes dudas:

1. Verifica que Python 3.14+ esté instalado
2. Asegúrate de que el entorno virtual está activado
3. Ejecuta nuevamente el procesador de datos
4. Recarga la página web en el navegador

---

## 📄 Licencia

Este proyecto es de uso educativo e interno.

---

**Última actualización**: 25 de febrero de 2026  
**Versión**: 1.0.0
