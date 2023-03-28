from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .' # THis hypen e in reuirements automatically trigger the setup file

def get_requirements(file_path:str)->List[str]:
    # This function will return the list of requirements
    requiremnets=[]
    with open('requirements.txt') as file_obj:
        requiremnets = file_obj.readlines()
        requirements=[req.replace("\n","")for req in requiremnets]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
name='MLProject',
version='0.0.1',
author='Asif',
author_email='mohamed.asif.2k23@gmail.com',
packages = find_packages(),
install_requires=get_requirements('requirements.txt')

)