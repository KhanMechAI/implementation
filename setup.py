from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='implementation',
    url='https://github.com/KhanMechAI/ass2',
    author='Khan Schroder-Turner',
    author_email='khan.schroderturner@gmail.com',
    # Needed to actually package something
    packages=['implementation', 'runner'],
    # Needed for dependencies
    install_requires=[],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Code for an Assignment',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)