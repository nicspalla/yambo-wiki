============
Showing code
============

The complete sphinx documentation about this topic is `here <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#showing-code-examples>`__.

To insert inline code use double backticks, ``like this``.

``code-block``
--------------

If more space is needed, use the ``code-block`` directive:

.. code-block:: none

   > wget https://media.yambo-code.eu/educational/tutorials/files/hBN.tar.gz
   [...]
   > wget https://media.yambo-code.eu/educational/tutorials/files/hBN-2D.tar.gz
   [...]
   > ls
   hBN-2D.tar.gz  hBN.tar.gz

Code can also be highlighted specifying the language, for example

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt

but this does not always work, so it's better to use ``code-block:: none`` (which does not highlight code).

One useful option is ``:emphasize-lines:``, which can be used to highlight specific lines in the code block:

.. code-block:: none
   :caption: Caption for this code block (includes a link!).
   :linenos:
   :emphasize-lines: 2,8,9,10

   [...]
   rim_cut              # [R] Coulomb potential
   gw0                  # [R] GW approximation
   el_el_corr           # [R] Electron-Electron Correlation
   HF_and_locXC         # [R] Hartree-Fock
   em1d                 # [R][X] Dynamically Screened Interaction
   NLogCPUs=0           # [PARALLEL] Live-timing CPU`s (0 for all)
   RandQpts=1000000     # [RIM] Number of random q-points in the BZ
   CUTGeo= "slab z"     # [CUT] Coulomb Cutoff geometry: box/cylinder/sphere/ws/slab X/Y/Z/XY..
   RandGvec= 5  Ry      # [RIM] Coulomb interaction RS components
   NGsBlkXm= 1  Ry      # [Xm] Response block size
   [...]

``literalinclude``
------------------

Finally, there is also the ``literalinclude`` directive that takes the code from an external file:

.. literalinclude:: example_files/example_literalinclude.txt
   :language: none
   :caption: caption
   :emphasize-lines: 4


