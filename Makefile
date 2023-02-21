.PHONY: install-requirements database-exec rebuild-streamlit rebuild-api predict train dive


install-requirements:
	pip install poetry
	poetry install
	poetry shell

# Define variables for the Docker image and container names
STREAMLIT_IMAGE = streamlit-app
STREAMLIT_CONTAINER = streamlit-container
API_IMAGE = app
API_CONTAINER = fastapi-container

# Set the Docker environment to use minikube
docker-env:
	eval $$(minikube docker-env)

# Rebuild the specified Docker image and update the corresponding container in Kubernetes
rebuild-image:
	docker build -t $(IMAGE):$(TAG) $(DOCKERFILE_DIR)/
	kubectl set image deployment/$(DEPLOYMENT) $(CONTAINER)=$(IMAGE):$(TAG)

# Rebuild the Streamlit Docker image and update the corresponding container in Kubernetes
rebuild-streamlit: docker-env
	$(eval DOCKERFILE_DIR := dashboard)
	make rebuild-image IMAGE=$(STREAMLIT_IMAGE) CONTAINER=$(STREAMLIT_CONTAINER) DEPLOYMENT=streamlit-deployment

# Rebuild the API Docker image and update the corresponding container in Kubernetes
rebuild-api: docker-env
	$(eval DOCKERFILE_DIR := .)
	make rebuild-image IMAGE=$(API_IMAGE) CONTAINER=$(API_CONTAINER) DEPLOYMENT=fastapi-deployment

# Make a prediction using the API
run-api-command = poetry run python -m api.api_requests -e $(1)

predict:
	$(call run-api-command,predict)

# Train the model using the API
train:
	$(call run-api-command,train)

train-and-predict: rebuild-api
	$(call run-api-command,train)
	$(call run-api-command,predict)

dive:
	docker build -t app:latest .
	dive app:latest

clean:
	rm -rf api/__pycache__/
