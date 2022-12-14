FROM python:3.10-bullseye

# UPDATE AND LOCALIZE
RUN apt-get update \
    && apt-get dist-upgrade -f -q -y \
    && apt-get install -f -q -y \
      locales \
      tzdata \
    && apt-get autoremove -y \
    && apt-get autoclean -y \
    && localedef -i pt_BR -c -f UTF-8 -A /usr/share/locale/locale.alias pt_BR.UTF-8
ENV LANG=pt_BR.utf8
ENV TZ=America/Sao_Paulo

# BUILD PYTHON VIRTUAL ENVIRONMENT
ENV PYTHONUNBUFFERED=TRUE
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python -m pip install -U pip setuptools wheel

# INSTALL AND BUILD
WORKDIR /usr/src/backend
COPY ./requirements_common.txt /usr/src/backend/requirements_common.txt
COPY ./requirements_docker.txt /usr/src/backend/requirements_docker.txt
RUN pip install -r requirements_docker.txt
COPY . /usr/src/backend/
