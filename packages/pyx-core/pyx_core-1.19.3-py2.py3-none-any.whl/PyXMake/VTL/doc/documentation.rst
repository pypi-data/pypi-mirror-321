.. Custom link to in-house GitLab repository.
:gitlab_url: https://gitlab.com/dlr-sy/pyxmake

.. toctree::
   :maxdepth: 2
   :hidden:

   pyx_core/core.rst
   pyx_poetry/plugin.rst
   pyx_webservice/api.rst
   pyxmake/contributing.rst
   pyxmake/changelog.rst
	
Harmonized interfaces and workflows to selected software development tools
==========================================================================
.. include:: ../../README.md
	:end-line: 4
	:parser: myst_parser.docutils_

.. admonition:: Summary

	`PyXMake`_ supports software development in Python by providing harmonized interfaces to selected third-party tools. 
	Strict default values are specified, which lower the entry barrier and shorten the initial training period. 
	These interfaces can be used either from the command line, via a pyproject.toml file or directly via Python scripts.
	More experienced developers can also transfer the existing class structure into their own build scripts through inheritance and modify them as required.

Installation
------------
You can install `PyXMake`_ directly with pip:

.. code-block:: console

    $ pip install pyxmake[lint]

Usage
-----
To display all available interface commands, use

.. code-block:: console

	$ pyxmake run --help
	usage: PyXMake run [-h] ...

	positional arguments:
	  namespace   An option identifier. Unknown arguments are ignored. Allowed values are: abaqus, api, pyinstaller,
				  archive, bundle, chocolatey, cmake, coverage, cxx, docker, doxygen, gfortran, gitlab, ifort, java,
				  latex, openapi, portainer, f2py, pyreq, sphinx, ssh_f2py, ssh_ifort, ssh_make

	options:
	  -h, --help  show this help message and exit

By default, all configuration settings are read directly from an enclosed pyproject.toml file and transferred to the respective background process as command line parameters.
The interfaces in the pyproject.toml file are defined as follows, e.g.:

.. include:: ../../pyproject.toml
   :start-line: 159
   :literal:

The -- operator
---------------
Each entry from a pyproject.toml file can be overwritten with the -- operator and a corresponding keyword. Additional command line parameters can also be added in this way.
For example, the following command uses a locally available version of Doxygen to create the documentation with a specified revision number. 
All other configuration settings are taken from the pyproject.toml file.

.. code-block:: console

	$ pyxmake run doxygen -- --version=1.0.0dev

Citation
--------
.. include:: ../../CITATION.cff
   :literal:

Legal notice
------------
.. include:: ../../LICENSE
   :literal:

Further readings
----------------
* `Example User Guide`_
* `Developer Reference Guide`_

..  _PyXMake: https://pypi.org/project/pyxmake
..  _Example User Guide: _static/html/index.html
..  _Developer Reference Guide: https://dlr-sy.gitlab.io/pyxmake