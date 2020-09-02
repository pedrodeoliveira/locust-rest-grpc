# Distributed Load Testing Results

This section provides the results of the distributed load tests performed using the various implemented APIs. The first set of tests were targeted to assess the performance of the APIs when using a single core. Next, the second set of tests evaluated the performance of the API when it was deployed in a single node with 8 cores. For the latter test case, there are two options: (i) 1 replica of the API using all the cores; or (ii) 8 replicas of the API each using 1 core.

The Locust master and workers were schedule on different nodes of the k8s cluster. For the master only one replica is deployed given it does not required a lot of computation power. The Locust workers were deployed as 14 replicas each of them configured for requesting 1 cpu for their processing work.


## Initial Setup

For making sure that the API replicas were scheduled in a single node, we have used the `nodeSelector` feature of k8s. First we labelled a node by running:

```bash
$ kubectl label nodes <node_id> workload=api
```

Then, we have added the following configuration in each of the API's `deployment` files.

```yaml
    spec:
      containers:
      ...
      nodeSelector:
        workload: api
```

## Tests using 1 CPU

In these tests the API deployments are configured to deploy a single replica and the underlying container requests a single cpu and has a limit of two cpus. As such, in pratice the pod will be able to use two cores when needed.

### REST Python

![](../resources/results/rest-py-1-cpu/statistics.png)

<details>
  <summary>Details</summary>

![](../resources/results/rest-py-1-cpu/rps.png)
![](../resources/results/rest-py-1-cpu/response_times.png)
![](../resources/results/rest-py-1-cpu/users.png)
</details>

### REST Go

![](../resources/results/rest-go-1-cpu/statistics.png)

<details>
  <summary>Details</summary>

![](../resources/results/rest-go-1-cpu/rps.png)
![](../resources/results/rest-go-1-cpu/response_time.png)
![](../resources/results/rest-go-1-cpu/users.png)
</details>

### gRPC Python

![](../resources/results/grpc-py-1-cpu/statistics.png)

<details>
  <summary>Details</summary>

![](../resources/results/grpc-py-1-cpu/rps.png)
![](../resources/results/grpc-py-1-cpu/response_time.png)
![](../resources/results/grpc-py-1-cpu/users.png)
</details>


### gRPC Go

![](../resources/results/grpc-go-1-cpu/statistics.png)

<details>
  <summary>Details</summary>

![](../resources/results/grpc-go-1-cpu/rps.png)
![](../resources/results/grpc-go-1-cpu/response_time.png)
![](../resources/results/grpc-go-1-cpu/users.png)
</details>


## Tests using 1 Node with 8 CPUs

### REST Python

![](../resources/results/rest-py-8-cpu/statistics.png)

<details>
  <summary>Details</summary>

![](../resources/results/rest-py-8-cpu/rps.png)
![](../resources/results/rest-py-8-cpu/response_time.png)
![](../resources/results/rest-py-8-cpu/users.png)
</details>


### REST Python (single replica)

![](../resources/results/rest-py-8-cpu-1-replica/statistics.png)

<details>
  <summary>Details</summary>

![](../resources/results/rest-py-8-cpu-1-replica/rps.png)
![](../resources/results/rest-py-8-cpu-1-replica/response_time.png)
![](../resources/results/rest-py-8-cpu-1-replica/users.png)
</details>

### REST Go

![](../resources/results/rest-go-8-cpu/statistics.png)

<details>
  <summary>Details</summary>

![](../resources/results/rest-go-8-cpu/rps.png)
![](../resources/results/rest-go-8-cpu/response_time.png)
![](../resources/results/rest-go-8-cpu/users.png)
</details>

### gRPC Python

![](../resources/results/grpc-py-8-cpu/statistics.png)

<details>
  <summary>Details</summary>

![](../resources/results/grpc-py-8-cpu/rps.png)
![](../resources/results/grpc-py-8-cpu/response_time.png)
![](../resources/results/grpc-py-8-cpu/users.png)
</details>

<details>
  <summary>Issues</summary>

![](../resources/results/grpc-py-8-cpu/pods_sleeping_1.png)
</details>

### gRPC Python (single replica)

![](../resources/results/grpc-py-8-cpu-1-replica/statistics.png)

<details>
  <summary>Details</summary>

![](../resources/results/grpc-py-8-cpu-1-replica/rps.png)
![](../resources/results/grpc-py-8-cpu-1-replica/response_time.png)
![](../resources/results/grpc-py-8-cpu-1-replica/users.png)
</details>

### gRPC Go

![](../resources/results/grpc-go-8-cpu/statistics.png)

<details>
  <summary>Details</summary>

![](../resources/results/grpc-go-8-cpu/rps.png)
![](../resources/results/grpc-go-8-cpu/response_time.png)
![](../resources/results/grpc-go-8-cpu/users.png)
</details>

<details>
  <summary>Issues</summary>

![](../resources/results/grpc-go-8-cpu/pod_sleeping_1.png)
</details>