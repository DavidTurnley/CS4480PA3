FROM ubuntu

RUN apt-get update
RUN apt-get -y install bash iproute2 net-tools tcpdump vim iputils-ping
RUN apt-get clean

CMD ["bash"]

RUN apt-get -y install curl
RUN apt-get -y install gnupg

RUN curl -s https://deb.frrouting.org/frr/keys.gpg | tee /usr/share/keyrings/frrouting.gpg > /dev/null

RUN apt-get install lsb-release

RUN FRRVER="frr-stable"

RUN echo deb '[signed-by=/usr/share/keyrings/frrouting.gpg]' https://deb.frrouting.org/frr $(lsb_release -s -c) $FRRVER | tee -a /etc/apt/sources.list.d/frr.list

RUN apt-get update
RUN apt-get -y install frr frr-pythontools

