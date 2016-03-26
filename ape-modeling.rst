Modeling and fitting plan
-------------------------

authors: Christoph Deil, Daniela Huppenkothen, Axel Donath, Tom Aldcroft, (you?)

date-created: 2016 March 25

date-last-revised: 2016 March 25

type: Standard Track

status: Discussion

Abstract
--------

This document contains:

* A summary of the status of modeling and fitting packages for
  astronomers, focusing on ``astropy.modeling`` and ``Sherpa``.
* Present common modeling / fitting use cases in astronomy,
  with example code in ``astropy-model-ideas``.
* Discuss options how to go forward, i.e. what should / could happen
  to ``astropy.modeling`` and ``Sherpa``.

Given that both ``astropy.modeling`` and ``Sherpa`` exist and won't go away,
the goal is to avoid duplication of effort and improve interoperability.

TODO: add statement on scope of modeling packages? I.e. the goal is not
to create a modeling / fitting package that will be super-general and
allow very complex applications (like TODO).

Why this document?
------------------

At `PyAstro15 <http://python-in-astronomy.github.io/2015/>`__ there were many
discussions on this topic. But they weren't followed up and the status is still
similar now, a year later. In part because there was no consensus what to do,
but in part also because there was no detailed writeup, action items and
follow-up meetings.

It is an attempt to summarise the discussions at `PyAstro16
<http://python-in-astronomy.github.io/2016/>`__, and to do better this time,
i.e. come up with a good solution and make sure it gets implemented in the
coming months.

This document doesn't present a concrete and complete plan yet that needs
approval. It's not clear if we should submit this as an `Astropy APE
<https://github.com/astropy/astropy-APEs>`__.

For now, please contribute to this document and code examples to
https://github.com/astropy/astropy-model-ideas.

Glossary
--------

The terms "model" and "fitting" mean very different things to different people,
making it hard to 

This glossary establishes the meaning of the terms used in this document
and the Astropy and Sherpa docs.

* "Model" --- tbd
* "Fitting" -- tbd
* "Optimisation" -- tbd
* "Error estimation" -- tbd
* "Fit statistic" -- tbd

TODO: do we need different terminoloty for Bayesian analysis or can we largely
have the same as for likelihood fitting?

Status
------

This section summarises the status of ``astropy.modeling`` and ``Sherpa``
and also comments briefly on other projects.

astropy.modeling
++++++++++++++++

The `astropy.modeling <http://astropy.readthedocs.org/en/latest/modeling/index.html>`__
package has an advanced framework to create models.
I.e. a parameter class, a model class, a way to create composite models.

The framework to implement fit statistic functions or to fit them is primitive
and has received little attention so far.

The concept of fit statistic, optimizer and error estimator has been combined
in a "Fitter" class (although there is a proposal to separate them
in https://github.com/astropy/astropy/pull/3786).

The main use case for ``astropy.modeling`` so far was the development of
chains of world coordinate transformations.
This is reflected in the fact that WCS models are wrapped or re-implemented
as Astropy models (TODO: link to docs), and that the GWCS models are
implemented as Astropy models:
https://github.com/spacetelescope/gwcs

There are some applications where Astropy models are fitted.

* The ``astropy.modeling`` docs show some examples how to do least-square fits to 1-dim and 2-dim data.
* PSF fitting photometry is implemented in
  `photometry.psf <http://photutils.readthedocs.org/en/latest/photutils/psf.html>`__.
* TODO: link to WCS fitting example that Nadia showed.

TODO: what to say here or later what this implies?
If we still propose to deprecate `astropy.modeling.fitting`,
what is the exact proposed replacement for these applications?

Sherpa
++++++

Other packages
++++++++++++++

Other Python modeling / fitting packages exist:

* See `iminuit <https://github.com/iminuit/iminuit>`__ and 
`probfit <https://github.com/iminuit/probfit>`__.
* See `astromodels <https://github.com/giacomov/astromodels>`__
and `3ML <https://github.com/giacomov/3ML>`__.

In Python efforts are very scattered. It seems that in Julia
the modeling / fitting community and development efforts are much better structured, see
http://www.juliaopt.org/.

TODO: make comments on how those are relevant here.
Is our only goal to figure out where to put priorities and developer time in
``astropy.modeling`` and ``Sherpa``, or do we have the energy and time to try to
improve the situation in Python as a whole?

Use cases
---------

The https://github.com/astropy/astropy-model-ideas repo contains example
Python scripts and IPYthon notebooks that illustrate modeling and fitting
use cases.

* `sherpa_astropy_iminuit.ipynb <https://github.com/astropy/astropy-model-ideas/blob/master/notebooks/sherpa_astropy_iminuit/sherpa_astropy_iminuit.ipynb>`__ - Comparing model fitting with Sherpa, iminuit and Astropy
* `MCMCWithAstropyModels.ipynb <https://github.com/astropy/astropy-model-ideas/blob/master/MCMCWithAstropyModels.ipynb>`__ - MCMC with Astropy models and emcee
* `sherpa_usermodel_wrap_astropy_model.py <https://github.com/astropy/astropy-model-ideas/blob/master/sherpa_usermodel_wrap_astropy_model.py>`__ -- Example how to wrap Astropy model and fit it with Sherpa 

Whishlist
---------

astropy.modeling
++++++++++++++++

* Improve docs to explain scope and alternatives (such as Sherpa or emcee)?
* Explain how to fit Astropy models and implement likelihoods with other packages (e.g. Sherpa, emcee, iminuit)?

Sherpa
++++++

* Resolve some issues with the Sherpa API:
  * Allow creation of a user likelihood and fitting it without the
    need to create a data shim class. TODO: link to example.
  * MWL fitting, per-dataset stat. TODO: link to example.
* Sphinx docs
* Better framework for Bayesian analysis (e.g. via emcee)?
* Python 3
* Easier to install (make Fortran and conda extensions optional)
* BSD license
* Faster release cycle?

Plan
----

* Link to Sherpa from the astropy.modeling docs front page,
  pointing it out as an alternative.
* Adopt Sherpa as astropy-affiliated package to further promote it?
  (what things should happen before?)
* Gather more use cases in the ``astropy-model-ideas`` repo.
* More experiments how to interface Astropy and Sherpa (and scipy.optimise, iminuit, emcee)
* What needs to be added to Sherpa to allow all major use cases (e.g. joint likelihood fitting)
* `GSoC application <https://github.com/astropy/astropy/wiki/GSoC-2016-Application-Michele-Costa:-Bridge-sherpa-and-astropy-fitting>`__
