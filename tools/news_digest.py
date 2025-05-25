# tools/news_digest.py

import os
import httpx
from dotenv import load_dotenv
from mcp.types import TextContent
from typing import Sequence

load_dotenv()

def register_tools_to(mcp):
    @mcp.tool()
    async def news_digest(category: str = "top") -> Sequence[TextContent]:
        """
        获取今日头条热点或指定分类新闻摘要（使用聚合数据接口）
        可选分类: top, shehui, guonei, guoji, yule, tiyu, keji, caijing, junshi, youxi, qiche, jiankang
        """
        api_key = os.getenv("JUHE_API_KEY")
        url = "http://v.juhe.cn/toutiao/index"
        params = {
            "type": category,
            "key": api_key
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, params=params)
                data = response.json()
            except Exception as e:
                return [TextContent(type="text", text=f"请求失败：{str(e)}")]

        if data.get("error_code") != 0:
            return [TextContent(type="text", text=f"API 错误：{data.get('reason')}")]

        articles = data["result"]["data"]
        result = "\n\n".join([f"{a['title']}\n{a['url']}" for a in articles[:5]])

        return [TextContent(type="text", text=f"【{category}】新闻推送：\n\n{result}")]
