from setuptools import setup

setup(name='wrapymongo',
      version='0.2',
      description='A wrapper for pymonogo driver',
      url='http://github.com/shreyasgokhale/wrapymongo',
      author='Shreyas Gokhale',
      author_email='shreyasgokhale@gmail.com',
      license='MIT',
      long_description='Wrapper modlue to handle our mongodb requests using pymongodb driver',
      keywords=["mongo", "mongodb", "pymongo", "mongodriver", "wrapymongo"],
      packages=['wrapymongo'],
      install_requires=[
          'pymongo',
      ],
      download_url = 'https://github.com/shreyasgokhale/wrapymongo/archive/v_02.tar.gz',
      classifiers=[
          # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
          'Development Status :: 3 - Alpha',
          # Define that your audience are developers
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'License :: OSI Approved :: MIT License',   # Again, pick a license
          # Specify which pyhton versions that you want to support
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],

      zip_safe=False)
