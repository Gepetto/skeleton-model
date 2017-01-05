from setuptools import setup, find_packages

setup(
    name='models',
    description='Biomechanical and Robotic Models',
    version='1.0',

    packages=find_packages(exclude=['data','tests']),
    
    author='Galo MALDONADO',
    author_email='galo.maldonado@laas.fr',
    
    #extras_requires = [
    #    "pinocchio"
    #],

    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],

)
