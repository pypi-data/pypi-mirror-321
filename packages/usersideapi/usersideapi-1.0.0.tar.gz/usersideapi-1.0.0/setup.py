from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='usersideapi',
  version='1.0.0',
  author='Andrey Litvinov',
  author_email='busybeaver.bb@gmail.com',
  description='Библиотека для работы с API запросами ERP UserSide/WorkNet',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/BusyBeaver54/usersideap',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='userside worknet api',
  project_urls={
    'Documentation': 'https://github.com/BusyBeaver54/usersideapi?tab=readme-ov-file'
  },
  python_requires='>=3.8'
)