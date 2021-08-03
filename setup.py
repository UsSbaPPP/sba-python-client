from setuptools import setup

setup(
   name='PPPForgivenessSDK',
   version='1.4',
   description='api support for Paycheck Protection Program Portal',
   author='',
   author_email='',
   url='https://sandbox.ussbaforgiveness.com/',
   packages=['PPPForgivenessSDK'],
   install_requires=['python-dateutil', 'requests'],
   python_requires= '>2.7,!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',

)