from typing import List, Dict, Any
from .state import KnowledgePoint, SkillPoint, TaskStep, TrainingResource, PositionData, MajorData

mock_positions = {
    "新能源汽车维修技师": PositionData(
        position_id="pos001",
        position_name="新能源汽车维修技师",
        industry_id="ind001",
        responsibilities=[
            "新能源汽车电池包拆装与维护",
            "电机控制系统故障诊断",
            "充电系统检测与维修",
            "高压安全操作"
        ],
        required_skills=[
            "电池包结构认知",
            "高压安全操作",
            "万用表使用",
            "故障诊断"
        ],
        typical_tasks=[
            "新能源汽车电池包拆装",
            "电机控制器检测",
            "充电接口维修"
        ]
    ),
    "工业机器人操作员": PositionData(
        position_id="pos002",
        position_name="工业机器人操作员",
        industry_id="ind002",
        responsibilities=[
            "工业机器人编程与调试",
            "机器人日常维护保养",
            "生产线协作作业",
            "故障排查与处理"
        ],
        required_skills=[
            "机器人编程语言",
            "PLC基础",
            "机械臂操作",
            "安全规范执行"
        ],
        typical_tasks=[
            "工业机器人示教编程",
            "机器人末端执行器更换",
            "生产线机器人协同调试"
        ]
    )
}

mock_majors = {
    "新能源汽车技术": MajorData(
        major_id="maj001",
        major_name="新能源汽车技术",
        related_positions=["新能源汽车维修技师", "电池检测工程师"],
        core_courses=["新能源汽车构造", "电池技术", "电机控制", "高压安全"],
        training_objectives=["掌握新能源汽车结构原理", "具备电池维护技能", "熟悉高压安全规范"]
    ),
    "工业机器人技术": MajorData(
        major_id="maj002",
        major_name="工业机器人技术",
        related_positions=["工业机器人操作员", "机器人调试工程师"],
        core_courses=["机器人原理", "PLC编程", "机器人编程", "自动化生产线"],
        training_objectives=["掌握机器人操作技能", "具备编程调试能力", "熟悉工业安全规范"]
    )
}

mock_knowledge_points = [
    KnowledgePoint(knowledge_id="k001", knowledge_name="电池包结构", category="理论知识", description="新能源汽车电池包的组成结构和工作原理", difficulty=3),
    KnowledgePoint(knowledge_id="k002", knowledge_name="高压安全规范", category="安全知识", description="新能源汽车高压系统安全操作规范", difficulty=4),
    KnowledgePoint(knowledge_id="k003", knowledge_name="电机控制原理", category="理论知识", description="新能源汽车驱动电机的控制原理", difficulty=4),
    KnowledgePoint(knowledge_id="k004", knowledge_name="机器人运动学", category="理论知识", description="工业机器人运动学基础", difficulty=4),
    KnowledgePoint(knowledge_id="k005", knowledge_name="PLC基础", category="理论知识", description="可编程逻辑控制器基础知识", difficulty=3),
    KnowledgePoint(knowledge_id="k006", knowledge_name="充电系统原理", category="理论知识", description="新能源汽车充电系统工作原理", difficulty=3)
]

mock_skill_points = [
    SkillPoint(skill_id="s001", skill_name="电池包拆装", category="操作技能", description="新能源汽车电池包的拆卸与安装操作", proficiency_level=4),
    SkillPoint(skill_id="s002", skill_name="高压安全操作", category="安全技能", description="高压系统安全操作技能", proficiency_level=5),
    SkillPoint(skill_id="s003", skill_name="万用表使用", category="工具技能", description="万用表测量操作技能", proficiency_level=3),
    SkillPoint(skill_id="s004", skill_name="机器人示教", category="操作技能", description="工业机器人示教编程操作", proficiency_level=4),
    SkillPoint(skill_id="s005", skill_name="故障诊断", category="综合技能", description="设备故障诊断与排查能力", proficiency_level=4),
    SkillPoint(skill_id="s006", skill_name="工具使用", category="工具技能", description="常用维修工具的正确使用", proficiency_level=2)
]

mock_resources = [
    TrainingResource(resource_id="r001", resource_name="新能源汽车电池包结构微课", resource_type="微课", resource_url="https://example.com/battery-course", description="讲解电池包结构的教学视频"),
    TrainingResource(resource_id="r002", resource_name="高压安全操作仿真", resource_type="仿真软件", resource_url="https://example.com/hv-simulator", description="高压安全操作模拟训练软件"),
    TrainingResource(resource_id="r003", resource_name="电池拆装实操指导", resource_type="实训指导", resource_url="https://example.com/battery-guide", description="电池包拆装实操详细指导"),
    TrainingResource(resource_id="r004", resource_name="机器人示教编程微课", resource_type="微课", resource_url="https://example.com/robot-course", description="工业机器人示教编程教学视频"),
    TrainingResource(resource_id="r005", resource_name="机器人仿真平台", resource_type="仿真软件", resource_url="https://example.com/robot-simulator", description="工业机器人仿真训练平台")
]

