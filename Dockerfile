FROM infopen/pyenv-tox:dev-latest

LABEL maintainer="a.chaussier@infopen.pro"

ADD --chown=pyenv-test . /srv/app/

WORKDIR /srv/app/
