import json
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path


class CurlSmokeTest(unittest.TestCase):
    def test_curl_gets_root_response(self):
        curl = shutil.which("curl.exe") or shutil.which("curl")
        if curl is None:
            self.skipTest("curl executable is not installed")

        with socket.socket() as sock:
            sock.bind(("127.0.0.1", 0))
            port = sock.getsockname()[1]

        project_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryFile() as server_log:
            server = subprocess.Popen(
                [
                    sys.executable,
                    "-m",
                    "uvicorn",
                    "main:app",
                    "--host",
                    "127.0.0.1",
                    "--port",
                    str(port),
                ],
                cwd=project_root,
                stdout=server_log,
                stderr=subprocess.STDOUT,
            )

            try:
                deadline = time.monotonic() + 10
                while time.monotonic() < deadline:
                    if server.poll() is not None:
                        server_log.seek(0)
                        output = server_log.read().decode(errors="replace")
                        self.fail(f"Uvicorn exited before becoming ready:\n{output}")

                    with socket.socket() as connection:
                        connection.settimeout(0.1)
                        if connection.connect_ex(("127.0.0.1", port)) == 0:
                            break
                    time.sleep(0.1)
                else:
                    self.fail("Uvicorn did not become ready within 10 seconds")

                result = subprocess.run(
                    [
                        curl,
                        "--fail",
                        "--silent",
                        "--show-error",
                        "--max-time",
                        "5",
                        f"http://127.0.0.1:{port}/",
                    ],
                    capture_output=True,
                    text=True,
                    timeout=7,
                    check=False,
                )

                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(
                    json.loads(result.stdout), {'message': 'Welcome to Gawab API', 'status': 'Running'}
                )
            finally:
                if server.poll() is None:
                    server.terminate()
                    try:
                        server.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        server.kill()
                        server.wait(timeout=5)


if __name__ == "__main__":
    unittest.main()
