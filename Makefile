# -*- mode: makefile-gmake; coding: utf-8 -*-

DESTDIR ?= ~

all:

download:
	pip3 download elasticsearch2
	unzip elasticsearch2-*-py2.py3-none-any.whl
	$(RM) -r *.dist-info *.whl

install: clean download
	python3 setup.py install \
	    --prefix=$(DESTDIR)/usr/ \
	    --no-compile \
	    --install-layout=deb

package:
	ian build -c

.PHONY: clean
clean:
	$(RM) -r *.dist-info *.whl
	$(RM) -r elasticsearch elasticsearch2
	$(RM) -r build
