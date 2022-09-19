try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A example from lpthw, exercise 47',
    'author': 'James Bay',
    'url': 'URL to get it at',
    'download_url': 'Where to download it.',
    'author_email': 'hwy1249171331@gmail.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)