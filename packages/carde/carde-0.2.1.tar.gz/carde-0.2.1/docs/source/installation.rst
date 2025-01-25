.. _installation:

Installation
************


Windows
=======

1. Install the latest version of `miniforge <https://github.com/conda-forge/miniforge>`_
2. Open the Miniforge Prompt
3. Create a new conda environment with the following command:

.. code-block:: bash

   conda create -n carde-env python=3.12

4. Activate the environment with the following command:

.. code-block:: bash

   conda activate carde-env

.. code-block:: bash

   python3 -m pip install carde


Linux
=====

1. create a virtual environment with the following command (in a terminal):

.. code-block:: bash

   python3 -m venv carde-env

2. Activate the environment with the following command:

.. code-block:: bash

   source carde-env/bin/activate

3. Install the package with the following command:

.. code-block:: bash

   python3 -m pip install carde
