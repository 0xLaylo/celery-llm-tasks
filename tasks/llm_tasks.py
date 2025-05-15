"""
Example: Async LLM tasks with Celery
"""

from celery import Celery

app = Celery('llm_tasks', broker='redis://localhost:6379/0')

@app.task
def process_llm_request(prompt: str):
    """Process LLM request asynchronously"""
    # LLM processing logic
    return f"Processed: {prompt}"

@app.task
def batch_process_llm(requests: list):
    """Batch process LLM requests"""
    results = []
    for req in requests:
        result = process_llm_request.delay(req)
        results.append(result)
    return results

