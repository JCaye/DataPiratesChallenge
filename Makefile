.PHONY: run

STATES ?= SP RJ
IMAGE = buscacep

run: 
	docker run -v C:/users/juliocaye/desafioneoway/datapirateschallenge/out:/root/out $(IMAGE)