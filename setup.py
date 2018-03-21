import os.path
from setuptools import setup

# Open project description text file.
#
# The first line must be the short description.
# Followed by a blank line.
# Followed by the long description.
with open(os.path.join('docs', 'project_description.txt')) as project_description_file:
    project_description_lines = project_description_file.read().strip().split("\n")
project_description = project_description_lines[0]
project_long_description = "\n".join(project_description_lines[2:])

# Read package __version__.
exec(open('pybacktrack/version.py').read())

setup(
    name='pybacktrack',
    version=__version__,
    description=project_description,
    long_description=project_long_description,
    packages=['pybacktrack', 'pybacktrack.util'],
    #
    # From the setuptools docs...
    #
    # If include_package_data set to True, this tells setuptools to automatically include any data files
    # it finds inside your package directories that are specified by your MANIFEST.in file.
    #
    # You do not need to use package_data if you are using include_package_data,
    # unless you need to add e.g. files that are generated by your setup script and build process.
    #
    include_package_data=True,
    # package_data={'pybacktrack': ['bundle_data/*']},
    install_requires=['numpy', 'scipy'],
    url='http://github.com/EarthByte/pyBacktrack',
    author='John Cannon',
    license='GPL',
    zip_safe=False)