FROM python:3.7.1-slim

ADD src/cep/buscaCep.py /root/buscaCep.py 
ADD requirements.txt /root/requirements.txt

RUN pip install -r /root/requirements.txt

WORKDIR /root

CMD ["python", "buscaCep.py"]