
#########################################
# IMPORT SoftwareAI Libs 
from softwareai.CoreApp._init_libs_ import *
#########################################
# IMPORT SoftwareAI Functions
from softwareai.CoreApp._init_functions_ import *
#########################################


def submit_output_autogetfilecontent(function_name,
                                function_arguments,
                                tool_call,
                                threead_id,
                                client,
                                run
                                ):


    if function_name == 'autogetfilecontent':
        args = json.loads(function_arguments)
        result = autogetfilecontent(
            repo_name=args['repo_name'],
            file_path=args['file_path'],
            branch_name=args['branch_name'],
            companyname=args['companyname'],
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

