PROD_FILE=prod.dockerfile
CLUSTER_NAME=storm-server
IMAGE_NAME=storm-server
CLUSTER=k3d-cluster/devcluster.yaml

###################################
# k3d based commands
###################################
build-import:
	@echo "Creating $(IMAGE_NAME)"
	docker buildx build --tag $(IMAGE_NAME):latest --no-cache -f $(PROD_FILE) .
	@echo "Finished creating $(IMAGE_NAME) docker image!"
	@echo "Importing into k3d now!"
	k3d image import $(IMAGE_NAME) -c $(CLUSTER_NAME)

create-cluster:
	@echo "Creating cluster $(CLUSTER_NAME)!"
	k3d cluster create -c $(CLUSTER)
	@echo "Creating $(IMAGE_NAME)"
	docker buildx build --tag $(IMAGE_NAME):latest --no-cache -f $(PROD_FILE) .
	@echo "Finished creating $(IMAGE_NAME) docker image!"
	@echo "Importing into k3d now!"
	k3d image import $(IMAGE_NAME) -c $(CLUSTER_NAME)

delete-cluster:
	@echo "Removing cluster $(CLUSTER_NAME) now!"
	k3d cluster delete -c $(CLUSTER)