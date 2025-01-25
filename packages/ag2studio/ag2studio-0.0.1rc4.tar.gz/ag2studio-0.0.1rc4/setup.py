# Copyright (c) 2023 - 2025, Owners of https://github.com/ag2ai
#
# SPDX-License-Identifier: Apache-2.0
from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call
import os
import sys

class PreInstallCommand(install):
    """Pre-installation for installation mode."""
    def run(self):
        try:
            check_call([sys.executable, 'build_frontend.py'])
        except Exception as e:
            print(f"Error building frontend: {e}")
            print("Continuing with installation...")
        install.run(self)

class PreDevelopCommand(develop):
    """Pre-installation for development mode."""
    def run(self):
        try:
            check_call([sys.executable, 'build_frontend.py'])
        except Exception as e:
            print(f"Error building frontend: {e}")
            print("Continuing with installation...")
        develop.run(self)

setup(
    cmdclass={
        'install': PreInstallCommand,
        'develop': PreDevelopCommand,
    }
)