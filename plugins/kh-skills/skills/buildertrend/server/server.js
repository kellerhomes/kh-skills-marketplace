// KH Job Hub server — zero dependencies, plain Node.
// Serves the app from ./public, job data from ./jobs.json, and stores
// shared schedule edits in ./edits.json. Run: node server.js
const http = require("http");
const fs = require("fs");
const path = require("path");

const PORT = process.env.PORT || 8787;
const ROOT = __dirname;
const PUB = path.join(ROOT, "public");
const MIME = {
  ".html": "text/html; charset=utf-8",
  ".json": "application/json",
  ".png": "image/png",
  ".svg": "image/svg+xml",
  ".ico": "image/x-icon",
};

function send(res, code, body, type) {
  res.writeHead(code, {
    "Content-Type": type || "text/plain",
    "Cache-Control": "no-store",
  });
  res.end(body);
}

function sendFile(res, file) {
  fs.readFile(file, (err, data) => {
    if (err) return send(res, 404, "not found");
    send(res, 200, data, MIME[path.extname(file)] || "application/octet-stream");
  });
}

const server = http.createServer((req, res) => {
  const u = decodeURIComponent(req.url.split("?")[0]);

  if (u === "/api/jobs") return sendFile(res, path.join(ROOT, "jobs.json"));

  if (u === "/api/edits") {
    if (req.method === "POST") {
      let body = "";
      req.on("data", (c) => {
        body += c;
        if (body.length > 1e6) req.destroy(); // 1 MB cap
      });
      req.on("end", () => {
        try {
          JSON.parse(body); // validate
          fs.writeFileSync(path.join(ROOT, "edits.json"), body);
          send(res, 200, "{}", "application/json");
        } catch (e) {
          send(res, 400, "bad json");
        }
      });
      return;
    }
    const f = path.join(ROOT, "edits.json");
    if (fs.existsSync(f)) return sendFile(res, f);
    return send(res, 200, "{}", "application/json");
  }

  // static files from ./public, path-traversal safe
  const file = path.normalize(path.join(PUB, u === "/" ? "index.html" : u));
  if (!file.startsWith(PUB)) return send(res, 403, "forbidden");
  sendFile(res, file);
});

server.listen(PORT, () => {
  console.log("KH Job Hub running.");
  console.log("  On this machine:  http://localhost:" + PORT);
  const nets = require("os").networkInterfaces();
  for (const list of Object.values(nets))
    for (const n of list)
      if (n.family === "IPv4" && !n.internal)
        console.log("  On your network:  http://" + n.address + ":" + PORT);
});
