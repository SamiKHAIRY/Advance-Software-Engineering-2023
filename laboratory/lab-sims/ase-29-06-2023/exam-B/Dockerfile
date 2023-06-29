FROM alpine:latest
RUN apk update
RUN apk add figlet git
RUN git clone https://github.com/glpaparelli/ase-29-06.git
WORKDIR /ase-29-06
CMD ["sh", "script.sh"]
