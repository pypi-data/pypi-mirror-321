from setuptools import setup
from setuptools.command.install import install
import os
import shutil
import sys
import platform

class CustomStemInstallCommand(install):
    def run(self):
        r"""
        Install packages STEM Application and KratosMultiphysics
        """
        # Call the default install process
        install.run(self)
        self.run_custom_command()

    def run_custom_command(self):
        """
        Run the custom command to move the package STEMApplication into the KratosMultiphysics
        This needs to be executed after the packages have been installed
        """
        # Custom logic to move data from my_package to another_package
        source_path = os.path.join(self.install_lib, os.path.join('StemKratos','StemApplication'))
        destination_path = os.path.join(self.install_lib, 'KratosMultiphysics')

        # Ensure the destination directory exists
        os.makedirs(destination_path, exist_ok=True)

        # Move the entire directory
        shutil.move(source_path, destination_path)


if __name__ == '__main__':
    setup(
         dependency_links=[
        'KratosLinearSolversApplication-9.5.0.6-cp310-cp310-win_amd64.whl'
    ],
        cmdclass={
            'install': CustomStemInstallCommand,
    })
