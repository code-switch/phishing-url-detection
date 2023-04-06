from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    with open(file_path) as file_obj:
        content = file_obj.readlines()
        content = [req.replace('\n',' ') for req in content]

        if HYPEN_E_DOT in content:
            content.remove(HYPEN_E_DOT)
        

setup(
name = 'phishing_url_detection',
version = '0.0.1',
author = 'code-switch',
author_email='abhi.learner07@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)