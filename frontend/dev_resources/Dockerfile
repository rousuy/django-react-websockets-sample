FROM node:18.17.1

ARG USER_ID
ARG GROUP_ID

WORKDIR /workspace

COPY ./entrypoint.sh /opt/sbin/entrypoint.sh

RUN chmod +x /opt/sbin/entrypoint.sh

RUN chown -R $USER_ID:$GROUP_ID /workspace && chown -R $USER_ID:$GROUP_ID /opt/sbin

EXPOSE 3000

ENTRYPOINT [ "/opt/sbin/entrypoint.sh" ]

CMD [""]
