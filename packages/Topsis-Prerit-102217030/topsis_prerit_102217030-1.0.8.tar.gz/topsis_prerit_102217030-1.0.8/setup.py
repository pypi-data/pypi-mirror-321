# from setuptools import setup, find_packages
# from pathlib import Path

# # Read the contents of your README file
# this_directory = Path(__file__).parent
# long_description = (this_directory / "README.md").read_text() #Gets the long description from Readme file

# setup(
#     name='TOPSIS_Prerit_102217030',
#     version='0.0',
#     packages=find_packages(),
#     install_requires=[
#         'pandas','numpy',
#     ],  # Add a comma here
#     author='Prerit Bhagat',
#     author_email='preritbhagat.pb@gmail.com',
#     description='This is the short description',

#     long_description=long_description,
#     long_description_content_type='text/markdown',
#     license='MIT',
#      project_urls={
#            'Source Repository': 'https://github.com/A-Sharan1/' #replace with your github source
#     }
# )

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")  # Explicit encoding for compatibility

setup(
    name='Topsis_Prerit_102217030',  # Package name must be unique on PyPI
    version='1.0.8',  # Initial release version
    packages=find_packages(),  # Automatically finds Python packages in the current directory
    install_requires=[
        'pandas>=1.0.0',  # Ensures compatibility with modern Pandas
        'numpy>=1.19.0',  # Ensures compatibility with modern NumPy
    ],
    author='Prerit Bhagat',
    author_email='preritbhagat.pb@gmail.com',
    description='A Python package for performing TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) analysis.',
    long_description=long_description,
    long_description_content_type='text/markdown',  # Specifies README format for PyPI rendering
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',  # Use "5 - Production/Stable" if it's ready for production
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='topsis mcdm multi-criteria decision-making ranking analysis',
    project_urls={
        'Documentation': 'https://github.com/Prerit-Bhagat/PYPI_Package#readme',  # Replace with the actual documentation link
        'Source': 'https://github.com/Prerit-Bhagat/PYPI_Package',  # Link to the GitHub repository
        # 'Bug Tracker': 'https://github.com/Prerit-Bhagat/PYPI_Package/issues',  # Link to the issue tracker
    },
    python_requires='>=3.7',  # Ensures the package runs on supported Python versions
    include_package_data=True,  # Ensures non-code files like README are included
    entry_points={
        'console_scripts': [
            'topsis=Topsis_Prerit_102217030.main:main',  # Adds CLI command to the script
        ],
    },
)


