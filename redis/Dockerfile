FROM redis:7.0-bullseye

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
