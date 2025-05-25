# tools/__init__.py

from tools.bmi_advanced import register_tools_to as register_bmi

def register_all(mcp):
    register_bmi(mcp)
    # register_web(mcp)
