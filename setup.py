from setuptools import setup
from setuptools.command.build_py import build_py
import subprocess

class BuildWithDocs(build_py):
    def run(self):
        # Gera a documentação estática
        subprocess.run(["mkdocs", "build"], check=True)
        # Executa o build normal
        super().run()

setup(
    cmdclass={
        "build_py": BuildWithDocs,
    },
)