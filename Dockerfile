FROM python:3.11-slim-buster
COPY requirements.txt /tmp/
COPY install_pkgs.sh /tmp/

ENV DEBIAN_FRONTEND noninteractive

RUN bash /tmp/install_pkgs.sh && \
    apt-get update && apt-get install -y vim python3-pip curl && \
  pip install --upgrade pip && \
  useradd --create-home appuser

COPY --chown=appuser . /home/appuser

# Guarantees umask is set properly to alleviate issue with umask not sticking inside the node container
# This is to ensure permissions of files stored on the server will be given the correct permissions

RUN chown -R appuser:appuser /run && \
    echo 'umask 002' >> /home/appuser/.profile && \
    echo 'umask 002' >> /home/appuser/.bashrc

WORKDIR /home/appuser

# Update permissions for the jpyadm user and group
COPY change_id.sh /root/change_id.sh
#RUN chmod 755 /root/change_id.sh && \
#  /root/change_id.sh -u 193 -g 199

# Copy code into the image
COPY --chown=appuser . /home/appuser

USER appuser
ENV PYTHONPATH=src

#CMD ["python", "./test.py"]
