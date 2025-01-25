from setuptools import setup

version = '0.1'

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name='heos-link-control-proxy',
    packages=['heos-link-control-proxy'],
    package_dir={'': 'src'},
    version=version,
    license='Apache 2.0',
    description='Control proxy for Denon HEOS link',
    long_description=long_descr,
    long_description_content_type='text/markdown',
    author='foxy82',
    author_email='foxy82.github@gmail.com',
    url='https://github.com/designer-living/heos-link-control-proxy',
    download_url=f'https://github.com/designer-living/heos-link-control-proxy/archive/{version}.tar.gz',
    keywords=['Denon', 'HEOS'],
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.10'
    ],
)
