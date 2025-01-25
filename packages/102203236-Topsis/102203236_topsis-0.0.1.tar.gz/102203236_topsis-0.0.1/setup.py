from setuptools import setup, find_packages

setup(
    name='102203236_Topsis',  
    version='0.0.1',
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    author='Pranav Khurana',
    author_email='pranavkhurana117@gmail.com',
    description='A Python package for TOPSIS multi-criteria decision making',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/PranavKhurana117?tab=repositories',  
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
)
