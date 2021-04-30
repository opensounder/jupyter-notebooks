
REPO?=
IMAGE=sllib-scipy-notebook
TAGNAME=$(REPO)$(IMAGE)

.PHONY: run
run:
	docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes \
		-v "$(CURDIR):/home/jovyan/work" \
		--name $(IMAGE) \
		$(TAGNAME)


.PHONY: build
build:
	docker build -t $(TAGNAME) -f containers/Dockerfile containers/

.PHONY: kill
kill:
	docker kill $(IMAGE)