from setuptools import find_packages, setup
from typing import List

minus_e_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    # This function will return the list of requirements
    req = []
    with open(file_path) as file_obj:
        req=file_obj.readlines()
        req = [r.replace("\n"," ") for r in req]
        if minus_e_dot in req:
            req.remove(minus_e_dot)
    return req

setup(
    name='EtoEMLProjects',
    version='0.0.1',
    author='Ranadeep',
    author_email='dema.ranadeepreddy2004@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)