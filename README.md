# Distributed Load Testing of REST/gRPC APIs using Locust

This project provides code and configuration for performing distributed Load testing of REST and gRPC APIs. As described in [Distribute Load Testing Using GKE](https://github.com/GoogleCloudPlatform/distributed-load-testing-using-kubernetes), *"Load testing is key to the development of any backend infrastructure because load tests demonstrate how well the system functions when faced with real-world demands"*. 

As a use for the Web APIs we use a Machine Learning serving problem, where the APIs serve predictions of a ML model. The problem at hand is an hypothetical *text classification/categorization* problem. A user can send a *predict* request with a string of text (to categorize), and the API will return the *predicted* category (an integer).

The tool used for performing the Load testing, i.e, for simulating users making requests to the API is [Locust](https://locust.io/). This tool can be used in a standalone mode, but can also be executed on distributed mode. In this mode, we will have a **master** running the a Web UI and a set of **workers** simulating the actual users. The **master** process will aggregate results as well. Running in a distributed fashion enables us to achieve a higher Requests Per Second (RPS) rate when testing the APIs.


## GKE Setup

### Requirements

- have a GCP account
- enable the relevant APIs
- gcloud and kubectl must be installed

### Configure GCP Defaults

```bash
PROJECT=locust-rest-grpc
REGION=europe-west2
ZONE=${REGION}-b
CLUSTER=gke-load-test
gcloud config set compute/region $REGION 
gcloud config set compute/zone $ZONE
```

Enable the relevant APIs:

```bash
gcloud services enable \
    cloudbuild.googleapis.com \
    compute.googleapis.com \
    container.googleapis.com \
    containeranalysis.googleapis.com \
    containerregistry.googleapis.com 
```

### Create a Cluster in GKE

```bash
gcloud container clusters create $CLUSTER --machine-type=n1-standard-8
```

```bash
gcloud container clusters get-credentials $CLUSTER
```

```bash
gcloud builds submit \
    --tag gcr.io/$PROJECT/locust-rest-grpc:latest .
```


### Cleanup

```bash
$ gcloud container clusters delete $CLUSTER --zone $ZONE
```

## Links

- [Seldon-core Benchmarking](https://docs.seldon.io/projects/seldon-core/en/v1.1.0/reference/benchmarking.html).
- [Testing others systems using custom clients](https://docs.locust.io/en/stable/testing-other-systems.html)
- [Distribute Load Testing Using GKE](https://github.com/GoogleCloudPlatform/distributed-load-testing-using-kubernetes)
