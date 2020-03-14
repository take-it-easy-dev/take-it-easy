FROM ubuntu:19.10
FROM pytorch/pytorch:latest
RUN apt-get update && apt-get install -y python3-dev\
      x11-apps \
      && rm -rf /usr/share/doc/* && \
      rm -rf /usr/share/info/* && \
      rm -rf /tmp/* && \
      rm -rf /var/tmp/*
RUN apt-get update && apt-get install -y libxtst6 libxi-dev
RUN apt-get update && apt-get install -y git vim ruby-dev default-libmysqlclient-dev zsh less mc
RUN apt-get update && apt-get install -y wget
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true
RUN sed -i 's/robbyrussell/junkfood/g' /root/.zshrc
RUN echo "alias pycharm=\"/root/pycharm/bin/pycharm.sh\"" >> /root/.zshrc
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install numpy matplotlib pylint black
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8