import http.server
import socketserver

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(('', PORT), Handler) as httpd:
#    print('Servidor local rodando')
    with open('db.json', 'r') as file:
        print(file.read())
    httpd.serve_forever()
