# tools/web_search.py

from typing import Any
import json
import os
from dotenv import load_dotenv
from tavily import TavilyClient
from mcp.types import TextContent
from typing import Sequence

# 载入环境变量
load_dotenv()

def register_tools_to(mcp):
    @mcp.tool()
    async def web_search(query: str) -> Sequence[TextContent]:
        """执行网络搜索并返回相关结果"""
        tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

        try:
            response = tavily_client.search(
                query=query,
                max_results=5,
                search_depth="advanced",
                include_answer="advanced"
            )
        except Exception as e:
            return [TextContent(type="text", text=f"搜索失败: {str(e)}")]

        return [TextContent(type="text", text=json.dumps(response, indent=2, ensure_ascii=False))]
