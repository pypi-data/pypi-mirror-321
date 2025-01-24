from typing import Protocol, List, Any

class LoggingOperations(Protocol):
    def log_pre_action(self, action_name: str, **kwargs):
        """Log details before the action begins."""
        pass

    def log_post_action_success(self, action_name: str, **kwargs):
        """Log details after the action completes successfully."""
        pass

    def log_post_action_failure(self, action_name: str, exception: Exception, **kwargs):
        """Log details after the action fails."""
        pass

