from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):                    # 有人用 GET 來敲門時，執行這裡
        self.send_response(200)          # 狀態碼：成功
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()               # 標頭結束，接下來是 Body
        self.wfile.write("國立臺中科技大學".encode("utf-8"))

if __name__ == "__main__":
    print("聽在 http://127.0.0.1:8000  （按 Ctrl+C 結束）")
    HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()