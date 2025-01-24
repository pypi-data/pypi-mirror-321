import logging
import os
import shutil
import subprocess

from graph_sitter.core.external.external_process import ExternalProcess

logger = logging.getLogger(__name__)


class TSDeclassify(ExternalProcess):
    def __init__(self, repo_path: str, base_path: str, working_dir: str = "/tmp/ts_declassify"):
        super().__init__(repo_path, base_path)
        self.working_dir = working_dir

        # Ensure NodeJS and npm are installed
        if not shutil.which("node") or not shutil.which("npm"):
            raise RuntimeError("NodeJS or npm is not installed")

    def _start(self):
        try:
            logger.info("Installing ts-declassify...")

            # Remove existing working directory
            if os.path.exists(self.working_dir):
                shutil.rmtree(self.working_dir)

            # Creating ts-declassify working directory
            os.makedirs(self.working_dir, exist_ok=True)

            # NPM Init
            try:
                logger.info(f"Running npm init in {self.working_dir}")
                subprocess.run(["npm", "init", "-y"], cwd=self.working_dir, check=True, capture_output=True, text=True)
            except subprocess.CalledProcessError as e:
                logger.error(f"NPM FAIL: npm init failed with exit code {e.returncode}")
                logger.error(f"NPM FAIL stdout: {e.stdout}")
                logger.error(f"NPM FAIL stderr: {e.stderr}")
                raise

            # NPM Install
            try:
                logger.info(f"Running npm install in {self.working_dir}")
                subprocess.run(["npm", "install", "-D", "@codemod/cli", "react-declassify"], cwd=self.working_dir, check=True, capture_output=True, text=True)
            except subprocess.CalledProcessError as e:
                logger.error(f"NPM FAIL: npm install failed with exit code {e.returncode}")
                logger.error(f"NPM FAIL stdout: {e.stdout}")
                logger.error(f"NPM FAIL stderr: {e.stderr}")
                raise

            # Finalize
            self.is_ready = True
        except Exception as e:
            self._error = e
            logger.error(f"Error installing ts-declassify: {e}")
            raise e

    def reparse(self):
        raise NotImplementedError("TSDeclassify does not support reparse")

    def declassify(self, source: str, filename: str = "file.tsx", error_on_failure: bool = True):
        assert self.ready(), "TSDeclassify is not ready"

        try:
            # Remove and recreate file.tsx
            source_file = os.path.join(self.working_dir, filename)
            with open(source_file, "w") as f:
                f.write(source)

            # Run declassify
            try:
                subprocess.run(["npx", "codemod", "--plugin", "react-declassify", source_file], cwd=self.working_dir, check=True, capture_output=True, text=True)
            except subprocess.CalledProcessError as e:
                logger.error(f"DECLASSIFY FAIL: declassify failed with exit code {e.returncode}")
                logger.error(f"DECLASSIFY FAIL stdout: {e.stdout}")
                logger.error(f"DECLASSIFY FAIL stderr: {e.stderr}")
                raise

            # Get the declassified source
            with open(source_file) as f:
                declassified_source = f.read()

            # Raise an error if the declassification failed
            if error_on_failure and "Cannot perform transformation" in declassified_source:
                raise RuntimeError("Declassification failed!")
        finally:
            # Remove file.tsx if it exists
            if os.path.exists(source_file):
                os.remove(source_file)

        return declassified_source
