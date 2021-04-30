# Jupyter Notebooks for python-sllib
This shoulb be regarded as a test/demo of what you can do with 
data in the logfiles from your Lowrance plotter/sounder.
All with the help of https://github.com/opensounder/python-sllib 
for interpreting the actual files.

You will need to have docker installed on your machine to follow the instructions.
Also make sure that you have the sample-data submodule cloned.

```shell
git submodule update --init --recursive
```


# Usage with Makefiles
```shell
make build
# now wait while the image is being built

make run
# follow the instructions that and browse to the link provided by 
# jupyter in the end
```


# Usage from PowerShell
Could be from you linux terminal as well but you will have to make some adjustments.
## Build new docker image
```powershell
docker build -t sllib-scipy-notebook -f containers/Dockerfile containers/
```
## Running
```powershell
# this works in powershell on windows, adapt to your environment
docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes `
    -v "${PWD}:/home/jovyan/work" `
    sllib-scipy-notebook
```
