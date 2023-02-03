database-exec:
	kubectl exec -it postgres-statefulset-0 -- psql -h localhost -U user --password -p 5432

rebuild-streamlit:
	eval $(minikube docker-env)
	docker build -t streamlit-app:$(TAG) dashboard/
	kubectl set image deployment/streamlit-deployment streamlit-container=streamlit-app:$(TAG)

rebuild-api:
	eval $(minikube docker-env)
	docker build -t app:$(TAG) .
	kubectl set image deployment/fastapi-deployment fastapi-container=app:$(TAG)

predict:
	poetry run python -m api.api_requests -e predict

train:
	poetry run python -m api.api_requests -e train
