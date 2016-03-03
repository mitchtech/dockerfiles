FROM ubuntu:14.04

MAINTAINER Michael J. Mitchell <michael@mitchtech.net>

RUN apt-get update && apt-get install -y -q \
    software-properties-common \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN add-apt-repository -y ppa:webupd8team/java

RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections

RUN apt-get update && apt-get install -y -q \
    oracle-java7-installer \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*
