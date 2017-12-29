# Builder for Sphinx producing Jupyter Notebook files

## TODO

1. register a builder named `ipynb` (how properly?) -- code is currently doing something
1. add itself as an extension (since version 1.6 this should be "easy": http://www.sphinx-doc.org/en/stable/extdev/index.html#discovery-of-builders-by-entry-point ???)
1. `make ipynb` should produce a lot of `.ipynb` files in the `build` subdirectory -- success!

## Usage Notes

I made this work via these essential additional in `conf.py`.
Of course, once the major TODOs are done, this should simplify and change...

```
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.expanduser('~/path/to/this/repo')))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'ipynbbuilder',                # <-- this loads the .py module. should be a proper python module!
]

mathjax_path = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-MML-AM_CHTML'

ipynb_kernel = 'sagemath'     # my No. 1 case is to convert the SageMath documentation and this is the kernel's name
```

## License

Apache 2.0

