from setuptools import setup, find_packages

setup(
    name='luogu-api-python',
    description='python implement of luogu API',
    version='0.0.1',
    packages=['pyLuogu', 'pyLuogu.bits'],
    install_requires=["requests", "beautifulsoup4"],
    url='https://github.com/NekoOS-Group/luogu-api-python',
    license='GLP3.0',
    author='bzy',
    author_email='bzy.cirno@gmail.com'
)
