# 🚀 项目部署指南：SmartBridge 智能工具平台

本指南将指导你如何从 0 到 1 部署并运行 SmartBridge 项目，包括：

- 🛠 本地开发环境搭建  
- ⚙️ 运行 MCP 服务与 Inspector  
- 📦 依赖管理与配置  
- ☁️ 可选部署方向（如 Render、Railway）

---
## 📁 目录结构
mcp_demo/ ├── server.py # MCP 服务主入口 ├── .env # 环境变量文件（包含 API 密钥） ├── requirements.txt # 依赖文件 ├── tools/ │ ├── init.py │ ├── bmi_advanced.py # BMI 工具模块 │ ├── web_search.py # Tavily 搜索模块 │ └── news_digest.py # 新闻聚合模块（聚合数据）
yaml
复制代码
---

## 🧱 环境准备

### ✅ 1. 克隆或创建本地项目

```bash
git clone https://github.com/Cooperiano/nvidia-hackthon
cd nvidia-hackthon
或将上述结构文件拷贝至你的本地目录。

✅ 2. 创建并激活 Python 虚拟环境
bash
复制代码
python -m venv .venv
source .venv/bin/activate    # macOS/Linux
.venv\Scripts\activate       # Windows
📦 依赖安装
✅ 3. 安装项目依赖
bash
复制代码
pip install -r requirements.txt
示例 requirements.txt 内容：
text
复制代码
mcp
python-dotenv
httpx
tavily
🔐 环境变量配置
✅ 4. 创建 .env 文件并填写：
makefile
复制代码
JUHE_API_KEY=你的聚合数据API Key
TAVILY_API_KEY=你的Tavily API Key
若你没有 API Key，可访问：

聚合数据
Tavily
▶️ 本地运行
✅ 5. 启动 MCP 服务（开发模式）
bash
复制代码
mcp dev server.py
Inspector 会自动在浏览器打开：
👉 http://localhost:6274/#tools

你将看到 bmi_advanced、web_search、news_digest 等工具。

🧪 调试与测试
每个工具的输入参数会自动生成表单；
可直接点工具进行测试；
控制台会打印所有注册工具的调试信息。


🧠 故障排查
问题	可能原因
工具不显示在 Inspector 中	register_all(mcp) 未调用，或装饰器缺失
.env 无效	load_dotenv() 未调用或路径错误
API 请求失败	Key 错误、网络问题、被限流
MCP Inspector 无响应	检查 mcp dev 是否正常启动
📈 后续建议
将工具返回结果格式化为卡片式 Markdown；
接入 Streamlit/FastAPI 构建前端；
添加日志记录、用户输入缓存、响应时间监控；
支持任务链式调用（如搜索 → 阅读 → 摘要）。



✅ 项目启动指令汇总
bash
复制代码
# 一次性执行：
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # 手动填写 key
mcp dev server.py
