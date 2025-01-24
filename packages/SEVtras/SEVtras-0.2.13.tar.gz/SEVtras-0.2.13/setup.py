from setuptools import setup

setup(
    name='SEVtras',
    version='0.2.13',
    author='Ruiqiao He',
    author_email='ruiqiaohe@gmail.com',
    packages=['SEVtras'],
    license="GPL",
    url='http://pypi.python.org/pypi/SEVtras/',
    description='sEV-containing droplet identification in scRNA-seq data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "numpy>=1.21.5,<2.0.0",
        "pandas>=1.1.2,<2.2.0",
        "scipy>=1.5.4,<1.13.1",
        "statsmodels>=0.12.1,<0.14.4",
        "anndata>=0.7.4,<0.11.1",
        "gseapy==0.14.0",
        'umap-learn==0.5.3',#3.10
        # "scanpy==1.8.1",
    ],
    python_requires='>=3.7.1',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
      ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'SEVtras=SEVtras.main:SEVtras_command',
        ]
    }
)
