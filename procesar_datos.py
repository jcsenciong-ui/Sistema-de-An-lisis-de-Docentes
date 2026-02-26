#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para procesar datos del archivo Excel y generar JSON para la aplicación web
"""

import pandas as pd
import json
from pathlib import Path

class ProcesadorDatos:
    def __init__(self, ruta_excel):
        self.ruta_excel = ruta_excel
        self.df = None
        self.datos_procesados = {
            'regionales': [],
            'distritos': [],
            'centros': [],
            'estadisticas': {}
        }
    
    def cargar_datos(self):
        """Cargar el archivo Excel"""
        print("Cargando archivo Excel...")
        # Leer el archivo saltando las primeras 3 filas de encabezado
        self.df = pd.read_excel(self.ruta_excel, sheet_name=0, header=2)
        
        # Renombrar columnas de manera clara
        self.df.columns = [
            'regional', 'distrito', 'centro', 'codigo_centro',
            'estado', 'mat_inicial', 'sec_inicial', 'doc_inicial',
            'mat_primario', 'sec_primario', 'doc_primario',
            'mat_secundario', 'sec_secundario', 'doc_secundario'
        ]
        
        # Filtrar solo las filas con datos reales
        self.df = self.df[self.df['regional'].notna()].copy()
        self.df = self.df[~self.df['regional'].str.contains('DIRECCION REGIONAL|DISTRITO', na=False)]
        
        # Convertir docentes a números
        for col in ['doc_inicial', 'doc_primario', 'doc_secundario']:
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce').fillna(0).astype(int)
        
        print(f"Datos cargados: {len(self.df)} registros")
        return self.df
    
    def procesar_datos(self):
        """Procesar y estructurar los datos"""
        print("Procesando datos...")
        
        # Obtener regionales únicas
        regionales = self.df['regional'].unique()
        regionales = sorted([r for r in regionales if pd.notna(r)])
        
        for regional in regionales:
            df_regional = self.df[self.df['regional'] == regional]
            
            # Obtener distritos por regional
            distritos = df_regional['distrito'].unique()
            distritos = sorted([d for d in distritos if pd.notna(d)])
            
            datos_regional = {
                'nombre': regional,
                'codigo': regional.split('-')[0].strip() if '-' in regional else regional,
                'distritos': []
            }
            
            for distrito in distritos:
                df_distrito = df_regional[df_regional['distrito'] == distrito]
                
                # Obtener centros educativos por distrito
                centros = df_distrito[['codigo_centro', 'centro', 'doc_inicial', 'doc_primario', 'doc_secundario']].copy()
                centros = centros[centros['codigo_centro'].notna()].drop_duplicates(subset=['codigo_centro'])
                
                datos_distrito = {
                    'nombre': distrito,
                    'codigo': distrito.split('-')[0].strip() if '-' in distrito else distrito,
                    'total_docentes_inicial': int(df_distrito['doc_inicial'].sum()),
                    'total_docentes_primario': int(df_distrito['doc_primario'].sum()),
                    'total_docentes_secundario': int(df_distrito['doc_secundario'].sum()),
                    'centros': []
                }
                
                # Agregar centros educativos
                for _, centro in centros.iterrows():
                    datos_distrito['centros'].append({
                        'codigo': str(int(centro['codigo_centro'])) if pd.notna(centro['codigo_centro']) else '',
                        'nombre': centro['centro'] if pd.notna(centro['centro']) else 'S/N',
                        'docentes_inicial': int(centro['doc_inicial']),
                        'docentes_primario': int(centro['doc_primario']),
                        'docentes_secundario': int(centro['doc_secundario'])
                    })
                
                datos_regional['distritos'].append(datos_distrito)
            
            self.datos_procesados['regionales'].append(datos_regional)
        
        # Calcular estadísticas globales
        self.datos_procesados['estadisticas'] = {
            'total_docentes_inicial': int(self.df['doc_inicial'].sum()),
            'total_docentes_primario': int(self.df['doc_primario'].sum()),
            'total_docentes_secundario': int(self.df['doc_secundario'].sum()),
            'total_docentes': int(self.df['doc_inicial'].sum() + self.df['doc_primario'].sum() + self.df['doc_secundario'].sum()),
            'total_centros': int(self.df['codigo_centro'].nunique()),
            'total_distritos': int(self.df['distrito'].nunique()),
            'total_regionales': int(self.df['regional'].nunique())
        }
        
        print("Datos procesados correctamente")
        return self.datos_procesados
    
    def guardar_json(self, ruta_salida):
        """Guardar datos procesados en JSON"""
        print(f"Guardando JSON en {ruta_salida}...")
        with open(ruta_salida, 'w', encoding='utf-8') as f:
            json.dump(self.datos_procesados, f, indent=2, ensure_ascii=False)
        print(f"JSON guardado correctamente")
    
    def ejecutar(self):
        """Ejecutar el procesamiento completo"""
        self.cargar_datos()
        self.procesar_datos()
        
        # Guardar JSON en la carpeta de la aplicación web
        ruta_json = Path(self.ruta_excel).parent / 'datos.json'
        self.guardar_json(ruta_json)
        
        # Mostrar resumen
        print("\n" + "="*60)
        print("RESUMEN DE DATOS PROCESADOS")
        print("="*60)
        stats = self.datos_procesados['estadisticas']
        print(f"Total de Regionales: {stats['total_regionales']}")
        print(f"Total de Distritos: {stats['total_distritos']}")
        print(f"Total de Centros Educativos: {stats['total_centros']}")
        print(f"\nDocentes por nivel:")
        print(f"  - Nivel Inicial: {stats['total_docentes_inicial']}")
        print(f"  - Nivel Primario: {stats['total_docentes_primario']}")
        print(f"  - Nivel Secundario: {stats['total_docentes_secundario']}")
        print(f"  - TOTAL: {stats['total_docentes']}")
        print("="*60 + "\n")
        
        return ruta_json


class ProcesadorReordenamiento:
    """Procesa el archivo de Reordenamiento de docentes"""
    
    def __init__(self, ruta_excel):
        self.ruta_excel = ruta_excel
        self.df = None
        self.datos_procesados = {
            'regionales': [],
            'estadisticas': {}
        }
    
    def cargar_datos(self):
        """Cargar el archivo Excel de Reordenamiento"""
        print("Cargando archivo de Reordenamiento...")
        # Leer el archivo saltando las primeras 4 filas de encabezado
        self.df = pd.read_excel(self.ruta_excel, sheet_name=0, header=4)
        
        # Renombrar columnas
        self.df.columns = [
            'vacio1', 'regional', 'distrito', 
            'faltante_inicial', 'excedente_inicial', 'completo_inicial',
            'faltante_primario', 'excedente_primario', 'completo_primario',
            'faltante_secundario', 'excedente_secundario', 'completo_secundario',
            'vacio2', 'vacio3', 'vacio4', 'vacio5'
        ]
        
        # Filtrar solo las filas con datos reales
        self.df = self.df[self.df['regional'].notna()].copy()
        self.df = self.df[~self.df['regional'].str.contains('Regional', na=False, case=False)]
        
        # Convertir a números
        for col in ['faltante_inicial', 'excedente_inicial', 'completo_inicial',
                    'faltante_primario', 'excedente_primario', 'completo_primario',
                    'faltante_secundario', 'excedente_secundario', 'completo_secundario']:
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce').fillna(0).astype(int)
        
        print(f"Datos cargados: {len(self.df)} registros")
        return self.df
    
    def procesar_datos(self):
        """Procesar datos de reordenamiento"""
        print("Procesando datos de Reordenamiento...")
        
        # Obtener regionales únicas (excluir filas sin distrito que son totales)
        regionales_unicas = self.df[self.df['distrito'].notna()]['regional'].unique()
        regionales_unicas = sorted([r for r in regionales_unicas if pd.notna(r)])
        
        for regional in regionales_unicas:
            df_regional = self.df[self.df['regional'] == regional]
            df_regional_distritos = df_regional[df_regional['distrito'].notna()].copy()
            
            datos_regional = {
                'nombre': regional,
                'codigo': regional.split('-')[0].strip() if '-' in regional else regional,
                'distritos': []
            }
            
            # Procesar cada distrito
            distritos = df_regional_distritos['distrito'].unique()
            distritos = sorted([d for d in distritos if pd.notna(d)])
            
            for distrito in distritos:
                df_distrito = df_regional_distritos[df_regional_distritos['distrito'] == distrito]
                
                if len(df_distrito) > 0:
                    fila = df_distrito.iloc[0]
                    datos_distrito = {
                        'nombre': distrito,
                        'codigo': distrito.split('-')[0].strip() if '-' in distrito else distrito,
                        'inicial': {
                            'faltante': int(fila['faltante_inicial']),
                            'excedente': int(fila['excedente_inicial']),
                            'completo': int(fila['completo_inicial'])
                        },
                        'primario': {
                            'faltante': int(fila['faltante_primario']),
                            'excedente': int(fila['excedente_primario']),
                            'completo': int(fila['completo_primario'])
                        },
                        'secundario': {
                            'faltante': int(fila['faltante_secundario']),
                            'excedente': int(fila['excedente_secundario']),
                            'completo': int(fila['completo_secundario'])
                        }
                    }
                    datos_regional['distritos'].append(datos_distrito)
            
            if datos_regional['distritos']:
                self.datos_procesados['regionales'].append(datos_regional)
        
        # Calcular estadísticas globales
        total_faltante_inicial = self.df[self.df['distrito'].notna()]['faltante_inicial'].sum()
        total_excedente_inicial = self.df[self.df['distrito'].notna()]['excedente_inicial'].sum()
        total_faltante_primario = self.df[self.df['distrito'].notna()]['faltante_primario'].sum()
        total_excedente_primario = self.df[self.df['distrito'].notna()]['excedente_primario'].sum()
        total_faltante_secundario = self.df[self.df['distrito'].notna()]['faltante_secundario'].sum()
        total_excedente_secundario = self.df[self.df['distrito'].notna()]['excedente_secundario'].sum()
        
        self.datos_procesados['estadisticas'] = {
            'total_regionales': len(regionales_unicas),
            'inicial': {
                'faltante': int(total_faltante_inicial),
                'excedente': int(total_excedente_inicial)
            },
            'primario': {
                'faltante': int(total_faltante_primario),
                'excedente': int(total_excedente_primario)
            },
            'secundario': {
                'faltante': int(total_faltante_secundario),
                'excedente': int(total_excedente_secundario)
            }
        }
        
        print("Datos procesados correctamente")
        return self.datos_procesados
    
    def guardar_json(self, ruta_salida):
        """Guardar datos procesados en JSON"""
        print(f"Guardando JSON en {ruta_salida}...")
        with open(ruta_salida, 'w', encoding='utf-8') as f:
            json.dump(self.datos_procesados, f, indent=2, ensure_ascii=False)
        print(f"JSON guardado correctamente")
    
    def ejecutar(self):
        """Ejecutar el procesamiento completo"""
        self.cargar_datos()
        self.procesar_datos()
        
        # Guardar JSON
        ruta_json = Path(self.ruta_excel).parent / 'datos_reordenamiento.json'
        self.guardar_json(ruta_json)
        
        # Mostrar resumen
        print("\n" + "="*60)
        print("RESUMEN DE REORDENAMIENTO")
        print("="*60)
        stats = self.datos_procesados['estadisticas']
        print(f"Total de Regionales: {stats['total_regionales']}")
        print(f"\nNivel Inicial:")
        print(f"  - Personal Faltante: {stats['inicial']['faltante']}")
        print(f"  - Personal Excedente: {stats['inicial']['excedente']}")
        print(f"\nNivel Primario:")
        print(f"  - Personal Faltante: {stats['primario']['faltante']}")
        print(f"  - Personal Excedente: {stats['primario']['excedente']}")
        print(f"\nNivel Secundario:")
        print(f"  - Personal Faltante: {stats['secundario']['faltante']}")
        print(f"  - Personal Excedente: {stats['secundario']['excedente']}")
        print("="*60 + "\n")
        
        return ruta_json


if __name__ == '__main__':
    # Procesar archivo de docentes
    print("[1] Procesando archivo de docentes...")
    ruta_excel = Path(__file__).parent / 'docente XLSX.xlsx'
    procesador = ProcesadorDatos(ruta_excel)
    procesador.ejecutar()
    
    # Procesar archivo de reordenamiento
    print("\n[2] Procesando archivo de reordenamiento...")
    ruta_reordenamiento = Path(__file__).parent / 'Reordenamiento XLSX (2).xlsx'
    if ruta_reordenamiento.exists():
        procesador_reord = ProcesadorReordenamiento(ruta_reordenamiento)
        procesador_reord.ejecutar()
    else:
        print(f"Archivo no encontrado: {ruta_reordenamiento}")
