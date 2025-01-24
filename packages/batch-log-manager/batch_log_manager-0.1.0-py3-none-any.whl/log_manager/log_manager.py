import weakref
from asyncio import Lock

class BatchLogManager:
    _instance = None

    def __new__(cls, injection_manager=None, session_factory=None, max_buffer_size=100):
        if cls._instance is None:
            cls._instance = super(LogManager, cls).__new__(cls)
            cls._instance.logs = {}
            cls._instance._injection_manager = injection_manager  # Strong reference
            cls._instance._session_factory = session_factory  # Strong reference
            cls._instance.max_buffer_size = max_buffer_size
            cls._instance._lock = Lock()

            cls._instance._total

            # Register a finalizer to flush remaining logs
            weakref.finalize(cls._instance, cls._finalize)

        return cls._instance

    @classmethod
    def _finalize(cls):
        """
        Finalizer to ensure remaining logs are flushed when the LogManager is garbage collected.
        """
        try:
            if cls._instance and cls._instance._injection_manager and cls._instance._session_factory:
                import asyncio
                asyncio.run(cls._instance.flush_remaining_logs())
        except Exception as e:
            print(f"Finalizer error: {e}")

    async def add_log(self, key, log_entry):
        """
        Add a log entry under the specified key. Flush if total log count exceeds the threshold.
        """
        async with self._lock:
            if key not in self.logs:
                self.logs[key] = []
            self.logs[key].append(log_entry)
            self._total += 1

            if self._total >= self.max_buffer_size:
                await self.flush_logs()

    async def flush_logs(self):
        """
        Flush all buffered logs to the database using the InjectionManager.
        """
        if not self.logs:
            return

        async with self._session_factory() as session:
            try:
                await self._injection_manager.inject(self.logs, session)
                self.logs.clear()
                self._total = 0
            except Exception as e:
                await session.rollback()
                raise e

    async def flush_remaining_logs(self):
        """
        Ensure any remaining logs are flushed, regardless of the buffer size.
        """
        async with self._lock:
            if self.logs:
                await self.flush_logs()
