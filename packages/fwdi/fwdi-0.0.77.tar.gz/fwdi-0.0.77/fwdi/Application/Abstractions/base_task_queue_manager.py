from abc import ABCMeta, abstractmethod
from ...Application.TaskManager.job_task import JobTask
from ...Application.TaskManager.task_queue_item import TaskQueueItem

class BaseTaskQueueManager(metaclass=ABCMeta):
    @abstractmethod
    def add_queue(self, name:str)->TaskQueueItem | None:
        ...
    
    @abstractmethod
    def add_task(self, task: JobTask, pull_name:str)->JobTask | None:
        ...