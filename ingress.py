from pulumi_kubernetes.networking.v1 import Ingress


def create(name, host, port):
    return {
        name: Ingress(
            name,
            metadata={
                "name": name,
                "annotations": {"ingress.kubernetes.io/ssl-redirect": "false"},
            },
            spec={
                "rules": [
                    {
                        "host": host,
                        "http": {
                            "paths": [
                                {
                                    "path": "/",
                                    "path_type": "Prefix",
                                    "backend": {
                                        "service": {
                                            "name": name,
                                            "port": {"number": port},
                                        }
                                    },
                                }
                            ]
                        },
                    }
                ]
            },
        )
    }
