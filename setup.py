from setuptools import setup

setup(name='wrapymongo',
      version='0.1',
      description='A wrapper for pymonogo driver',
      url='http://github.com/shreyasgokhale/wrapymongo',
      author='Shreyas Gokhale',
      author_email='shreyasgokhale@gmail.com',
      license='MIT',
      long_description='Really, the funniest around.',
      keywords=["mongo", "mongodb", "pymongo", "mongodriver", "wrapymongo"],
      packages=['wrapymongo'],
      install_requires=[
          'pymongo',
      ],
      zip_safe=False)
