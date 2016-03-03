FROM mitchtech/android-sdk

MAINTAINER Michael J. Mitchell <michael@mitchtech.net>

RUN curl 'http://adakoda.github.io/android-screen-monitor/download/3.0.0/ASM_3_00.zip' > /tmp/asm.zip && \
    unzip -d /opt /tmp/asm.zip && \
    rm /tmp/asm.zip

ENTRYPOINT ["java", "-jar", "asm.jar", "$ANDROID_HOME"]
