from setuptools import find_packages, setup
from typing import List

Hypen_e_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements from the file
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)
    print(requirements)
    return requirements
        

setup(
    name='my_package',
    version='0.0.1',
    author='Rehman Sadaqat',
    author_email='zaynali0987@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)

print("Install requires:", get_requirements("requirements.txt"))