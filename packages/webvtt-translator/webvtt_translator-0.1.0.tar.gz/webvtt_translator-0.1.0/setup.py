from setuptools import setup, find_packages

setup(
    name='webvtt_translator',
    version='0.1.0',
    author='Sergio Sousa',
    author_email='shenrique@gmail.com',
    description='An automated translator of WebVTT (Web Video Text Tracks) from one language to another using generative AI.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my-python-project',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'webvtt-translator=webvtt_translator.main:main',
        ],
    },
    install_requires=[
        'openai',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)