# -*- coding: utf-8 -*-
from typing import Dict, Any
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    from langchain_openai import ChatOpenAI
    
    deepseek_key = os.getenv("DEEPSEEK_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")
    
    if deepseek_key and deepseek_key != "${DEEPSEEK_API_KEY}" and deepseek_key.strip():
        return ChatOpenAI(
            model="deepseek-chat",
            api_key=deepseek_key,
            base_url="https://api.deepseek.com/v1",
            temperature=0.7
        )
    elif openai_key and openai_key != "your-api-key-here" and openai_key.strip():
        return ChatOpenAI(
            model="gpt-3.5-turbo",
            api_key=openai_key,
            temperature=0.7
        )
    return None

def parse_user_query(state: Dict[str, Any]) -> Dict[str, Any]:
    user_query = state.get("user_query", "")
    
    llm = get_llm()
    
    if llm:
        try:
            from langchain.prompts import ChatPromptTemplate
            
            prompt = ChatPromptTemplate.from_messages([
                ("system", "你是一个岗位任务分析专家。请分析用户输入的任务描述，提取关键信息。"),
                ("human", "分析以下任务描述，提取：1) 任务名称 2) 所属岗位 3) 所属专业 4) 任务类型。\n\n任务描述：{query}")
            ])
            
            chain = prompt | llm
            response = chain.invoke({"query": user_query})
            result = response.content
            lines = result.strip().split('\n')
            parsed = {}
            for line in lines:
                if '任务名称' in line:
                    parsed['task_name'] = line.split('：')[1].strip() if '：' in line else line.split(':')[1].strip()
                elif '所属岗位' in line:
                    parsed['position_name'] = line.split('：')[1].strip() if '：' in line else line.split(':')[1].strip()
                elif '所属专业' in line:
                    parsed['major_name'] = line.split('：')[1].strip() if '：' in line else line.split(':')[1].strip()
                elif '任务类型' in line:
                    parsed['task_type'] = line.split('：')[1].strip() if '：' in line else line.split(':')[1].strip()
            
            return {
                **state,
                "original_task": parsed.get('task_name', user_query),
                "position_data": {"position_name": parsed.get('position_name', '')},
                "major_data": {"major_name": parsed.get('major_name', '')},
                "workflow_stage": "parsed"
            }
        except Exception as e:
            pass
    
    return parse_user_query_fallback(user_query, state)

def parse_user_query_fallback(user_query: str, state: Dict[str, Any]) -> Dict[str, Any]:
    position_name = ""
    major_name = ""
    
    if "新能源" in user_query or "电池" in user_query:
        position_name = "新能源汽车维修技师"
        major_name = "新能源汽车技术"
    elif "机器人" in user_query or "示教" in user_query:
        position_name = "工业机器人操作员"
        major_name = "工业机器人技术"
    
    return {
        **state,
        "original_task": user_query,
        "position_data": {"position_name": position_name},
        "major_data": {"major_name": major_name},
        "workflow_stage": "parsed"
    }

def analyze_task_requirements(state: Dict[str, Any]) -> Dict[str, Any]:
    original_task = state.get("original_task", "")
    position_name = state.get("position_data", {}).get("position_name", "")
    
    llm = get_llm()
    
    if llm:
        try:
            from langchain.prompts import ChatPromptTemplate
            
            prompt = ChatPromptTemplate.from_messages([
                ("system", "你是一个职业教育课程设计专家。请分析企业任务的教学转化需求。"),
                ("human", "分析任务：{task}，针对岗位：{position}。请输出：1) 教学目标 2) 核心知识点 3) 核心技能点 4) 安全注意事项。")
            ])
            
            chain = prompt | llm
            response = chain.invoke({"task": original_task, "position": position_name})
            analysis_result = {
                "analysis_completed": True,
                "llm_analysis": response.content
            }
            return {
                **state,
                "analysis_result": analysis_result,
                "workflow_stage": "analyzed"
            }
        except Exception as e:
            pass
    
    return {
        **state,
        "analysis_result": {"analysis_completed": False, "message": "使用本地规则分析"},
        "workflow_stage": "analyzed"
    }

