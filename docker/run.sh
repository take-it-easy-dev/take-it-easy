#!/bin/bash -eux

docker run -it --rm \
       	   -v /home/mate/pycharm/pycharm-community-2019.3.3:/root/pycharm \
	   -v /tmp/.X11-unix:/tmp/.X11-unix \
	   -v $HOME/.Xauthority:/root/.Xauthority \
           -e DISPLAY=$DISPLAY \
	   -v ~/.PyCharmCE2019.3:/root/.PyCharmCE2019.3 \
	   -v /home/mate/peek:/root/peek \
	   -v /home/mate/repos:/root/repos \
	   --net=host \
	   --name take-it-easy-dev-container take-it-easy-dev-env /bin/zsh
