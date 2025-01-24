import logging

from cached_property import cached_property
from sonarqube import SonarQubeClient
from sonarqube.utils.exceptions import NotFoundError

LOGGER = logging.getLogger(__name__)

METRIC_KEYS = ["code_smells", "bugs", "vulnerabilities", "security_hotspots"]


class SonarQubeProject:
    """SonarQube project."""

    def __init__(self, project_key, host, token, branch=None):
        """Sonarqube Project for fetching metrics.

        Args:
            project_key: sonarqube project key
            host: cluster hostname
            token: User token
            branch: Respective branch for analysis
        """
        self.project_key = project_key
        self.host = host
        self.token = token
        self.branch = branch

    @cached_property
    def client(self):
        """Return sonarqube API client."""
        return SonarQubeClient(sonarqube_url=self.host, token=self.token)

    def get_measures(self, new=False):
        """Get metrics.

        Args:
            new: Metrics for New code else it will take overall code.
        """
        if new:
            metric_keys = ",".join([f"new_{k}" for k in METRIC_KEYS])
        else:
            metric_keys = ",".join(METRIC_KEYS)

        data = self.client.measures.get_component_with_specified_measures(
            component=self.project_key, fields="metrics,periods", metricKeys=metric_keys
        )
        measures = data.get("component", {}).get("measures", [])

        _measures = []
        if new:
            for measure in measures:
                _measure = {"metric": measure["metric"]}
                _measure.update(measure["period"])
                _measures.append(_measure)
            return _measures
        return {m["metric"]: int(m["value"]) for m in measures}

    def get_quality_gates_status(self):
        """Quality gate status."""
        data = self.client.qualitygates.get_project_qualitygates_status(projectKey=self.project_key)
        return data["projectStatus"]

    def get_last_update_time(self):
        """Collect last analysis time."""
        try:
            data = self.client.project_analyses.search_project_analyses_and_events(
                project=self.project_key, branch=self.branch, ps=2
            )
        except NotFoundError as e:
            msg = f"branch '{self.branch}' not found"
            if msg in str(e):
                LOGGER.warning(f"[SonarQube] {msg}. Collecting global event.")
                data = self.client.project_analyses.search_project_analyses_and_events(
                    project=self.project_key, ps=2
                )
        if data["analyses"]:
            date = data["analyses"][0]["date"]
            LOGGER.info(f"Last analysis {data['analyses'][0]['key']} time: {date}")
            return date


def get_sonar_metrics(project_key, host, token, branch):
    LOGGER.info(f"[SonarQube] Collecting metrics for {project_key}")
    sonar = SonarQubeProject(project_key=project_key, host=host, token=token, branch=branch)
    try:
        measures = sonar.get_measures()
        last_update_time = sonar.get_last_update_time()
    except NotFoundError as e:
        LOGGER.error(e)
        return None

    if measures:
        measures["sonar_last_analysis"] = last_update_time
    return measures


if __name__ == "__main__":
    pass
