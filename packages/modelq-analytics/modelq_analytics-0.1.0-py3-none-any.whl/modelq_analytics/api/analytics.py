from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.responses import HTMLResponse
import uvicorn
import json

class Analytics:
    """
    A small FastAPI-based API for ModelQ-like data, encapsulated in a class.
    """

    def __init__(self, redis_client):
        """
        :param redis_client: an existing Redis instance
        """
        self.redis = redis_client

        # Create the FastAPI app
        self.app = FastAPI(title="ModelQ Dashboard (API Only)")

        # Create a router to group our /api endpoints
        api_router = APIRouter()

        # ---- API Endpoints ----

        @api_router.get("/")
        def root():
            return {"message": "Welcome to the ModelQ Analytics API!"}

        @api_router.get("/task/{task_id}")
        def get_task_by_id(task_id: str):
            task_key = f"task:{task_id}"
            data = self.redis.get(task_key)
            if not data:
                raise HTTPException(status_code=404, detail="Task not found")
            task_data = json.loads(data)

            # Check if there is a separate "task_result:{task_id}"
            result_key = f"task_result:{task_id}"
            result_data = self.redis.get(result_key)
            if result_data:
                task_data["full_result"] = json.loads(result_data)

            return task_data

        @api_router.get("/queue_stats")
        def queue_stats():
            queued_count = self.redis.scard("queued_tasks") or 0
            processing_count = self.redis.scard("processing_tasks") or 0
            ml_tasks_count = self.redis.llen("ml_tasks") or 0

            return {
                "queued_count": queued_count,
                "processing_count": processing_count,
                "ml_tasks_count": ml_tasks_count
            }

        @api_router.get("/workers")
        def worker_statuses():
            servers_data = {}
            server_keys = self.redis.hkeys("servers")
            for server_id in server_keys:
                val = self.redis.hget("servers", server_id)
                if val:
                    servers_data[server_id] = json.loads(val)
            return servers_data

        # Add the router to the main FastAPI application
        # All API endpoints are prefixed with /api
        self.app.include_router(api_router, prefix="/api")

        # ---- Webpage Endpoint (returns HTML) ----
        @self.app.get("/", response_class=HTMLResponse)
        def dashboard():
            return """
<!DOCTYPE html>
<html>
  <head>
    <title>ModelQ Dashboard</title>
    <meta charset="UTF-8" />
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 2rem;
      }
      h1, h2 {
        color: #333;
      }
      .section {
        margin-bottom: 2rem;
      }
      textarea {
        width: 100%;
        height: 200px;
      }
    </style>
  </head>
  <body>
    <h1>ModelQ Dashboard</h1>
    
    <!-- Section: Task Lookup -->
    <div class="section">
      <h2>Task Lookup</h2>
      <input type="text" id="task_id" placeholder="Enter task ID" />
      <button onclick="getTask()">Search</button>
      <br /><br />
      <label>Task Data:</label><br />
      <textarea id="task_data" readonly></textarea>
    </div>

    <!-- Section: Queue Stats -->
    <div class="section">
      <h2>Queue Stats</h2>
      <pre id="queue_stats">(Loading...)</pre>
    </div>

    <!-- Section: Workers -->
    <div class="section">
      <h2>Workers</h2>
      <pre id="workers">(Loading...)</pre>
    </div>

    <script>
      // 1) Task Lookup
      async function getTask() {
        const taskId = document.getElementById("task_id").value.trim();
        if (!taskId) {
          alert("Please enter a task ID.");
          return;
        }
        document.getElementById("task_data").value = "Searching...";

        try {
          const response = await fetch("/api/task/" + taskId);
          if (!response.ok) {
            document.getElementById("task_data").value = "Task not found or error fetching data.";
            return;
          }
          const data = await response.json();
          // Pretty-print JSON in the textarea
          document.getElementById("task_data").value = JSON.stringify(data, null, 2);
        } catch (err) {
          document.getElementById("task_data").value = "Error: " + err.toString();
        }
      }

      // 2) Get Queue Stats
      async function getQueueStats() {
        try {
          const response = await fetch("/api/queue_stats");
          const data = await response.json();
          document.getElementById("queue_stats").textContent = JSON.stringify(data, null, 2);
        } catch (err) {
          document.getElementById("queue_stats").textContent = "Error: " + err.toString();
        }
      }

      // 3) Get Worker Info
      async function getWorkers() {
        try {
          const response = await fetch("/api/workers");
          const data = await response.json();
          document.getElementById("workers").textContent = JSON.stringify(data, null, 2);
        } catch (err) {
          document.getElementById("workers").textContent = "Error: " + err.toString();
        }
      }

      // On page load, fetch queue stats and worker info
      window.addEventListener('load', () => {
        getQueueStats();
        getWorkers();
      });
    </script>
  </body>
</html>
"""

    def serve(self):
        uvicorn.run(self.app, host="0.0.0.0", port=5566)