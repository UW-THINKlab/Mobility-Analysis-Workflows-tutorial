## Base image https://hub.docker.com/u/rocker/
FROM rocker/r-base:latest

## copy Scripts and data
COPY install_packages.R install_packages.R
COPY myScript.R myScript.R
COPY us-500.csv us-500.csv

## install R-packages
RUN Rscript install_packages.R
