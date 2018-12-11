.PHONY: build test run

STATES ?= SP RJ
IMAGE = buscacep

build:
	docker build -t $(IMAGE) .

test:
	docker run --rm `pwd`/reports:/root/test-reports $(IMAGE) \
	python -m pytest --junitxml=test-reports/junit.xml

run: 
	docker run --rm -v `pwd`/out:/root/out $(IMAGE) \
	python buscacep.py $(STATES)