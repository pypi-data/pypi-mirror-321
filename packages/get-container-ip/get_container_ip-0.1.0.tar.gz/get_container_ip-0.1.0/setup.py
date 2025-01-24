from setuptools import setup, find_packages

setup(
  name='get_container_ip',
  version='0.1.0',
  packages=find_packages(include=['get_container_ip', 'get_container_ip.*']),
  install_requires=[
    'argparse',
    'logging',
  ],
  author='Koent S.r.l.',
  author_email='tools@koent.it',
  description='Un package per ottenere l\'indirizzo IP di un container.',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/Koent-it/get_container_ip',
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
  python_requires='>=3.6',
)