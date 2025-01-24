from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='hanzi_pinyin',
    version='0.2.3',
    packages=find_packages(),
    description='Query the pinyin of Chinese characters.',
    long_description=Path('README.md').read_text(encoding='utf-8'),
    long_description_content_type='text/markdown',
    author='neooier',
    author_email='53945377+neooier@users.noreply.github.com',
    url='https://github.com/neooier/hanzi_pinyin',
    install_requires=[
        'unidecode',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
