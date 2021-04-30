
# Build new image
From the project root do the following.

```powershell
docker build -t sllib-scipy-notebook -f .\notebook\Dockerfile .


docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes `
    -v "${PWD}/notebook:/home/jovyan/work" `
    -v "${PWD}/tests/sample-data-lowrance:/home/jovyan/sample-data-lowrance" `
    sllib-scipy-notebook
```
