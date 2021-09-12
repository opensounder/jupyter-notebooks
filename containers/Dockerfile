FROM jupyter/scipy-notebook

RUN conda config --append channels conda-forge


# leaflet
RUN conda install ipyleaflet
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-leaflet

# dependencies/utilities from conda 
RUN conda install  geopandas descartes 

# install verde and dependencies
RUN conda install  verde
RUN conda install  pyproj
# RUN conda install -c conda-forge cartopy

# rasterio
RUN conda install rasterio

# tqdm
RUN pip install ipywidgets
RUN conda install -c conda-forge tqdm
RUN jupyter nbextension enable --py widgetsnbextension
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager

WORKDIR /home/jovyan/work

# requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
