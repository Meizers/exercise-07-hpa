"""Synthetic load for the node-registry API, to push CPU past the HPA target.

Run headless against a port-forwarded Service, for example:
    kubectl port-forward svc/node-registry 8080:8080
    locust -f loadtest/locustfile.py --headless -u 50 -r 10 -t 3m --host http://localhost:8080
"""

from locust import HttpUser, between, task


class NodeRegistryUser(HttpUser):
    wait_time = between(0.1, 0.5)

    @task(3)
    def health(self):
        self.client.get("/health")

    @task(1)
    def list_nodes(self):
        self.client.get("/api/nodes")
