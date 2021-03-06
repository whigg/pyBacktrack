.. _pybacktrack_getting_started:

Getting Started
===============

.. contents::
   :local:
   :depth: 4


.. _pybacktrack_installation:

Installation
++++++++++++

You can install ``pybacktrack`` either:

#. using :ref:`pip <pybacktrack_install_using_pip>`, or
#. using :ref:`Docker <pybacktrack_install_using_docker>`.

Docker is typically more straightforward since all the dependencies of ``pybacktrack`` have been pre-installed.

.. _pybacktrack_install_using_pip:

Install using pip
-----------------

Python packages installed using `pip <https://pypi.org/project/pip/>`_ will typically also have their dependency packages automatically installed also.
However ``pybacktrack`` requires manual installation of some of its dependencies.

.. contents::
   :local:
   :depth: 2

.. _pybacktrack_requirements:

Requirements
^^^^^^^^^^^^

PyBacktrack depends on:

- `NumPy <http://www.numpy.org/>`_
- `SciPy <https://www.scipy.org/>`_
- `Generic Mapping Tools (GMT) <http://gmt.soest.hawaii.edu/>`_ (>=5.0.0)
- `PyGPlates <http://www.gplates.org/>`_

`NumPy` and `SciPy` are automatically installed by `pip` when :ref:`pybacktrack is installed <pybacktrack_install_pybacktrack>`, however `GMT` (version 5 or above) and `pyGPlates` need to be manually installed.

`GMT` is called via the command-line (shell) and so just needs to be in the PATH in order for `pyBacktrack` to find it.
Also ensure that version 5 or above (supports NetCDF version 4) is installed since the :ref:`bundled grid files in pyBacktrack<pybacktrack_reference_bundle_data>` are in NetCDF4 format.

`PyGPlates` is not currently installable as a package and so needs to be in the python path (sys.path or PYTHONPATH).
Installation instructions are available `here <http://www.gplates.org/docs/pygplates/index.html>`_.

Also, pyGPlates currently requires Python 2.7 (future releases will support Python 3).
So unfortunately you will need a Python 2.7 installation. If you have an existing Python 3 installation then the
:ref:`Macports install example <pybacktrack_install_requirements_mac>` below shows one approach to selecting the default Python (using ``sudo port select``).
Another approach is using Python virtual environments where each environment has its own ``python``, ``pip`` and installed packages.
However, currently pyGPlates does not yet work in virtual environments (at least on Mac systems).

.. _pybacktrack_install_requirements_ubuntu:

Install Python 2.7, pip, GMT and pyGPlates on Ubuntu
****************************************************

This is an example demonstrating how to install GMT and pyGPlates on Ubuntu 16.04 (Xenial).

