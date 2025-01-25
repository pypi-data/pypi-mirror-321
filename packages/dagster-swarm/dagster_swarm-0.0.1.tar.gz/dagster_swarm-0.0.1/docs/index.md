# Home

A Dagster integration for running in a Docker Swarm configuration.

!!! note

    This project is **not** affiliated with Dagster.

Currently, `dagster-docker` provides the capability to launch runs in new containers.
However, this is limited to the same host as the Docker daemon.

In order to decouple the run execution from the rest of the Dagster system, Docker Swarm can be used to distributed workloads across Swarm nodes.

## Limitation of `dagster-docker`

`dagster-docker` uses `docker-py` to interface with the Docker client and explicility starts containers using the "container" API.
To use Swarm, containers should be started using the "service" API instead.

This project references the `dagster-docker` implementation, but swaps the "container" API for the "service" API.
