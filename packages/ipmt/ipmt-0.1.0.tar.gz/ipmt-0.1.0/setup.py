from setuptools import find_packages, setup

setup(
    name='ipmt',
    packages=find_packages(include=['manager']),
    author_email="nightxcros@gmail.com",
    version='0.1.0',
    description='This is a flask ip management dependencys wich can use to manage ip address and visitors and protect your website from ddos attacks',
    author='night9a',
    install_requires=[],
    setup_requires=['flask','Flask-Limiter'],
)