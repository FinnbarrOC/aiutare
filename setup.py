#!/usr/bin/env python3
import os
import sys
import platform
import importlib
from subprocess import call, DEVNULL


PIP_DEPENDENCIES = [
        'setuptools',
        'pymongo',
        'mongoengine',
        'progressbar2',
        'tabulate',
        'numpy',
        'scipy',
        'plotly',
        'psutil'
]


def pip_install(package):
    call(["pip3", "install", "--user", package], stdout=DEVNULL)


def main():
    print("Creating directory structure")
    os.makedirs("results/log", exist_ok=True)
    os.makedirs("plots", exist_ok=True)
    if platform.system() != "Windows":
        uid = os.getuid()
        os.chown("results", uid, -1)
        os.chown("results/log", uid, -1)
        os.chown("plots", uid, -1)

    for root, dirs, files in os.walk("results"):
        for file in dirs:
            os.chmod(os.path.join(root, file), 0o0777)
        for file in files:
            os.chmod(os.path.join(root, file), 0o0777)

    print("Installing pip dependencies")
    call(["pip3", "install", "--upgrade", "pip", "--user"], stdout=DEVNULL)
    for dependency in PIP_DEPENDENCIES:
        pip_install(dependency)

    print("Calling setuptools.setup function")
    import site
    importlib.reload(site)
    import setuptools
    with open("README.md", "r") as fh:
        long_description = fh.read()

    setuptools.setup(
        name="aiutare",
        version="1.0",
        author="Lukas Finnbarr O'Callahan, Federico Mora",
        author_email="lukasocallahan@gmail.com, fmora@cs.toronto.edu",
        description="A benchmarking framework for SAT, SMT, and equivalence checking programs.",
        long_description=long_description,
        url="https://github.com/FedericoAureliano/aiutare",
        scripts=[
            'bin/aiutare',
            'bin/plot',
            'bin/verify'
        ],
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: POSIX :: Linux",
            "Operating System :: Microsoft :: Windows",
        ],
        requires=PIP_DEPENDENCIES,
    )

    from bin.mongod_manager import start_server

    try:
        start_server()
    except Exception as e:
        print(e)
        print("Please ensure you have the latest version of MongoDB installed.")

    print("\nSetup successful!")


if __name__ == '__main__':
    main()
