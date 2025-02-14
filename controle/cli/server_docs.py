import http.server
import socketserver
import os
from pathlib import Path

def main():
    # Caminho para a documentação estática
    docs_dir = Path(__file__).parent.parent.parent / "docs" / "site"
    
    if not docs_dir.exists():
        print("Documentação não encontrada. Gere a documentação com 'mkdocs build'.")
        return

    # Define a porta (padrão: 8000)
    PORT = 8000

    # Muda para o diretório da documentação
    os.chdir(docs_dir)

    # Inicia o servidor HTTP
    with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
        print(f"Servindo documentação em http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    main()