# KH Job Hub server — Python fallback (stdlib only), for machines without Node.
# Run: python server.py   (or py server.py on Windows)
import json, os, socket
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = int(os.environ.get("PORT", 8787))
ROOT = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(ROOT, "public")
MIME = {".html": "text/html; charset=utf-8", ".json": "application/json",
        ".png": "image/png", ".svg": "image/svg+xml", ".ico": "image/x-icon"}


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="text/plain"):
        if isinstance(body, str):
            body = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _file(self, path):
        try:
            with open(path, "rb") as f:
                data = f.read()
            self._send(200, data, MIME.get(os.path.splitext(path)[1], "application/octet-stream"))
        except OSError:
            self._send(404, "not found")

    def do_GET(self):
        u = self.path.split("?")[0]
        if u == "/api/jobs":
            return self._file(os.path.join(ROOT, "jobs.json"))
        if u == "/api/edits":
            f = os.path.join(ROOT, "edits.json")
            return self._file(f) if os.path.exists(f) else self._send(200, "{}", "application/json")
        f = os.path.normpath(os.path.join(PUB, "index.html" if u == "/" else u.lstrip("/")))
        if not f.startswith(PUB):
            return self._send(403, "forbidden")
        self._file(f)

    def do_POST(self):
        if self.path.split("?")[0] != "/api/edits":
            return self._send(404, "not found")
        n = int(self.headers.get("Content-Length", 0))
        if n > 1_000_000:
            return self._send(413, "too large")
        body = self.rfile.read(n)
        try:
            json.loads(body)
        except ValueError:
            return self._send(400, "bad json")
        with open(os.path.join(ROOT, "edits.json"), "wb") as f:
            f.write(body)
        self._send(200, "{}", "application/json")

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    print("KH Job Hub running.")
    print(f"  On this machine:  http://localhost:{PORT}")
    try:
        ip = socket.gethostbyname(socket.gethostname())
        print(f"  On your network:  http://{ip}:{PORT}")
    except OSError:
        pass
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
