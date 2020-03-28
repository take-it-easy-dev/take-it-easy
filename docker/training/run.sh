#!/bin/bash -eux

docker run -it --rm \
		-v /home/mate/pycharm/pycharm-community-2019.3.3:/root/pycharm \
		-v ~/.PyCharmCE2019.3:/root/.PyCharmCE2019.3 \
		-v /home/mate/hp/take_it_easy:/root/take_it_easy \
	       	-v /tmp/.X11-unix:/tmp/.X11-unix \
	   	-v $HOME/.Xauthority:/root/.Xauthority \
		-v /home/mate/peek:/root/peek \
	        -v /home/mate/repos:/root/repos \
       	        -e DISPLAY=$DISPLAY \
	   	--net=host \
	   	-w /root/take_it_easy \
	   	--name take-it-easy-dev-container take-it-easy-dev-env /bin/zsh