def analyze_task(task: str) -> Dict[str, Any]:
    analysis = {
        "task_name": task,
        "task_type": "实操任务",
        "complexity": "中等",
        "estimated_duration": 120,
        "required_tools": ["扳手", "万用表", "绝缘工具"],
        "safety_requirements": ["佩戴绝缘手套", "断开高压电源", "设置警示标识"],
        "key_operations": ["拆卸固定螺栓", "断开连接线束", "检查外观状态", "安装密封件", "性能测试"]
    }
    return analysis

def query_position(position_name: str) -> Dict[str, Any]:
    position = mock_positions.get(position_name)
    if position:
        return {
            "position_id": position.position_id,
            "position_name": position.position_name,
            "responsibilities": position.responsibilities,
            "required_skills": position.required_skills,
            "typical_tasks": position.typical_tasks
        }
    return {"error": f"未找到岗位: {position_name}"}

def query_major(major_name: str) -> Dict[str, Any]:
    major = mock_majors.get(major_name)
    if major:
        return {
            "major_id": major.major_id,
            "major_name": major.major_name,
            "related_positions": major.related_positions,
            "core_courses": major.core_courses,
            "training_objectives": major.training_objectives
        }
    return {"error": f"未找到专业: {major_name}"}

def extract_knowledge_points(task: str, position_name: str) -> List[Dict[str, Any]]:
    result = []
    if "电池" in task or "新能源" in task:
        result.extend([
            {"knowledge_id": "k001", "knowledge_name": "电池包结构", "category": "理论知识", "difficulty": 3},
            {"knowledge_id": "k002", "knowledge_name": "高压安全规范", "category": "安全知识", "difficulty": 4},
            {"knowledge_id": "k006", "knowledge_name": "充电系统原理", "category": "理论知识", "difficulty": 3}
        ])
    if "机器人" in task:
        result.extend([
            {"knowledge_id": "k004", "knowledge_name": "机器人运动学", "category": "理论知识", "difficulty": 4},
            {"knowledge_id": "k005", "knowledge_name": "PLC基础", "category": "理论知识", "difficulty": 3}
        ])
    return result

def extract_skill_points(task: str, position_name: str) -> List[Dict[str, Any]]:
    result = []
    if "电池" in task or "拆装" in task:
        result.extend([
            {"skill_id": "s001", "skill_name": "电池包拆装", "category": "操作技能", "proficiency_level": 4},
            {"skill_id": "s002", "skill_name": "高压安全操作", "category": "安全技能", "proficiency_level": 5},
            {"skill_id": "s003", "skill_name": "万用表使用", "category": "工具技能", "proficiency_level": 3},
            {"skill_id": "s006", "skill_name": "工具使用", "category": "工具技能", "proficiency_level": 2}
        ])
    if "机器人" in task or "编程" in task:
        result.extend([
            {"skill_id": "s004", "skill_name": "机器人示教", "category": "操作技能", "proficiency_level": 4},
            {"skill_id": "s005", "skill_name": "故障诊断", "category": "综合技能", "proficiency_level": 4}
        ])
    return result

