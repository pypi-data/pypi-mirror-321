import contextlib
import inspect

from .state import BlocksState

class OnClass:

    def __init__(self, func, state: BlocksState):
        self.func = func
        self.state = state
        self.source_code = inspect.getsource(func)
        self.name = func.__name__

    @staticmethod
    def get_decorator(state: BlocksState):
        def set_trigger(func, trigger_alias=None, trigger_kwargs=None):
            new_trigger = OnClass(func, state)
            trigger_kwargs = trigger_kwargs or {}

            is_function_already_wrapped_in_decorator = False

            # Check if the function is already wrapped in a decorator
            with contextlib.suppress(AttributeError):
                if func.task_metadata:
                    function_name = func.task_metadata.get("function_name")
                    parent_type = func.task_metadata.get("type")
                    function_source_code = func.task_metadata.get("function_source_code")
                    task_kwargs = func.task_metadata.get("task_kwargs")
                    
                    state.automations.append({
                        "trigger_alias": trigger_alias,
                        "function_name": function_name,
                        "function_source_code": function_source_code,
                        "parent_type": parent_type,
                        "trigger_kwargs": trigger_kwargs,
                        "task_kwargs": task_kwargs
                    })

                    is_function_already_wrapped_in_decorator = True
            
            if not is_function_already_wrapped_in_decorator:
                func.trigger_metadata = {
                    "type": "trigger",
                    "trigger_alias": trigger_alias,
                    "function_name": new_trigger.name,
                    "function_source_code": new_trigger.source_code,
                    "trigger_kwargs": trigger_kwargs
                }
            
            return func

        def decorator(*decorator_args, **decorator_kwargs):
            # If decorator is used without parentheses
            if len(decorator_args) == 1 and callable(decorator_args[0]) and not decorator_kwargs:
                return set_trigger(decorator_args[0])
            
            # If decorator is used with parentheses
            def wrapper(func):
                return set_trigger(func, decorator_args[0] if decorator_args else None, decorator_kwargs)
            return wrapper
            
        decorator.blocks_state = state
        return decorator
