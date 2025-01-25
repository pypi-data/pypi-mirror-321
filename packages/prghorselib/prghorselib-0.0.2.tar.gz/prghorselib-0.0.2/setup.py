from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='prghorselib',
  version='0.0.2',
  author='Alx',
  author_email='proshka20081010@gmail.com',
  description='A library specifically for the prghorse team',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/alxprgs/prghorselib',
  packages=find_packages(),
  install_requires=['motor>=3.6.0', 'fastapi>=0.115.5', 'psutil>=6.1.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='prghorse',
  project_urls={},
  python_requires='>=3.10'
)