def generate_learning_task(state: Dict[str, Any]) -> Dict[str, Any]:
    from .tools import generate_learning_task as tool_generate_task
    
    original_task = state.get("original_task", "")
    position_name = state.get("position_data", {}).get("position_name", "")
    major_name = state.get("major_data", {}).get("major_name", "")
    
    if not position_name:
        position_name = "新能源汽车维修技师"
    if not major_name:
        major_name = "新能源汽车技术"
    
    learning_task = tool_generate_task(original_task, position_name, major_name)
    
    return {
        **state,
        "learning_task": learning_task,
        "workflow_stage": "generated"
    }

def format_output(state: Dict[str, Any]) -> Dict[str, Any]:
    learning_task = state.get("learning_task", {})
    
    if not learning_task:
        return {
            **state,
            "workflow_stage": "completed",
            "final_output": "无法生成学习任务，请检查输入参数。"
        }
    
    output_lines = []
    output_lines.append("=" * 60)
    output_lines.append(f"【学习任务卡】{learning_task.get('task_name', '')}")
    output_lines.append("=" * 60)
    
    output_lines.append("\n一、任务信息")
    output_lines.append(f"原任务名称：{learning_task.get('original_task', '')}")
    output_lines.append(f"目标岗位：{learning_task.get('target_position', '')}")
    output_lines.append(f"目标专业：{learning_task.get('target_major', '')}")
    output_lines.append(f"预计时长：{learning_task.get('estimated_duration_minutes', 0)}分钟")
    
    output_lines.append("\n二、工作情境")
    output_lines.append(f"{learning_task.get('work_context', '')}")
    
    output_lines.append("\n三、任务目标")
    for i, objective in enumerate(learning_task.get('task_objectives', []), 1):
        output_lines.append(f"{i}. {objective}")
    
    output_lines.append("\n四、分步操作指南")
    for step in learning_task.get('task_steps', []):
        output_lines.append(f"\n步骤{step.get('step_number', '')}：{step.get('step_name', '')}")
        output_lines.append(f"    描述：{step.get('step_description', '')}")
        output_lines.append(f"    时长：{step.get('duration_minutes', 0)}分钟")
        if step.get('tools_required'):
            output_lines.append(f"    工具：{', '.join(step.get('tools_required', []))}")
        if step.get('safety_notes'):
            output_lines.append(f"    安全要点：{', '.join(step.get('safety_notes', []))}")
    
    output_lines.append("\n五、安全要点汇总")
    for i, point in enumerate(learning_task.get('safety_points', []), 1):
        output_lines.append(f"{i}. {point}")
    
    output_lines.append("\n六、知识点匹配")
    for kp in learning_task.get('knowledge_points', []):
        output_lines.append(f"• {kp.get('knowledge_name', '')}（{kp.get('category', '')}，难度：{kp.get('difficulty', 3)}）")
    
    output_lines.append("\n七、技能点匹配")
    for sp in learning_task.get('skill_points', []):
        output_lines.append(f"• {sp.get('skill_name', '')}（{sp.get('category', '')}，熟练度：{sp.get('proficiency_level', 3)}）")
    
    output_lines.append("\n八、关联实训资源")
    for resource in learning_task.get('training_resources', []):
        output_lines.append(f"【{resource.get('resource_type', '')}】{resource.get('resource_name', '')}")
        output_lines.append(f"    链接：{resource.get('resource_url', '')}")
        output_lines.append(f"    说明：{resource.get('description', '')}")
    
    output_lines.append("\n" + "=" * 60)
    output_lines.append("学习任务卡生成完成")
    output_lines.append("=" * 60)
    
    final_output = "\n".join(output_lines)
    
    return {
        **state,
        "workflow_stage": "completed",
        "final_output": final_output
    }

def decide_next_step(state: Dict[str, Any]) -> str:
    stage = state.get("workflow_stage", "start")
    
    if stage == "start":
        return "parse"
    elif stage == "parsed":
        return "analyze"
    elif stage == "analyzed":
        return "generate"
    elif stage == "generated":
        return "format"
    elif stage == "completed":
        return "end"
    else:
        return "end"