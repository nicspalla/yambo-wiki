==========
Contribute
==========

In order to contribute to this wiki (for example adding tutorials, fixing typos etc.) you need to be a contributor of the GitHub repository.

The html files are updated whenever there is a push on the main branch: this triggers the automated ``sphinx`` workflow on GitHub that builds the static webpage.

Setup ``sphinx`` locally
========================

Since the automated GitHub workflow takes some time to finish (a couple of minutes from the push) you may want to install ``sphinx`` on your local machine to test your updates before committing and pushing. 

.. attention::

   In order to have the same output on GitHub, make sure that all additional software needed for the build is also loaded by the workflow, i.e. make sure that every additional software you used is also listed in the ``docs/requirements.txt`` file.

I suggest creating a virtual enviroment with the installation of ``sphinx`` and all requirements after cloning the ``yambo-wiki`` repository:

.. code-block:: none

   > python -m venv <somewhere>/sphinx-wiki
   [...]
   > source <somewhere>/sphinx-wiki/bin/activate
   (sphinx-wiki) > pip install <requirements.txt>

.. attention::

   Use the same version of ``python`` as in ``yambo-wiki/.github/workflows/sphinx.yml``. Check also that the version of ``sphinx`` installed by ``pip`` is the same one used in the automated workflow.

To produce the ``html`` files, activate the ``sphinx-wiki`` environment and run the following command from inside the ``yambo-wiki`` folder:

.. code-block:: none
   :emphasize-lines: 5

   > source <somewhere>/sphinx-wiki/bin/activate
   (sphinx-wiki) > cd <somewhere-else>/yambo-wiki
   (sphinx-wiki) > ls
   docs  README.md
   (sphinx-wiki) > sphinx-build -b html docs/source/ ~/Desktop/build

.. attention::

   Redirect the output ``build`` folder (i.e. the one with ``html`` files) **outside** the ``yambo-wiki`` folder (for example to ``~/Desktop``).


