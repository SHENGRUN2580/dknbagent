# -*- coding: utf-8 -*-
from langgraph.graph import StateGraph, END
from typing import Dict, Any
from .utils.nodes import parse_user_query, analyze_task_requirements, generate_learning_task, format_output, decide_next_step

class TaskTeachingAgent:
    def __init__(self):
        self.graph = self.build_graph()
    
    def build_graph(self):
        workflow = StateGraph(Dict[str, Any])
        
        workflow.add_node("parse", parse_user_query)
        workflow.add_node("analyze", analyze_task_requirements)
        workflow.add_node("generate", generate_learning_task)
        workflow.add_node("format", format_output)
        
        workflow.set_entry_point("parse")
        
        workflow.add_edge("parse", "analyze")
        workflow.add_edge("analyze", "generate")
        workflow.add_edge("generate", "format")
        workflow.add_edge("format", END)
        
        return workflow.compile()
    
    def run(self, user_query: str) -> str:
        initial_state = {
            "user_query": user_query,
            "workflow_stage": "start"
        }
        
        result = self.graph.invoke(initial_state)
        return result.get("final_output", "任务处理完成")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        task_input = sys.argv[1]
    else:
        task_input = "新能源汽车电池包拆装"
    
    agent = TaskTeachingAgent()
    output = agent.run(task_input)
    print(output)