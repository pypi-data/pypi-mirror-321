import contextlib
import inspect

from .state import BlocksState

class TaskClass:

    def __init__(self, func, state: BlocksState):
        self.func = func
        self.state = state
        self.source_code = inspect.getsource(func)
        self.name = func.__name__

    @staticmethod
    def get_decorator(state: BlocksState):
        def set_task(func, task_args=None, task_kwargs=None):
            new_task = TaskClass(func, state)
            
            is_function_already_wrapped_in_decorator = False
            
            def run(*args, **kwargs):
                return func(*args, **kwargs)

            # In case trigger decorator was applied before job decorator
            with contextlib.suppress(AttributeError):
                if func.trigger_metadata:
                    trigger_metadata = func.trigger_metadata
                    trigger_kwargs = trigger_metadata.get("trigger_kwargs")
                    function_name = trigger_metadata.get("function_name")
                    function_source_code = trigger_metadata.get("function_source_code")
                    trigger_alias = trigger_metadata.get("trigger_alias")

                    state.automations.append({
                        "trigger_alias": trigger_alias,
                        "function_name": function_name,
                        "function_source_code": function_source_code,
                        "parent_type": "task",
                        "trigger_kwargs": trigger_kwargs,
                        "task_kwargs": task_kwargs
                    })

                    is_function_already_wrapped_in_decorator = True

            if not is_function_already_wrapped_in_decorator:
                run.task_metadata = {
                    "type": "task",
                    "function_name": new_task.name,
                    "function_source_code": new_task.source_code,
                    "task_kwargs": task_kwargs
                }
            return run

        def decorator(*decorator_args, **decorator_kwargs):
            # If decorator is used without parentheses
            if len(decorator_args) == 1 and callable(decorator_args[0]) and not decorator_kwargs:
                return set_task(decorator_args[0])
            
            # If decorator is used with parentheses
            def wrapper(func):
                # Store any args passed to decorator for future use if needed
                return set_task(func, task_args=decorator_args, task_kwargs=decorator_kwargs)
            return wrapper

        decorator.blocks_state = state
        return decorator

