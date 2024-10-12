import pulumi

import chart
import ingress

# Config
config = pulumi.Config()
chart_config = config.get_object("Chart")
ingress_config = config.get_object("Ingress")

# Create Chart
for charts in chart_config:
    chart.create(
        charts["name"],
        charts["helm-repo"],
        charts["values"],
    )

# Create Ingress
for ingresses in ingress_config:
    ingress.create(
        ingresses["name"],
        ingresses["ingress-host"],
        ingresses["ingress-port"],
    )
