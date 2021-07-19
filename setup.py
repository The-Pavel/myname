from setuptools import setup

# list dependencies from file
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name='myname',
      description="Display my name",
      packages=["myname"],
      install_requires=requirements,
      scripts=['scripts/myname-run'])
