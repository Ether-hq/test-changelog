import gc

class BackgroundWorker:
    def __init__(self):
        self.tasks = []
        self.completed = []
    
    def process_tasks(self):
        """Process background tasks with proper memory cleanup"""
        while self.tasks:
            task = self.tasks.pop(0)
            result = self._execute(task)
            self.completed.append(result)
            
            # Fix: Clear completed tasks periodically to prevent memory leak
            if len(self.completed) > 100:
                self.completed = self.completed[-50:]
                gc.collect()  # Force garbage collection
    
    def _execute(self, task):
        """Execute a single task"""
        return {"task": task, "status": "completed"}
