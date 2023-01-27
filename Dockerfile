FROM amanqs/oktaviauserbot:buster

RUN git clone -b OktaviaUserbot https://github.com/amanqs/OktaviaUserbot /home/OktaviaUserbot/ \
    && chmod 777 /home/OktaviaUserbot \
    && mkdir /home/OktaviaUserbot/bin/

WORKDIR /home/OktaviaUserbot/

CMD [ "bash", "start" ]
