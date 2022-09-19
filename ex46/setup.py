try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'An example from LPTHW Exercise 46',
    'author': 'James Bay',
    'url': 'https://baidu.com',
    'download_url': 'https://baidu.com',
    'author_email': 'hwy1249171331@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex46'],
    'scripts': [],
    'name': 'ex46'
}

setup(**config)