from setuptools import setup

with open('README.MD','r') as arq:
    readme = arq.read()

setup(name='LAGEF-UFF-Shoreline',
    version='0.0.2',
    license='MIT License',
    author='Pablo Simoes',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='pablosergio.simoes@gmail.com',
    keywords='lagef uff',
    description=u'Wrapper não oficial do Panda Video',
    packages=['LAGEF_shoreline'],
    install_requires=['requests','pandas','geemap','numpy','earthengine-api'],)







