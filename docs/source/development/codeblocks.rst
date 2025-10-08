===============
Code blocks rST
===============

Some code blocks follow...

.. code-block:: bash

   echo `date` 
   yambo -F y.in

.. code-block::

   echo `date` 
   yambo -F y.in

.. code-block:: 
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

