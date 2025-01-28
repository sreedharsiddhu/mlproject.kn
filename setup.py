from setuptools import find_packages,setup
from typing import List


hyfen_e_dot="-e ."
def get_requirements(file_path:str)->List[str]:
    
    """
    this function will return the list of requiremnts
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements =file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if hyfen_e_dot in requirements:
            requirements.remove(hyfen_e_dot)
    return
        
setup(
name ="mlproject", 
version="0.0.1",
author="sree",
author_email="sreedharsiddhu1998@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

    
    
)