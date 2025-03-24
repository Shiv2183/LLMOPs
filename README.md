# Multi-Agent System (MAS) Overview

This project demonstrates a Multi-Agent System (MAS) using the `crewai` library to simulate collaborative task execution among agents powered by Large Language Models (LLMs). Below is a detailed explanation of the `main.py` file.

## Key Components

### 1. **Environment Setup**

The script uses environment variables to configure the LLM model and its credentials. These are loaded using the `dotenv` library:

- `LITELLM_MODEL`: Specifies the LLM model to be used.
- `GEMINI_API_KEY`: Provides authentication for the LLM service.

### 2. **Default LLM Configuration**

The `LLM` class is used to define the default language model with the following parameters:

- `model`: The LLM model name, fetched from the `LITELLM_MODEL` environment variable.
- `vertex_credentials`: API key for authentication, fetched from the `GEMINI_API_KEY` environment variable.
- `temperature`: Controls the randomness of the model's output (set to `0.7` for balanced creativity and determinism).

### 3. **Agent Definition**

An agent named `researcher` is created using the `Agent` class:

- **Role**: `Senior Researcher`
- **Goal**: To discover groundbreaking technologies.
- **Verbose Mode**: Enabled for detailed output during execution.
- **Backstory**: Provides context about the agent's expertise and interests.
- **LLM**: The default LLM is assigned to the agent for task execution.

### 4. **Task Creation**

A task named `research_task` is defined using the `Task` class:

- **Description**: `Identify the next big trend in AI`.
- **Expected Output**: A detailed report in 5 paragraphs.
- **Assigned Agent**: The `researcher` agent is responsible for completing this task.

### 5. **Crew Setup**

The `Crew` class is used to manage the agents and tasks:

- **Agents**: Includes the `researcher` agent.
- **Tasks**: Includes the `research_task`.
- **Process**: Tasks are executed sequentially (`Process.sequential`).

### 6. **Task Execution**

The `kickoff` method of the `Crew` class initiates the task execution. The `researcher` agent processes the `research_task` and generates the expected output.

## How It Works

1. The script initializes the environment and configures the LLM.
2. An agent (`researcher`) is created with a specific role, goal, and backstory.
3. A task is defined and assigned to the agent.
4. The `Crew` orchestrates the execution of tasks by the agent.
5. The `kickoff` method starts the process, and the agent uses the LLM to complete the task.

This setup demonstrates how to use the `crewai` library to build a collaborative system where agents powered by LLMs can execute tasks in a structured manner.
