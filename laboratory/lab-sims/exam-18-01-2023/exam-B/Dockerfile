FROM ubuntu:18.04
RUN apt -y update
RUN apt -y install cowsay fortune git
RUN git clone http://github.com/teto1992/cowsay
WORKDIR /cowsay
CMD ["bash", "start.sh"]