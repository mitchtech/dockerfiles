FROM mitchtech/java7-oracle

MAINTAINER Michael J. Mitchell <michael@mitchtech.net>

RUN dpkg --add-architecture i386

RUN apt-get update && apt-get install -y -q \
	curl \
	expect \
	git \
	lib32gcc1 \
	lib32ncurses5 \
	lib32stdc++6 \
	lib32z1 \
	libc6-i386 \ 
	python \
	wget \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN cd /opt && \
	wget --output-document=android-sdk.tgz --quiet http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz && \
	tar xzf android-sdk.tgz && \
	rm -f android-sdk.tgz && \
	chown -R root.root android-sdk-linux

ENV ANDROID_HOME /opt/android-sdk-linux

ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools

COPY tools /opt/tools

ENV PATH ${PATH}:/opt/tools

RUN ["/opt/tools/android-accept-licenses.sh", "android update sdk --all --force --no-ui --filter platform-tools,tools,build-tools-21,build-tools-21.0.1,build-tools-21.0.2,build-tools-21.1,build-tools-21.1.1,build-tools-21.1.2,build-tools-22,build-tools-22.0.1,android-21,android-22,addon-google_apis_x86-google-21,extra-android-support,extra-android-m2repository,extra-google-m2repository,extra-google-google_play_services,sys-img-armeabi-v7a-android-21"]

RUN which adb

RUN which android

RUN echo "no" | android create avd \
                --force \
                --device "Nexus 5" \
                --name test \
                --target android-21 \
                --abi armeabi-v7a \
                --skin WVGA800 \
                --sdcard 512M

RUN mkdir -p /opt/workspace

WORKDIR /opt/workspace