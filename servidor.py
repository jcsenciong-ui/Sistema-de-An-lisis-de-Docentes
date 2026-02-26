#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Servidor web simple para servir la aplicación
"""

import http.server
import socketserver
import os
from pathlib import Path

class MiHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Agregar headers para evitar caché
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {format % args}")

if __name__ == '__main__':
    os.chdir(Path(__file__).parent)
    
    PORT = 8000
    Handler = MiHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"✅ Servidor iniciado en http://localhost:{PORT}")
        print(f"📂 Directorio: {os.getcwd()}")
        print(f"📄 Accede a: http://localhost:{PORT}/index.html")
        print(f"\nPresiona Ctrl+C para detener el servidor")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n⛔ Servidor detenido")
