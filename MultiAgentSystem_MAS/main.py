from crewai import Agent, Task, LLM
import os
from dotenv import load_dotenv
from crewai import Crew, Process

load_dotenv()

# default_llm = AzureChatOpenAI(
#     openai_api_version=os.environ.get("AZURE_OPENAI_VERSION", "2023-07-01-preview"),
#     azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT", "gpt35"),
#     azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT", "https://<your-endpoint>.openai.azure.com/"),
#     api_key=os.environ.get("AZURE_OPENAI_KEY")
# )

# default_llm = LLM(
#     model="ollama/llama3.2:1b",
#     base_url="http://localhost:11434"
# )

# default_llm = LLM(
#     model=os.getenv('LITELLM_MODEL'),
#     vertex_credentials=os.getenv('GEMINI_API_KEY'),
#     temperature=0.7
# )

default_llm = LLM(
    model="groq/mistral-saba-24b",
    temperature=0.7
)


# Create a researcher agent
researcher = Agent(
  role='Senior Researcher',
  goal='Discover groundbreaking technologies',
  verbose=True,
  llm=default_llm,
  backstory='A curious mind fascinated by cutting-edge innovation and the potential to change the world, you know everything about tech.'
)

# Task for the researcher
research_task = Task(
  description='Identify the next big trend in AI',
  expected_output='5 paragraphs on the next big AI trend',
  agent=researcher  # Assigning the task to the researcher
)


# Instantiate your crew
tech_crew = Crew(
  agents=[researcher],
  tasks=[research_task],
  process=Process.sequential  # Tasks will be executed one after the other
)

# Begin the task execution
tech_crew.kickoff()