FROM jupyter/scipy-notebook

# leaflet
RUN conda install -c conda-forge ipyleaflet
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-leaflet

# dependencies/utilities from conda 
RUN conda install -c conda-forge geopandas descartes 

# something is not working as it should with rasterio
# RUN conda install -c conda-forge rasterio

# install verde and dependencies
RUN conda install verde --channel conda-forge
RUN conda install -c conda-forge cartopy
RUN conda install -c conda-forge pyproj

WORKDIR /home/jovyan/work

# sllib
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt