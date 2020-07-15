## Base image https://hub.docker.com/u/rocker/
FROM rocker/r-base:latest

## install R-packages
RUN Rscript install_packages.R

## copy Scripts and data
COPY myScript.R myScript.R
COPY us-500.csv us-500.csv