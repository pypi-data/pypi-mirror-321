# IMPORT SoftwareAI _init_environment_
from softwareai.CoreApp._init_environment_ import init_env
# IMPORT SoftwareAI Agents
from softwareai.CoreApp.Agents.Software_Development.QuantumCore import QuantumCoreUpdate
#########################################
# IMPORT SoftwareAI Core
from softwareai.CoreApp._init_core_ import * 
#########################################
# IMPORT SoftwareAI keys
from softwareai.CoreApp._init_keys_ import *
#########################################


def autoupdaterepo(repo_name):
    
    init_env(repo_name)

    Melhorias = QuantumCoreUpdate(
                repo_name,
                OpenAIKeysinit,
                FirebaseKeysinit,
                OpenAIKeysteste,
                GithubKeys,
                python_functions,
                Agent_files_update,
                AutenticateAgent,
                ResponseAgent,
            )