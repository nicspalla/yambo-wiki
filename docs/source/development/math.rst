========
Math rST
========

This is an equation:

.. math::
   :label: dummyeq

   a^2 + b^2 = c^2 + \sum_i (i-i)

Equations can be numbered and also referenced using the ``:label:`` option.

.. math::
   :label: euler
   
   e^{i\pi} + 1 = 0

For example, Eq :eq:`euler` is Euler's identity, Eq. :eq:`dummyeq` is a dummy equation.

.. attention::
   
   Cross-referencing equations using ``:eq:<label>`` only works within the same document.


