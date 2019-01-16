from setuptools import setup

setup(name='choicemaker',
      version='0.1',
      description='choice maker for you',
      url='https://github.com/vogu66/ChoiceMaker',
      author='vogu66',
      packages=['choicemaker'],
      entry_points = {
        'console_scripts': ['choose=choicemaker.command_line:main'],
    },
      zip_safe=False)
