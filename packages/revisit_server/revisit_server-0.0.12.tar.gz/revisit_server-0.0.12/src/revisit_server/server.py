import os
import subprocess
# from .run_server import run_server


def serve(port=8080):
    script_path = os.path.join(os.path.dirname(__file__), "run_server.py")
    command = ["python", script_path]
    print(command)
    # Run the server script in the background
    process = subprocess.Popen(
        command,  # Pass port as an argument
        stdout=subprocess.DEVNULL,             # Capture standard output
        stderr=subprocess.DEVNULL              # Capture standard error
    )

    print(f"Server is running in the background at http://localhost:{port}")

    return process
