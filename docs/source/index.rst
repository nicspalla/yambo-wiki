.. toctree::
   :hidden:
   :caption: Schools

   index_schools_modena2025.rst



YAMBO documentation
===================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.

.. note::

   This is a note block.

.. warning::
   
   This is a warning block.

.. seealso::

   This is a seealso block.

.. hint::

   This is a hint block.

.. admonition:: Example

   This is an admonition block named example.

.. code-block:: bash

   echo `date` 
   yambo -F y.in

.. code-block:: console

   echo `date` 
   yambo -F y.in

This is an equation:

.. math::

   a^2 + b^2 = c^2 + \sum_i (i-i)

Normal text looks like this.

Footnote references, like [#]_. Note that footnotes may get rearranged [#]_, e.g., to the bottom of the "page".

.. [#] A numerical footnote. Note there's no colon after the ``]``.

.. [#] Not sure when this happens.

Input file variables
====================

This will eventually contain the description of yambo input file variables.

:blue:`A` :red:`typical` :ypurple:`YAMBO` :ypink:`input` :ypeach:`file` :yred:`looks` :yyellow:`like` :ygray:`this`:

.. code-block:: console
   :emphasize-lines: 2,7

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

Note that each comment begins with a *marker*, for example ``[R]``, ``[RIM]``, ``[CUT]`` and so on. These *markers*, identify different classes of variables that refer to specific sections of either the calculation or the code itself.
In the following, all the variables are grouped according to their reference *marker(s)*.
You may also notice that for some variables it is possible to specify the units...
