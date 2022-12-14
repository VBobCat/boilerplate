FROM node:18-bullseye

# UPDATE AND LOCALIZE
RUN apt-get update \
    && apt-get dist-upgrade -f -q -y \
    && apt-get install \
      locales \
      tzdata \
    -f -q -y \
    && apt-get autoremove -y \
    && apt-get autoclean -y \
    && localedef -i pt_BR -c -f UTF-8 -A /usr/share/locale/locale.alias pt_BR.UTF-8
ENV LANG=pt_BR.utf8
ENV TZ=America/Sao_Paulo

# INSTALL AND BUILD
WORKDIR /usr/src/frontend
COPY . /usr/src/frontend/
RUN npm install
RUN npm run build