def generate_task_steps(task: str) -> List[Dict[str, Any]]:
    if "电池包拆装" in task:
        return [
            {"step_number": 1, "step_name": "安全准备", "step_description": "穿戴绝缘手套、安全帽，设置警示标识", "duration_minutes": 10, "tools_required": ["绝缘手套", "安全帽"], "safety_notes": ["确保工作区域无杂物", "断开车辆电源"]},
            {"step_number": 2, "step_name": "断开高压连接", "step_description": "按照安全规范断开高压系统连接", "duration_minutes": 15, "tools_required": ["绝缘工具", "万用表"], "safety_notes": ["确认高压断电", "等待电容放电"]},
            {"step_number": 3, "step_name": "拆卸固定螺栓", "step_description": "使用扳手拆卸电池包固定螺栓", "duration_minutes": 20, "tools_required": ["扳手", "套筒"], "safety_notes": ["按对角线顺序拆卸"]},
            {"step_number": 4, "step_name": "断开连接线束", "step_description": "逐一断开电池包连接线束", "duration_minutes": 25, "tools_required": ["端子拔取器"], "safety_notes": ["做好线束标记"]},
            {"step_number": 5, "step_name": "吊取电池包", "step_description": "使用专用吊具将电池包移出", "duration_minutes": 30, "tools_required": ["吊具", "起重机"], "safety_notes": ["确保吊具载荷足够", "平稳操作"]},
            {"step_number": 6, "step_name": "检查与清洁", "step_description": "检查电池包外观，清洁安装面", "duration_minutes": 15, "tools_required": ["清洁剂", "抹布"], "safety_notes": ["避免液体进入接口"]},
            {"step_number": 7, "step_name": "安装电池包", "step_description": "按相反顺序安装电池包", "duration_minutes": 30, "tools_required": ["吊具", "扳手"], "safety_notes": ["按规定扭矩紧固螺栓"]},
            {"step_number": 8, "step_name": "功能测试", "step_description": "连接电源，测试充电和放电功能", "duration_minutes": 25, "tools_required": ["万用表", "诊断仪"], "safety_notes": ["逐步恢复供电"]}
        ]
    elif "机器人" in task or "示教" in task:
        return [
            {"step_number": 1, "step_name": "设备检查", "step_description": "检查机器人本体和周边安全设施", "duration_minutes": 10, "tools_required": ["点检表"], "safety_notes": ["确认急停按钮有效"]},
            {"step_number": 2, "step_name": "进入示教模式", "step_description": "将机器人切换至示教模式", "duration_minutes": 5, "tools_required": ["示教器"], "safety_notes": ["确保安全门关闭"]},
            {"step_number": 3, "step_name": "创建程序", "step_description": "在示教器上创建新程序", "duration_minutes": 10, "tools_required": ["示教器"], "safety_notes": ["选择合适的坐标系"]},
            {"step_number": 4, "step_name": "示教点位", "step_description": "手动移动机器人记录关键点位", "duration_minutes": 30, "tools_required": ["示教器"], "safety_notes": ["低速操作，注意周边"]},
            {"step_number": 5, "step_name": "设置运动参数", "step_description": "设置各轴运动速度和加速度", "duration_minutes": 15, "tools_required": ["示教器"], "safety_notes": ["从低速开始"]},
            {"step_number": 6, "step_name": "程序调试", "step_description": "试运行程序并调整参数", "duration_minutes": 25, "tools_required": ["示教器"], "safety_notes": ["全程监控运行状态"]},
            {"step_number": 7, "step_name": "安全验证", "step_description": "验证安全区域和限位保护", "duration_minutes": 15, "tools_required": ["示教器"], "safety_notes": ["测试急停功能"]},
            {"step_number": 8, "step_name": "保存程序", "step_description": "保存程序并备份", "duration_minutes": 5, "tools_required": ["示教器", "U盘"], "safety_notes": ["确认程序完整性"]}
        ]
    else:
        return [
            {"step_number": 1, "step_name": "任务准备", "step_description": "了解任务要求，准备所需工具", "duration_minutes": 10, "tools_required": [], "safety_notes": []},
            {"step_number": 2, "step_name": "执行操作", "step_description": "按照规范执行任务操作", "duration_minutes": 60, "tools_required": [], "safety_notes": []},
            {"step_number": 3, "step_name": "质量检查", "step_description": "检查任务完成质量", "duration_minutes": 15, "tools_required": [], "safety_notes": []},
            {"step_number": 4, "step_name": "整理收尾", "step_description": "清理工作现场，记录工作情况", "duration_minutes": 10, "tools_required": [], "safety_notes": []}
        ]

def match_training_resources(task: str, major_name: str) -> List[Dict[str, Any]]:
    result = []
    if "电池" in task or "新能源" in task:
        result.extend([
            {"resource_id": "r001", "resource_name": "新能源汽车电池包结构微课", "resource_type": "微课", "resource_url": "https://example.com/battery-course", "description": "讲解电池包结构的教学视频"},
            {"resource_id": "r002", "resource_name": "高压安全操作仿真", "resource_type": "仿真软件", "resource_url": "https://example.com/hv-simulator", "description": "高压安全操作模拟训练软件"},
            {"resource_id": "r003", "resource_name": "电池拆装实操指导", "resource_type": "实训指导", "resource_url": "https://example.com/battery-guide", "description": "电池包拆装实操详细指导"}
        ])
    if "机器人" in task or "编程" in task:
        result.extend([
            {"resource_id": "r004", "resource_name": "机器人示教编程微课", "resource_type": "微课", "resource_url": "https://example.com/robot-course", "description": "工业机器人示教编程教学视频"},
            {"resource_id": "r005", "resource_name": "机器人仿真平台", "resource_type": "仿真软件", "resource_url": "https://example.com/robot-simulator", "description": "工业机器人仿真训练平台"}
        ])
    return result

def generate_learning_task(task: str, position_name: str, major_name: str) -> Dict[str, Any]:
    task_steps = generate_task_steps(task)
    knowledge_points = extract_knowledge_points(task, position_name)
    skill_points = extract_skill_points(task, position_name)
    resources = match_training_resources(task, major_name)
    
    work_context = f"在{position_name}岗位工作场景中，需要完成{task}任务，培养学生实际操作能力和问题解决能力。"
    
    safety_points = []
    for step in task_steps:
        safety_points.extend(step.get("safety_notes", []))
    
    estimated_duration = sum(step.get("duration_minutes", 0) for step in task_steps)
    
    return {
        "task_id": f"task_{hash(task)}",
        "task_name": f"【教学任务】{task}",
        "original_task": task,
        "work_context": work_context,
        "target_position": position_name,
        "target_major": major_name,
        "task_objectives": [
            f"掌握{task}的基本操作流程",
            f"理解相关安全规范和操作要点",
            f"具备独立完成{task}的能力",
            f"培养问题分析和故障排除能力"
        ],
        "task_steps": task_steps,
        "safety_points": list(set(safety_points)),
        "knowledge_points": knowledge_points,
        "skill_points": skill_points,
        "training_resources": resources,
        "estimated_duration_minutes": estimated_duration
    }