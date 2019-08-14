build:
	pipenv install --dev

lint:
	pipenv run flake8

start:
	pipenv run python app.py

docker:
	docker build -t eu.gcr.io/census-rm-ci/rm/census-rm-notify-stub .

docker-run:
	docker run --name=notifystub -p 8917:5000 eu.gcr.io/census-rm-ci/rm/census-rm-notify-stub:latest