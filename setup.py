from setuptools import setup


setup(
    name='site_checker',
    author='Shivam Garg',
    version='0.1',
    py_modules=['run', 'checker'],
    package_dir={'':'site_checker'},
    install_requires=[
        'Click',
        'requests',
        'bs4',
        'plyer',
        'lxml'
    ],
    entry_points='''
        [console_scripts]
        checker=run:cli
    ''',
)
