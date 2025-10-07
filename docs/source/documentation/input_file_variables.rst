.. To use colors, include this file
.. include:: /_static/special.rst

.. toctree:
   :hidden:
   :glob:

   *

.. _pagetop input file variables:

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

.. admonition:: :ref:`Runlevels <sec runlevels>`

   *Marker(s)*: ``[R]``

   These variables are used by the driver to determine what needs to be computed...
   A set of variables is connected to each runlevel.
   Runlevel variables are marked by ``[R]``

   :ref:`rim_cut <var rim_cut>`
   :ref:`em1d <var em1d>`
   :ref:`gw0 <var gw0>`
   :ref:`el_el_corr <var el_el_corr>`


.. admonition:: :ref:`RIM and Coulomb cutoff <sec rim and coulomb cutoff>`

   *Marker(s)*: ``[RIM]``, ``[CUT]``

   These variables control the random integration method and the cutoff 
   geometry of the Coulomb interaction...

   :ref:`RandQpts <var RandQpts>`
   :ref:`CUTGeo <var CUTGeo>`

|



----



.. _sec runlevels:

Runlevels
---------



|

.. _var rim_cut:

**rim_cut**:
 
 | Description...
 | aligned line break
 | looong line looong line looong line looong line looong line looong line looong line looong line looong line looong line looong line
 |
 | :ref:`> top <pagetop input file variables>`



|

.. _var em1d:

**em1d**:

 | Description...
 | aligned line break
 | looong line looong line looong line looong line looong line looong line looong line looong line looong line looong line looong line
 |
 | :ref:`> top <pagetop input file variables>`



|

.. _var gw0:

**gw0**:

 | Description...
 | aligned line break
 | looong line looong line looong line looong line looong line looong line looong line looong line looong line looong line looong line
 |
 | :ref:`> top <pagetop input file variables>`



|

.. _var el_el_corr:

**el_el_corr**:

 | Description...
 | aligned line break
 | looong line looong line looong line looong line looong line looong line looong line looong line looong line looong line looong line
 |
 | :ref:`> top <pagetop input file variables>`



|

----



.. _sec rim and coulomb cutoff:

RIM and Coulomb cutoff
----------------------



|

.. _var RandQpts:

**RandQpts**:

 | *Type*: INTEGER
 | *Units*: RL
 | *Default*: 100..?
 |
 | Number of random q-points in the BZ to perform Monte Carlo Integration. Values like 10^6 can be used to ensure convergence. Needed for non 3D system to avoid divergences for small q, and needed to build cutoff potential with box shape.
 |
 | :ref:`> top <pagetop input file variables>`



|

.. _var CUTGeo:

**CUTGeo**:

 | *Type*: STRING
 | *Units*: None
 | *Default*: None
 |
 | Cutoff geometry. Allowed values are...
 |
 | :ref:`> top <pagetop input file variables>`


