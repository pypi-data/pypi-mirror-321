try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='defirl',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    platforms='any',
    version='0.1.3',
    description='A reinforcement learning package for predicting buy and sell signals',
    license='MIT',
    author='Nicolus Rotich',
    author_email='nicholas.rotich@gmail.com',
    install_requires=[
    	"setuptools>=58.1.0",
    	"wheel>=0.37.1",
        "scikit-learn>=1.4.0",
        "fire"
    ],
    url='https://nkrtech.com',
    download_url='https://github.com/moinonin/defirl/archive/refs/heads/main.zip',
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
)
