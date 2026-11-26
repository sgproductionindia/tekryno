.PHONY: help install build verify test clean

PYTHON ?= python3
RELEASE_TTF := fonts/ttf/Tekryno-Regular.ttf
BUILT_TTF := build/Tekryno-Regular.ttf

help:
	@echo 'Tekryno font project'
	@echo '  make install  Install pinned Python build requirements'
	@echo '  make build    Build editable UFO as TrueType in build/'
	@echo '  make verify   Assert exact byte-for-byte match with approved release TTF'
	@echo '  make test     Alias for verify'
	@echo '  make clean    Remove local development builds'

install:
	$(PYTHON) -m pip install -r requirements.txt

build:
	$(PYTHON) sources/build_from_ufo.py

verify: build
	$(PYTHON) -c "from pathlib import Path; from fontTools.ttLib import TTFont; import hashlib; a=Path('$(RELEASE_TTF)').read_bytes(); b=Path('$(BUILT_TTF)').read_bytes(); assert a==b, 'The UFO rebuild differs from the approved TTF'; f=TTFont('$(BUILT_TTF)'); assert len(f.getGlyphOrder())==218; assert len(f.getBestCmap())==327; print('PASS: exact-source TTF SHA256',hashlib.sha256(b).hexdigest())"

test: verify

clean:
	rm -rf build/
