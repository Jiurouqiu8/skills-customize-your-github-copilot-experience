# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using FastAPI. Students will create endpoints for retrieving and creating resources, validate request data, and return JSON responses.

## 📝 Tasks

### 🛠️ Build the API Skeleton

#### Description
Create a FastAPI application with a root endpoint and a data model for tasks.

#### Requirements
Completed program should:

- Create a FastAPI app instance named `app`
- Add a root endpoint at `/` that returns a welcome message
- Define a Pydantic model named `Task` with `id`, `title`, `description`, and `completed` fields

### 🛠️ Add GET and POST Endpoints

#### Description
Add endpoints to retrieve all tasks and create new tasks.

#### Requirements
Completed program should:

- Add a GET endpoint at `/tasks` that returns a list of tasks
- Add a POST endpoint at `/tasks` that accepts a `Task` request body
- Return the created task with a success status

### 🛠️ Add Validation and Error Handling

#### Description
Validate task input and handle cases where task creation fails.

#### Requirements
Completed program should:

- Use FastAPI validation to ensure required fields are present
- Return a descriptive error if the task title is missing or invalid
- Include at least one example of raising `HTTPException`

### 🛠️ (Stretch) Document and Test the API

#### Description
Use FastAPI’s automatic docs and optionally test the endpoints.

#### Requirements
Completed program should:

- Confirm that API docs are available at `/docs`
- Optionally add comments or instructions for running the FastAPI app
