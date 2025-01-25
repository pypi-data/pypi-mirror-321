from dagster._core.launcher.base import RunLauncher


class SwarmRunLauncher(RunLauncher):
    """Run launcher for kicking off runs within a Docker Swarm."""


class CodeLocationSwarmRunLauncher(SwarmRunLauncher):
    """Run launcher for kicking off runs on the same node as the job's code location."""
