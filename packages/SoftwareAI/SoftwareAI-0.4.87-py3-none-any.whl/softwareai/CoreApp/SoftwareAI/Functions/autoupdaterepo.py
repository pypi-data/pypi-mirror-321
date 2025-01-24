# IMPORT SoftwareAI _init_environment_
from softwareai.CoreApp._init_environment_ import init_env


def autoupdaterepo(repo_name, appfb, client, SoftwareDevelopment):

    init_env(repo_name)

    Melhorias = SoftwareDevelopment.QuantumCoreUpdate(
        appfb, client, repo_name
        )