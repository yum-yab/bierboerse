
run-mypy:
	poetry run mypy bierboerse
	


run-black:
	poetry run black bierboerse

check: run-black run-mypy
