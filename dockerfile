FROM bash:latest

RUN apk update && apk add fortune cowsay netcat-openbsd

COPY wisecow.sh /wisecow.sh
RUN chmod +x /wisecow.sh

EXPOSE 4499

CMD ["/wisecow.sh"]

