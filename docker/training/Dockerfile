FROM ubuntu:19.10
RUN apt-get update && apt-get install -y python3-dev\
      x11-apps \
      && rm -rf /usr/share/doc/* && \
      rm -rf /usr/share/info/* && \
      rm -rf /tmp/* && \
      rm -rf /var/tmp/*
RUN apt-get update && apt-get install -y libxtst6 libxi-dev
RUN apt-get update && apt-get install -y git vim ruby-dev default-libmysqlclient-dev zsh less mc
RUN apt-get update && apt-get install -y wget
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -qq install python3-tk
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true
RUN sed -i 's/robbyrussell/junkfood/g' /root/.zshrc
RUN echo "alias pycharm=\"/root/pycharm/bin/pycharm.sh\"" >> /root/.zshrc
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install numpy matplotlib pylint black 
RUN pip3 install torch torchvision
#RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
#RUN apt-get -y install python3-tk
RUN pip3 install jupyterlab seaborn scipy scikit-learn
RUN pip3 install pytest
RUN pip3 install mypy
RUN apt-get update && apt-get install -y silversearcher-ag libopencv-dev
RUN pip3 install opencv-python
ENV PYTHONPATH /root/take_it_easy/src
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
