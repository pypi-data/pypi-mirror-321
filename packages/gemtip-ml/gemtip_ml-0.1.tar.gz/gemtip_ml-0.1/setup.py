from setuptools import setup, find_packages

setup(
    name='gemtip-ml',
    version='0.1',
    packages=find_packages(),
    install_requires=["torch","matplotlib","scipy","torchquad" 
    ],
    author='Charles L. Bérubé, Jean-Luc Gagnon',
    author_email='charles.berube@polymtl.ca, jean-luc.gagnon@polymtl.ca',
    description='A package for generation of synthetic anisotropic GEMTIP data',
    url='https://github.com/clberube/gemtip-ml',
)
