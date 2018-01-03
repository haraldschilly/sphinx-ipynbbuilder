.. test documentation master file, created by
   sphinx-quickstart on Wed Jan  3 16:44:33 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to test's documentation!
================================

Contents:

.. toctree::
   :maxdepth: 2


Code
====

Code is **fun**!

Model persistence
-----------------

It is possible to save a model in scikit-learn by using Python's built-in
persistence model, namely `pickle <https://docs.python.org/2/library/pickle.html>`_::

  >>> from sklearn import svm
  >>> from sklearn import datasets
  >>> clf = svm.SVC()
  >>> iris = datasets.load_iris()
  >>> X, y = iris.data, iris.target
  >>> clf.fit(X, y)  # doctest: +NORMALIZE_WHITESPACE
  SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

  >>> import pickle
  >>> s = pickle.dumps(clf)
  >>> clf2 = pickle.loads(s)
  >>> clf2.predict(X[0:1])
  array([0])
  >>> y[0]
  0

In the specific case of scikit-learn, it may be more interesting to use
joblib's replacement of pickle (``joblib.dump`` & ``joblib.load``),
which is more efficient on big data, but can only pickle to the disk
and not to a string::

  >>> from sklearn.externals import joblib
  >>> joblib.dump(clf, 'filename.pkl') # doctest: +SKIP

Later you can load back the pickled model (possibly in another Python process)
with::

  >>> clf = joblib.load('filename.pkl') # doctest:+SKIP

test::

  >>> print(1)
  1
  >>> print('asdfsadf'
  ...    'asdfsadf'
  ... )
  2


Type casting
~~~~~~~~~~~~

Unless otherwise specified, input will be cast to ``float64``::

  >>> import numpy as np
  >>> from sklearn import random_projection

  >>> rng = np.random.RandomState(0)
  >>> X = rng.rand(10, 2000)
  >>> X = np.array(X, dtype='float32')
  >>> X.dtype
  dtype('float32')

  >>> transformer = random_projection.GaussianRandomProjection()
  >>> X_new = transformer.fit_transform(X)
  >>> X_new.dtype
  dtype('float64')


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

