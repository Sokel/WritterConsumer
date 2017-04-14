build:
	docker build -t writter_consumer .
run:
	docker run -it --rm --name writter_consumer writter_consumer
