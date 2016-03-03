FROM ubuntu:14.04

MAINTAINER Michael J. Mitchell <michael@mitchtech.net>

RUN apt-get update && apt-get install -y -q \
	android-tools* \
	ca-certificates \
	curl \
	usbutils \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["bash"]
