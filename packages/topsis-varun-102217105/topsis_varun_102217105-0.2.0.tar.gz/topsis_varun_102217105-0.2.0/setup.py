from setuptools import setup, find_packages

VERSION = '0.2.0'
DESCRIPTION = 'Technique for Order Preference by Similarity to Ideal Solution(TOPSIS) Package'

# Setting up
setup(
    name="topsis_varun_102217105",
    version=VERSION,
    author="Varun Kumar",
    author_email="varunkumar2004.vk@gmail.com",
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['numpy', 'pandas', 'openpyxl'],
    keywords=['python', 'topsis', 'multi-criteria decision-making', 'mcdm', 'ranking'],
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)