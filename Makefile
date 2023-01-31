database-exec:
	kubectl exec -it postgres-statefulset-0 -- psql -h localhost -U user --password -p 5432

rebuild-streamlit:
	eval $(minikube docker-env)
	docker build -t streamlit-app:$(TAG) dashboard/
	kubectl set image deployment/streamlit-deployment streamlit-container=streamlit-app:$(TAG)
	kubectl port-forward service/streamlit-service 8501:8501

rebuild-api:
	eval $(minikube docker-env)
	docker build -t app:$(TAG) .
	kubectl set image deployment/fastapi-deployment fastapi-container=app:$(TAG)
	kubectl port-forward service/fastapi-service 8000:8000

predict:
	poetry run python -m api.api_requests -e predict

train:
	poetry run python -m api.api_requests -e train
