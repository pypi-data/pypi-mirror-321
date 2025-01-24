
#########################################
# IMPORT SoftwareAI Libs 
from softwareai.CoreApp._init_libs_ import *
#########################################
# IMPORT SoftwareAI Functions
from softwareai.CoreApp._init_functions_ import autoupdaterepo
#########################################
# IMPORT SoftwareAI Core
from softwareai.CoreApp._init_core_ import * 
#########################################
# IMPORT SoftwareAI keys
from softwareai.CoreApp._init_keys_ import *
#########################################

def submit_output_autoupdaterepo(function_name,
                                function_arguments,
                                tool_call,
                                threead_id,
                                client,
                                run
                                ):

    if function_name == 'autoupdaterepo':
        args = json.loads(function_arguments)     
        result = autoupdaterepo(
                repo_name=args['repo_name'],
                OpenAIKeysinit=OpenAIKeysinit,
                FirebaseKeysinit=FirebaseKeysinit,
                OpenAIKeysteste=OpenAIKeysteste,
                GithubKeys=GithubKeys,
                python_functions=python_functions,
                Agent_files_update=Agent_files_update,
                AutenticateAgent=AutenticateAgent,
                ResponseAgent=ResponseAgent,
                )

        try:
            run = client.beta.threads.runs.submit_tool_outputs_and_poll(
            thread_id=threead_id,
            run_id=run.id,
            tool_outputs=[{
            "tool_call_id": tool_call.id,
            "output": json.dumps(result)
            }]
            )
            print("Tool outputs submitted successfully.")
            return True
        except Exception as e:
            print("Failed to submit tool outputs:", e)
