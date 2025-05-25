# server.py

from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
load_dotenv()

# 初始化 MCP 服务
mcp = FastMCP("my_server")


# 从工具模块注册所有工具
from tools.bmi_advanced import register_tools_to
register_tools_to(mcp)

from tools.web_search import register_tools_to as register_web
register_web(mcp)

from tools.news_digest import register_tools_to as register_news
register_news(mcp)

# 其他工具也可以类似引入
# from tools import register_all
# register_all(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")