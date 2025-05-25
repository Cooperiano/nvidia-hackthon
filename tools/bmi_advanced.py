# tools/bmi_advanced.py

from mcp.types import TextContent
from typing import Sequence
import json

def register_tools_to(mcp):
    @mcp.tool()
    async def bmi_advanced(height_cm: float, weight_kg: float, age: int, gender: str) -> Sequence[TextContent]:
        height_m = height_cm / 100.0
        if height_m <= 0 or weight_kg <= 0:
            raise ValueError("身高和体重必须为正数")

        bmi = weight_kg / (height_m ** 2)
        category = (
            "偏瘦" if bmi < 18.5 else
            "正常" if bmi < 24 else
            "超重" if bmi < 28 else
            "肥胖"
        )

        def get_peer_comparison():
            avg_bmi = 22.0
            delta = bmi - avg_bmi
            if abs(delta) < 1:
                return "你的 BMI 接近同龄同性别人群的平均水平。"
            elif delta < -1:
                return "你的 BMI 低于同龄同性别人群的平均水平。"
            else:
                return "你的 BMI 高于同龄同性别人群的平均水平。"

        def get_diet_advice():
            if category == "偏瘦":
                return "建议增加蛋白质和复合碳水的摄入，提升每日总热量。"
            elif category == "正常":
                return "继续保持营养均衡，控制油盐糖摄入。"
            elif category == "超重":
                return "减少高糖高脂饮食，适度锻炼。"
            else:
                return "建议遵循营养师的低热量饮食方案。"

        result = {
            "身高": f"{height_cm} cm",
            "体重": f"{weight_kg} kg",
            "年龄": f"{age} 岁",
            "性别": gender,
            "BMI": round(bmi, 2),
            "健康建议": category,
            "与同龄人比较": get_peer_comparison(),
            "饮食建议": get_diet_advice()
        }

        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]
