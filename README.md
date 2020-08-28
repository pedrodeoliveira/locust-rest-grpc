# Distributed Load Testing of REST/gRPC APIs using Locust

This project provides code and configuration for performing distributed load testing of REST and gRPC APIs. As described in [Distribute Load Testing Using GKE](https://github.com/GoogleCloudPlatform/distributed-load-testing-using-kubernetes), *"Load testing is key to the development of any backend infrastructure because load tests demonstrate how well the system functions when faced with real-world demands"*. 

As a use case for the Web APIs, we implement an API that serves predictions of a Machine Learning model. The problem at hand is an hypothetical *text classification/categorization* problem. A user can send a **predict** request with a string of text (to categorize), and the API will return the **predicted** category (an integer).

This project uses [Locust](https://locust.io/) as a tool for performing the load testing, i.e, for simulating users/clients making requests to the APIs. This tool can be used in a standalone mode, but can also be executed on a distributed mode. In the latter, we will have a **master** running the a Web UI and a set of **workers** simulating the actual users/clients. Running in a distributed fashion enables us to achieve a higher Requests Per Second (RPS) rate when testing the APIs. The RPS will be limited by either the API or the Locust workers throughput.

In the tests that are performed we will pay close attention to the RPS rate (throughput) the latency percentiles and to failure rates as well.

## Distributed Load Testing with Locust

## Web APIs

This section brifely describes the Web APIs implemented in this project that can be tested using the Locust Workers developed here.

- Python REST API using FastAPI
- Python gRPC API
- Go REST API
- Go gRPC API

## GKE Setup

### Requirements

- have a GCP account
- enable the relevant APIs
- gcloud and kubectl must be installed

### Configure GCP Defaults

```bash
$ PROJECT=locust-rest-grpc && \
REGION=europe-west2 && \
ZONE=${REGION}-b && \
CLUSTER=gke-load-test && \
gcloud config set compute/region $REGION && \
gcloud config set compute/zone $ZONE
```

Enable the relevant APIs:

```bash
$ gcloud services enable \
    cloudbuild.googleapis.com \
    compute.googleapis.com \
    container.googleapis.com \
    containeranalysis.googleapis.com \
    containerregistry.googleapis.com 
```

### Create a Cluster in GKE

```bash
$ gcloud container clusters create $CLUSTER --machine-type=n1-standard-8
```

Get the credentials of the newly create GKE cluster, which will update the `.kubeconfig` file.

```bash
$ gcloud container clusters get-credentials $CLUSTER
```

### Build Images with Locust Workers and Python APIs

Given that we are using the Google Cloud, we will use for convinience the Container Builder to build and upload the images into the GCP's Container Registry.

The below command can be used for building the image that will contain both the code with Locust Master and Workers (for both REST and gRPC flavours) together with the code for the Python Web APIs (FastAPI and gRPC-based API):

```bash
$ gcloud builds submit --tag gcr.io/$PROJECT/locust-rest-grpc:latest .
```

### Build Images for the Go REST/gRPC APIs

Build the Go REST API with:

```bash
$ gcloud builds submit --config cloudbuild_rest_go.yaml
```

Similarly, build the Go gRPC API with:

```bash
$ gcloud builds submit --config cloudbuild_grpc_go.yaml
```

The previous commands will generate the images `gcr.io/$PROJECT/rest-go` and `gcr.io/$PROJECT/grpc-go`, respectively.

### Cleanup

```bash
$ gcloud container clusters delete $CLUSTER --zone $ZONE
```

## Results


## Conclusions


## Links

- [Seldon-core Benchmarking](https://docs.seldon.io/projects/seldon-core/en/v1.1.0/reference/benchmarking.html)
- [Testing others systems using custom clients](https://docs.locust.io/en/stable/testing-other-systems.html)
- [Distribute Load Testing Using GKE](https://github.com/GoogleCloudPlatform/distributed-load-testing-using-kubernetes)
