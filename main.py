import os
import http.server
import socketserver

PORT = int(os.environ.get("PORT", 3000))
Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({".html": "text/html", ".css": "text/css"})

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
