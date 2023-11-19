from sanic import Blueprint, Request
from sanic.response import file, json

from .exam import Exam

api = Blueprint("api", url_prefix="/api")


@api.route("/", methods=["GET"])
async def index(request: Request):
    """主页"""
    return await file("./static/index.html")


@api.route("/api/get_que", methods=["GET", "POST"])
async def get_que(request: Request):
    """获得题目"""
    content = request.json
    if not ("line" in content and "index" in content):
        return json({"code": 1, "msg": "参数错误"})
    line = content.get("line")
    index = content.get("index")
    return json({"code": 0, "msg": "ok", "data": Exam.get_que(line, index)})


@api.route("/api/get_line", methods=["GET", "POST"])
async def get_line(request: Request):
    content = request.json
    if not ("line" in content):
        return json({"code": 1, "msg": "参数错误"})
    line = content.get("line")
    return json({"code": 0, "msg": "ok", "data": Exam.get_line(line)})


@api.route("/api/query_que", methods=["GET", "POST"])
async def query_que(request: Request):
    """搜索题目"""
    content = request.json
    if "text" not in content:
        return json({"code": 1, "msg": "参数错误"})
    text = content.get("text")
    return json({"code": 0, "msg": "ok", "data": Exam.query_que(text)})


@api.route("/api/make_docx", methods=["GET", "POST"])
async def make_docx(request: Request):
    """生成 docx"""
    content = request.json
    if not ("ids" in content):
        return json({"code": 1, "msg": "参数错误"})
    ids = content.get("ids")
    if not (isinstance(ids, list) and 0 < len(ids) < 300):
        return json({"code": 1, "msg": "参数错误"})
    return json({"code": 0, "msg": "ok", "data": Exam.search_for(ids)})


@api.route("/api/make_exam", methods=["GET", "POST"])
async def make_exam(request: Request):
    """
    生成考试试卷
    - 单选题：`35x1`
    - 多选题：`25x1`
    - 判断题：`20x0.5`
    - 填空题：`20x1.5`
    """
    content = request.json
    if not (
        "seed" in content and content.get("seed").isdigit() and "course" in content
    ):
        return json({"code": 0, "msg": "参数错误"})
    seed = int(content.get("seed"))
    course = content.get("course")
    return json({"code": 0, "msg": "ok", "data": Exam.make_exam(course, seed)})
