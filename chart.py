from pulumi_kubernetes.helm.v3 import Chart, ChartOpts, FetchOpts


def create(name, repo, values):
    return {
        name: Chart(
            name,
            ChartOpts(
                chart=name,
                fetch_opts=FetchOpts(repo=repo),
                values=values,
            ),
        )
    }
