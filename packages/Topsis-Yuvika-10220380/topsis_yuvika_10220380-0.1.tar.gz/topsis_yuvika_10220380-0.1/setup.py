from setuptools import setup, find_packages

setup(
    name='Topsis-Yuvika-10220380',
    version='0.1',
    author='Yuvika',
    author_email='yuvikasardana@gmail.com',
    description='A Python package for TOPSIS',
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    entry_points={
        'console_scripts': [
            'topsis = Topsis_Yuvika_102203800.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
