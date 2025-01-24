# IMPORT SoftwareAI _init_environment_
from softwareai.CoreApp._init_environment_ import init_env
# IMPORT SoftwareAI Agents
from softwareai.CoreApp._init_agents_ import AgentInitializer

def autoupdaterepo(repo_name):
    SoftwareDevelopment = AgentInitializer.get_agent('SoftwareDevelopment') 
    init_env(repo_name)

    Melhorias = SoftwareDevelopment.QuantumCoreUpdate(repo_name)