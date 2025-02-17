from setuptools import setup, find_packages
from setuptools.command.build_py import build_py

import subprocess

class BuildWithDocs(build_py):
    def run(self):
        # Gera a documentação estática
        subprocess.run(["mkdocs", "build"], check=True)
        # Executa o build normal
        super().run()

setup(
    name='HControll',
    version='0.2.0',
    description='Um projeto de controle de horas para uso pessoal.',
    author='Erik Marques',
    author_email='lucro.alternativo@outlook.com',
    url='https://github.com/ErckMarques/controlador-ponto.git',
    maintainer='Erik Marques',
    packages=find_packages(),
    python_requires='>=3.9',
    install_requires=[
        'dateparser',
    ],
    extras_require={
        'dev': ['taskipy'],
        'test': ['pytest', 'pytest-cov', 'coverage'],
        'doc': ['mkdocs', 'mkdocstrings[python]', 'mkdocs-material'],
    },
    include_package_data=True,
    zip_safe=False,
    cmdclass={
        'build_py': BuildWithDocs,
    },
    entry_points={
        'console_scripts': [
            'HControll = controle.__main__:main',
        ],
    },
)