# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from promptflow.core import tool
# import asyncio
import os

from config.sk_service_configurator import add_service
from semantic_kernel import Kernel
from semantic_kernel.planners.function_calling_stepwise_planner import FunctionCallingStepwisePlanner

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need


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
    # goal = "Figure out how much I have if first, my investment of 2130.23 dollars increased by 23%, and then I spend $5 on a coffee"  # noqa: E501

    # Execute the plan
    result = await planner.invoke(kernel=kernel, question=input1)

    #print(f"The goal: {input1}")
    #print(f"Plan result: {result.final_answer}")
    # </RunPlanner>

    return result.final_answer
