FROM ubuntu:14.04

MAINTAINER Michael J. Mitchell <michael@mitchtech.net>

RUN apt-get update && apt-get install -y -q \
    software-properties-common \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN add-apt-repository -y ppa:bladerf/bladerf && \
    add-apt-repository -y ppa:ettusresearch/uhd && \
    add-apt-repository -y ppa:myriadrf/drivers && \
    add-apt-repository -y ppa:myriadrf/gnuradio && \
    add-apt-repository -y ppa:gqrx/gqrx-sdr

RUN apt-get update && apt-get install -y -q \
    gqrx-sdr \
    libvolk1-bin \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN volk_profile

ENTRYPOINT ["gqrx"]

