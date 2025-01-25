from setuptools import setup, find_packages

setup(
    name='lulu_api',
    version='0.1.1',
    description='Un package pour l\'API Lulu',
    author='Looming Team',
    author_email='devteam@looming.zone',
    url='https://github.com/LoomingPlatform/looming-ai/packages/lulu_api',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
