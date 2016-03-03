FROM mitchtech/java7-oracle

MAINTAINER Michael J. Mitchell <michael@mitchtech.net>

RUN apt-get update && apt-get install -y -q \
    ant \
    curl \
    git \
#    lib32gcc1 \
#    libc6-i386 \ 
    lib32bz2-1.0 \
    lib32ncurses5 \
    lib32stdc++6 \
    lib32z1 \
    x11-apps \
    unzip \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN curl 'https://dl.google.com/dl/android/studio/ide-zips/1.5.1.0/android-studio-ide-141.2456560-linux.zip' > /tmp/studio.zip && \
    unzip -d /opt /tmp/studio.zip && \
    rm /tmp/studio.zip

# Replace 1000 with user / group id.
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

ADD 51-android.rules /etc/udev/rules.d

RUN chmod a+r /etc/udev/rules.d/51-android.rules

USER developer

ENV HOME /home/developer

ENTRYPOINT ["/opt/android-studio/bin/studio.sh"]
