# IMPORT SoftwareAI _init_environment_
from softwareai.CoreApp._init_environment_ import init_env
# IMPORT SoftwareAI Agents
from softwareai.CoreApp.Agents.Software_Development.QuantumCore import QuantumCoreUpdate

def autoupdaterepo(repo_name):
    
    init_env(repo_name)

    Melhorias = QuantumCoreUpdate(repo_name)