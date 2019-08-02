from setuptools import setup

setup(
    name='simpleKasa',
    version='0.1.1',
    packages=['simpleKasa', 'webcolors'],
    url='',
    install_requires=["pyHS100"],
    license='MIT',
    author='jarbasai',
    author_email='jarbasai@mailfence.com',
    description='control tplink Kasa devices'
)
