FROM teskalabs/bspump:nightly-py38

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

RUN set -ex \
	mkdir -p /opt/bspump-blank-app

COPY ./bspumpblankapp /opt/bspump-blank-app/bspumpblankapp
COPY ./bspump-blank-app.py /opt/bspump-blank-app/bspump-blank-app.py


WORKDIR /opt/bspump-blank-app
CMD ["python3", "/opt/bspump-blank-app/bspump-blank-app.py", "-w"]
