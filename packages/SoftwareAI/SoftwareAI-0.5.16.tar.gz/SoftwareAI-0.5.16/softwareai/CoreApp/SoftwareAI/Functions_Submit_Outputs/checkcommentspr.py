
#########################################
# IMPORT SoftwareAI Libs 
from softwareai.CoreApp._init_libs_ import *
#########################################
# IMPORT SoftwareAI Functions
from softwareai.CoreApp._init_functions_ import *
#########################################

def submit_output_checkcommentspr(function_name,
                                function_arguments,
                                tool_call,
                                threead_id,
                                client,
                                run
                                ):

    if function_name == 'checkcommentspr':
        args = json.loads(function_arguments)
        result = checkcommentspr(
            OWNER=args['OWNER'],
            REPO=args['REPO'],
            PR_NUMBER=args['PR_NUMBER'],
            github_token=args['github_token']
        )
        tool_call_id = tool_call.id
        client.beta.threads.runs.submit_tool_outputs(
            thread_id=threead_id,
            run_id=run.id,
            tool_outputs=[
                {
                    "tool_call_id": tool_call_id,
                    "output": json.dumps(result)
                }
            ]
        )
