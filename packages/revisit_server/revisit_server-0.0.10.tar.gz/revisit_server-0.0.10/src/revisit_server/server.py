from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
from multiprocessing import Process


class ReactHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve index.html for all unknown paths
        static_dir = os.path.join(os.path.dirname(__file__), "static")
        requested_path = os.path.join(static_dir, self.path.lstrip("/"))

        # Check if the requested path is a file
        if not os.path.isfile(requested_path):
            self.path = "/index.html"

        return super().do_GET()


def run_server(port):
    static_dir = os.path.join(os.path.dirname(__file__), "static")
    handler = ReactHandler
    handler.static_dir = static_dir  # Pass the static directory to the handler class
    server = HTTPServer(("localhost", port), handler)
    # print(f"Serving React app at http://localhost:{port}")
    server.serve_forever()


def serve(port=3000, detached=True):
    process = Process(target=run_server, args=(port,))

    # Set the process as a daemon if running in detached mode
    if detached:
        process.daemon = True
        process.start()
        print(f"Server is running in the background at http://localhost:{port}")
    else:
        # This will run the server directly in the current process (blocking)
        run_server(port)  # Blocks until the server is stopped

    return process  # Return the process to allow for later management (only if detached is True)
