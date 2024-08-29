from promptflow.core import tool
import os
from config.sk_service_configurator import add_service
from semantic_kernel import Kernel
from semantic_kernel.planners.function_calling_stepwise_planner import FunctionCallingStepwisePlanner

@tool
async def my_python_tool(input1: str) -> str:
    # <CreatePlanner>
    # Initialize the kernel
    kernel = Kernel()

    # Add the service to the kernel
    # use_chat: True to use chat completion, False to use text completion
    kernel = add_service(kernel=kernel, use_chat=True)

    script_directory = os.path.dirname(__file__)
    plugins_directory = os.path.join(script_directory, "plugins")
    kernel.add_plugin(parent_directory=plugins_directory, plugin_name="MathPlugin")

    planner = FunctionCallingStepwisePlanner(service_id="default")
    # </CreatePlanner>
    # <RunPlanner>

    # Execute the plan
    result = await planner.invoke(kernel=kernel, question=input1)

    # </RunPlanner>

    return result.final_answer
