DATE = $(shell date +'%Y-%m-%d')
VIRTUAL_ENV ?= env

ifeq ($(shell uname -s), Linux)
	HOSTNAME := localhost
else
	HOSTNAME := host.docker.internal
endif

.PHONY: benchmark
benchmark:
	@make aiohttp
	@make baize
	@make blacksheep
	@make django
	@make fastapi
	@make starlette
	@make tornado
	@make django_sync
	@make flask_sync

# Run benchmark
%:
	@echo "\nBenchmarking $@\n--------------------"
	@sudo docker build -f $(CURDIR)/frameworks/Dockerfile -t benchmarks:$@ $(CURDIR)/frameworks/$@
	@sudo docker run --rm -d --publish 8080:8080 --name $@-benchmark benchmarks:$@
	sleep 2
	@echo "\nRun HTML [$@]\n"
	@docker run --rm --network host \
	       -e FRAMEWORK=$@ -e FILENAME=/results/html.csv \
	       -v $(CURDIR)/results:/results \
	       -v $(CURDIR)/wrk:/scripts \
	       williamyeh/wrk http://${HOSTNAME}:8080/html -d15s -t4 -c64 -s /scripts/html.lua
	@echo "\nRun UPLOAD [$@]\n"
	@docker run --rm --network host \
	       -e FRAMEWORK=$@ -e FILENAME=/results/upload.csv \
	       -v $(CURDIR)/results:/results \
	       -v $(CURDIR)/wrk:/scripts \
	       williamyeh/wrk http://${HOSTNAME}:8080/upload -d15s -t4 -c64 -s /scripts/upload.lua
	@echo "\nRun API [$@]\n"
	@docker run --rm --network host \
	       -e FRAMEWORK=$@ -e FILENAME=/results/api.csv \
	       -v $(CURDIR)/results:/results \
	       -v $(CURDIR)/wrk:/scripts \
	       williamyeh/wrk http://${HOSTNAME}:8080/api/users/1/records/1?query=test -d15s -t4 -c64 -s /scripts/api.lua
	@echo "\nFinish [$@]\n"
	@docker kill $@-benchmark
	sleep 1