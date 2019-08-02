from setuptools import setup

setup(
    name='simpleKasa',
    version='0.1.2',
    packages=['simpleKasa'],
    url='https://github.com/jarbasal/simpleKasa',
    install_requires=["pyHS100", 'webcolors'],
    license='MIT',
    author='jarbasai',
    author_email='jarbasai@mailfence.com',
    description='control tplink Kasa devices'
)
