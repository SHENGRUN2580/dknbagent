from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class IndustryData(BaseModel):
    industry_id: str
    industry_name: str
    description: str
    typical_tasks: List[str] = []

class PositionData(BaseModel):
    position_id: str
    position_name: str
    industry_id: str
    responsibilities: List[str] = []
    required_skills: List[str] = []
    typical_tasks: List[str] = []

class MajorData(BaseModel):
    major_id: str
    major_name: str
    related_positions: List[str] = []
    core_courses: List[str] = []
    training_objectives: List[str] = []

class KnowledgePoint(BaseModel):
    knowledge_id: str
    knowledge_name: str
    category: str
    description: str
    difficulty: int = Field(ge=1, le=5)

class SkillPoint(BaseModel):
    skill_id: str
    skill_name: str
    category: str
    description: str
    proficiency_level: int = Field(ge=1, le=5)

class TaskStep(BaseModel):
    step_number: int
    step_name: str
    step_description: str
    duration_minutes: int
    tools_required: List[str] = []
    safety_notes: List[str] = []
    related_knowledge: List[str] = []
    related_skills: List[str] = []

class TrainingResource(BaseModel):
    resource_id: str
    resource_name: str
    resource_type: str
    resource_url: str
    description: str

class LearningTask(BaseModel):
    task_id: str
    task_name: str
    original_task: str
    work_context: str
    target_position: str
    target_major: str
    task_objectives: List[str] = []
    task_steps: List[TaskStep] = []
    safety_points: List[str] = []
    knowledge_points: List[KnowledgePoint] = []
    skill_points: List[SkillPoint] = []
    training_resources: List[TrainingResource] = []
    estimated_duration_minutes: int = 0

class TaskTeachingState(BaseModel):
    user_query: str = ""
    industry_data: Optional[IndustryData] = None
    position_data: Optional[PositionData] = None
    major_data: Optional[MajorData] = None
    original_task: str = ""
    analysis_result: Dict[str, Any] = {}
    learning_task: Optional[LearningTask] = None
    workflow_stage: str = "start"
    error_message: str = ""