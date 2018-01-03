#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import glob
import inspect
from os import path

from six import iteritems
from six.moves import cPickle as pickle

import sphinx
from sphinx.builders import Builder
#from sphinx.util import logging
from sphinx.util.inspect import safe_getattr

import codecs
from os import path

from docutils.io import StringOutput

from sphinx.builders import Builder
from sphinx.util.osutil import ensuredir, os_path

from ipynbwriter import IpynbWriter


class IpynbBuilder(Builder):
    name = 'ipynb'
    format = 'ipynb'
    out_suffix = '.ipynb'
    allow_parallel = True

    def init(self):
        pass

    def get_outdated_docs(self):
        for docname in self.env.found_docs:
            if docname not in self.env.all_docs:
                yield docname
                continue
            targetname = self.env.doc2path(docname, self.outdir,
                                           self.out_suffix)
            try:
                targetmtime = path.getmtime(targetname)
            except Exception:
                targetmtime = 0
            try:
                srcmtime = path.getmtime(self.env.doc2path(docname))
                if srcmtime > targetmtime:
                    yield docname
            except EnvironmentError:
                # source doesn't exist anymore
                pass

    def get_target_uri(self, docname, typ=None):
        return ''

    def prepare_writing(self, docnames):
        self.writer = IpynbWriter(self, self.config.ipynb_kernel)

    def write_doc(self, docname, doctree):
        self.current_docname = docname
        destination = StringOutput(encoding='utf-8')
        self.writer.write(doctree, destination)
        outfilename = path.join(self.outdir, os_path(docname) + self.out_suffix)
        ensuredir(path.dirname(outfilename))
        try:
            f = codecs.open(outfilename, 'w', 'utf-8')
            try:
                f.write(self.writer.output)
            finally:
                f.close()
        except (IOError, OSError) as err:
            self.warn("error writing file %s: %s" % (outfilename, err))

    def finish(self):
        pass


def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    app.add_builder(IpynbBuilder)
    app.add_config_value('ipynb_kernel', 'python', False)
    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}

