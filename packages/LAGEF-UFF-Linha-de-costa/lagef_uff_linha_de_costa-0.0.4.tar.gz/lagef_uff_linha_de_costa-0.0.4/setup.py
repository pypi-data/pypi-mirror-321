from setuptools import setup

with open('README.md','r') as arq:
    readme = arq.read()

setup(name='LAGEF-UFF-Linha_de_costa',
    version='0.0.4',
    license='MIT License',
    author='Pablo Simoes',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='pablosergio.simoes@gmail.com',
    keywords=['lagef uff','linha de costa','google earth engine'],
    description=u'Scripts para análise de linha de costa',
    packages=['LAGEF_UFF'],
    install_requires=['pandas','geemap','numpy','earthengine-api','scikit-image','matplotlib'],)







