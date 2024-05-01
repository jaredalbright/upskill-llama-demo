import os
from langchain_community.llms import Ollama
from crewai import Agent, Task, Crew, Process

os.environ['OPENAI_API_BASE'] = 'https://api.groq.com/openai/v1'
os.environ['OPENAI_MODEL_NAME'] = 'llama3-8b-8192'
os.environ['OPENAI_API_KEY'] = ''


model = Ollama(model = "llama3")

classifier = Agent(
    role = "career planner",
    goal = "create a multi-step plan to help advance a software engineer's career given their dream job and current skills. This plan should give immediate steps that involve specific relevant technologies as well as longterm goals that are technology agnostic to account for the rapidly changing tech climate",
    backstory = "you are a staff engineer and mentor to a junior engineer who is looking to upskill and become a 10x engineer",
    verbose = True,
    allow_delegation = False,
)

goal_string = "Senior Distributed Systems Engineer"

skills = "python, AWS, GCP, big data, Apache Spark, Javascript"

create_career_plan = Task(
    description = f"Give a career plan to become {goal_string}, the engineer's current skills are {skills}",
    agent = classifier,
    expected_output = "A plan with 5-10 steps to become the career goal. This plan can focus on strenghtening current skills if relevant or focus on building new ones"
)

crew = Crew(
    agents = [classifier],
    tasks = [create_career_plan],
    verbose = 2,
    process = Process.sequential
)

output = crew.kickoff()

print(output)