.. note:: The main difference for other Ubuntu versions will be the pyGPlates install package
          (you'll need to select the package appropriate for your Ubuntu version).

First install Python 2.7 and Pip:
::

  sudo apt-get update
  
  sudo apt-get install python python-pip
  sudo pip install --upgrade pip

Then install GMT 5:
::

  sudo apt-get install gmt

Then download the pyGPlates debian package `pygplates-ubuntu-xenial_2.1_1_amd64.deb <https://sourceforge.net/projects/gplates/files/pygplates/beta-revision-18/>`_,
and install it:
::

  sudo apt-get install pygplates-ubuntu-xenial_2.1_1_amd64.deb

Then add the installed location of pyGPlates to the PYTHONPATH environment variable:
::

  export PYTHONPATH=$PYTHONPATH:/usr/lib/pygplates/revision18

Or, alternatively, copy pyGPlates to the Python system install directory:
::

  cp /usr/lib/pygplates/revision18/pygplates.so /usr/lib/python2.7/dist-packages/

.. _pybacktrack_install_requirements_mac:

Install Python 2.7, pip, GMT and pyGPlates on Mac using Macports
****************************************************************

This is an example demonstrating how to install GMT and pyGPlates on a Mac system using `Macports <https://www.macports.org/>`_.

First install Python 2.7 and Pip:
::

  sudo port install python27
  sudo port install py27-pip

Set your default ``python`` to Python 2.7:
::

  sudo port select --set python python27
  sudo port select --set pip pip27

.. note:: If you already have ``python`` referencing Python 3 then you can instead use ``python2`` to reference Python 2.7:
          ::
          
            sudo port select --set python2 python27
            sudo port select --set pip2 pip27
          
          ...but this will require using ``python2`` on the command-line to run
          :ref:`pybacktrack <pybacktrack_use_a_builtin_module_script>` (instead of just ``python``).

Then install GMT 5:
::

  sudo port install gmt5

Then download the pyGPlates Mac zip file `pygplates_rev18_python27_MacOS64.zip <https://sourceforge.net/projects/gplates/files/pygplates/beta-revision-18/>`_,
and extract it to your home directory.

Then add the unzipped location of pyGPlates to the PYTHONPATH environment variable:
::

  export PYTHONPATH=~/pygplates_rev18_python27_MacOS64:$PYTHONPATH

.. note:: The above line can be added to your ``~/.bashrc`` or ``~/.profile`` file so that
          PYTHONPATH is set each time you open a new terminal window.

.. _pybacktrack_install_pybacktrack:

Install pybacktrack
^^^^^^^^^^^^^^^^^^^

To install the latest stable version, run:
::

  pip install pybacktrack

.. note:: If you are using a package manager such as `Conda <https://docs.conda.io>`_ you may need to run ``python -m pip install pybacktrack`` to ensure
          ``pybacktrack`` is installed into Conda Python and not the system Python (assuming ``python`` will execute the Conda Python interpreter). 
          It is only necessary if, for example, ``python`` executes the Conda Python interpreter but ``pip`` installs into the system Python
          (because the base Conda environment is not activated).

.. warning:: | On Mac systems, when using `Macports <https://www.macports.org/>`_, it might be better to install to the
               local user install directory with ``pip install --user pybacktrack`` to avoid confusing Macports
               (which installs to the system install directory).
             | And on linux systems, if you have admin privileges, you can install to the system install directory with ``sudo pip install pybacktrack``.

If you already have ``pybacktrack`` installed and would like to upgrade to the latest version then use the ``--upgrade`` flag:
::

  pip install --upgrade pybacktrack

Installing `pyBacktrack` will automatically install the `NumPy` and `SciPy` :ref:`requirements <pybacktrack_requirements>`.
However, as mentioned in :ref:`requirements <pybacktrack_requirements>`, `GMT` and `pyGPlates` still need to be manually installed.

To install the latest development version (requires Git on local system), run:
::

  pip install "git+https://github.com/EarthByte/pyBacktrack.git#egg=pybacktrack"

.. note:: | You may need to update your `Git` if you receive an error ending with ``tlsv1 alert protocol version``.
          | This is apparently due to an `update on GitHub <https://blog.github.com/2018-02-23-weak-cryptographic-standards-removed>`_.

...or download the `pyBacktrack source code <https://github.com/EarthByte/pyBacktrack>`_, extract to a local directory and run:
::

  pip install <path-to-local-directory>

.. _pybacktrack_install_examples:

Install the examples
^^^^^^^^^^^^^^^^^^^^

Before running the example below, or any :ref:`other examples <pygplates_overview>`, you'll also need to install the example data (from the pybacktrack package itself).
This assumes you've already :ref:`installed the pybacktrack package <pybacktrack_install_pybacktrack>`.

The following command installs the examples (example data and notebooks) to a new sub-directory of your *current working directory* called ``pybacktrack_examples``:

.. code-block:: python

    python -c "import pybacktrack; pybacktrack.install_examples()"

.. note:: The *current working directory* is whatever directory you are in when you run the above command.

.. note:: | Alternatively you can choose a different sub-directory by providing an argument to the ``install_examples()`` function above.
          | For example, ``python -c "import pybacktrack; pybacktrack.install_examples('pybacktrack/examples')"``
            creates a new sub-directory of your *current working directory* called ``pybacktrack/examples``.
          | However the example below assumes the default directory (``pybacktrack_examples``).

.. _pybacktrack_install_using_docker:

Install using Docker
--------------------

This method of running ``pybacktrack`` relies on `Docker <https://www.docker.com/>`_, so before installing
the ``pybacktrack`` docker image, ensure you have installed `Docker <https://www.docker.com/>`_.

.. note:: | On Windows platforms you can install `Docker Toolbox <https://docs.docker.com/toolbox/overview/>`_ or
            `Docker Desktop for Windows <https://docs.docker.com/docker-for-windows/install/>`_.
          | *Docker Desktop for Windows* offers the most "native" experience and is recommended by Docker, but has
            higher system requirements and once it's installed you can no longer use VirtualBox (to run other Virtual Machines).
          | In contrast, *Docker Toolbox* relies on VirtualBox, so if your system can run VirtualBox then
            *Docker Toolbox* should work on your system.
          | A similar situation applies on Mac platforms where you can install
            `Docker Toolbox <https://docs.docker.com/toolbox/overview/>`_ or
            `Docker Desktop for Mac <https://docs.docker.com/docker-for-mac/install/>`_.

Once Docker is installed, open a Docker terminal (command-line interface).

.. note:: | For *Docker Toolbox* this is the *Docker Quickstart Terminal*.
          | For `Docker Desktop for Windows <https://docs.docker.com/docker-for-windows/install/>`_ and
            `Docker Desktop for Mac <https://docs.docker.com/docker-for-mac/install/>`_ this a regular command-line terminal.
          | On Linux systems this a regular command-line terminal.

To install the ``pybacktrack`` docker image, type:

.. code-block:: none

    docker pull earthbyte/pybacktrack

To run the docker image:

.. code-block:: none

    docker run -it --rm -p 18888:8888 -w /usr/src/pybacktrack earthbyte/pybacktrack

| This should bring up a command prompt inside the running docker container.
| The current working directory should be ``/usr/src/pybacktrack/``.
| It should have a ``pybacktrack_examples`` sub-directory containing test data.

.. note:: On Linux systems you may have to use `sudo` when running `docker` commands. For example:
          ::
          
            sudo docker pull earthbyte/pybacktrack
            sudo docker run -it --rm -p 18888:8888 -w /usr/src/pybacktrack earthbyte/pybacktrack

From the current working directory you can run the :ref:`backtracking example <pybacktrack_a_backtracking_example>` below,
or any :ref:`other examples <pygplates_overview>` in this documentation. For example, you could run:

.. code-block:: python

    python -m pybacktrack.backtrack -w pybacktrack_examples/test_data/ODP-114-699-Lithology.txt -d age water_depth -- ODP-114-699_backtrack_decompat.txt

If you wish to run the `example notebooks <https://github.com/EarthByte/pyBacktrack/tree/master/pybacktrack/notebooks>`_
then there is a ``notebook.sh`` script to start a Jupyter notebook server in the running docker container:

.. code-block:: none

    ./notebook.sh

Then you can start a web browser on your local machine and type the following in the URL field:

.. code-block:: none

    http://localhost:18888/tree

| This will display the current working directory in the docker container.
| In the web browser, navigate to ``pybacktrack_examples`` and then ``notebooks``.
| Then click on a notebook (such as `backtrack.ipynb <https://github.com/EarthByte/pyBacktrack/blob/master/pybacktrack/notebooks/backtrack.ipynb>`_).
| You should be able to run the notebook, or modify it and then run it.

.. note:: | If you are running *Docker Toolbox on Windows* then use the Docker Machine IP instead of ``localhost``.
          | For example ``http://192.168.99.100:18888/tree``.
          | To find the IP address use the command ``docker-machine ip``.

.. _pybacktrack_a_backtracking_example:

A Backtracking Example
++++++++++++++++++++++

Once :ref:`installed <pybacktrack_installation>`, ``pybacktrack`` is available to:

#. run built-in scripts (inside ``pybacktrack``), or
#. ``import pybacktrack`` into your own script.

The following example is used to demonstrate both approaches. It backtracks an ocean drill site and saves the output to a text file by:

- reading the ocean drill site file ``pybacktrack_examples/test_data/ODP-114-699-Lithology.txt``,

  .. note:: | This file is part of the :ref:`example data <pybacktrack_install_examples>`.
            | However if you have your own ocean drill site file then you can substitute it in the example below if you want.

- backtracking it using:

  * the ``M2`` dynamic topography model, and
  * the ``Haq87_SealevelCurve_Longterm`` sea-level model,

- writing the amended drill site to ``ODP-114-699_backtrack_amended.txt``, and
- writing the following columns to ``ODP-114-699_backtrack_decompat.txt``:

  * age
  * compacted_depth
  * compacted_thickness
  * decompacted_thickness
  * decompacted_density
  * water_depth
  * tectonic_subsidence
  * lithology

.. _pybacktrack_use_a_builtin_module_script:

Use a built-in module script
----------------------------

Since there is a ``backtrack`` module inside ``pybacktrack`` that can be run as a script,
we can invoke it on the command-line using ``python -m pybacktrack.backtrack`` followed by command line options that are specific to that module.
This is the easiest way to run backtracking.

To see its command-line options, run:

.. code-block:: python

    python -m pybacktrack.backtrack --help

The backtracking example can now be demonstrated by running the script as:

.. code-block:: python

    python -m pybacktrack.backtrack \
        -w pybacktrack_examples/test_data/ODP-114-699-Lithology.txt \
        -d age compacted_depth compacted_thickness decompacted_thickness decompacted_density water_depth tectonic_subsidence lithology \
        -ym M2 \
        -slm Haq87_SealevelCurve_Longterm \
        -o ODP-114-699_backtrack_amended.txt \
        -- \
        ODP-114-699_backtrack_decompat.txt

.. _pybacktrack_import_into_your_own_script:

Import into your own script
---------------------------

An alternative to running a built-in script is to write your own script (using a text editor) that imports ``pybacktrack`` and
calls its functions. You might do this if you want to combine pyBacktrack functionality with other research functionality into a single script.

The following Python code does the same as the :ref:`built-in script<pybacktrack_use_a_builtin_module_script>` by calling the
:func:`pybacktrack.backtrack_and_write_well` function:

.. code-block:: python

    import pybacktrack
    
    # Input and output filenames.
    input_well_filename = 'pybacktrack_examples/test_data/ODP-114-699-Lithology.txt'
    amended_well_output_filename = 'ODP-114-699_backtrack_amended.txt'
    decompacted_output_filename = 'ODP-114-699_backtrack_decompat.txt'
    
    # Read input well file, and write amended well and decompacted results to output files.
    pybacktrack.backtrack_and_write_well(
        decompacted_output_filename,
        input_well_filename,
        dynamic_topography_model='M2',
        sea_level_model='Haq87_SealevelCurve_Longterm',
        # The columns in decompacted output file...
        decompacted_columns=[pybacktrack.BACKTRACK_COLUMN_AGE,
                             pybacktrack.BACKTRACK_COLUMN_COMPACTED_DEPTH,
                             pybacktrack.BACKTRACK_COLUMN_COMPACTED_THICKNESS,
                             pybacktrack.BACKTRACK_COLUMN_DECOMPACTED_THICKNESS,
                             pybacktrack.BACKTRACK_COLUMN_DECOMPACTED_DENSITY,
                             pybacktrack.BACKTRACK_COLUMN_WATER_DEPTH,
                             pybacktrack.BACKTRACK_COLUMN_TECTONIC_SUBSIDENCE,
                             pybacktrack.BACKTRACK_COLUMN_LITHOLOGY],
        # Might be an extra stratigraphic well layer added from well bottom to ocean basement...
        ammended_well_output_filename=amended_well_output_filename)

If you save the above code to a file called ``my_backtrack_script.py`` then you can run it as:

.. code-block:: python

    python my_backtrack_script.py
