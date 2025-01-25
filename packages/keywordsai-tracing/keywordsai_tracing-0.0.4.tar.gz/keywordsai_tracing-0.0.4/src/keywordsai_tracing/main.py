from .constants.keywordsai_config import *
from .decorators import workflow, task
from traceloop.sdk import Traceloop
class KeywordsAITelemetry:
    """
    KeywordsAITelemetry initializes and manages OpenTelemetry instrumentation for Keywords AI.
    """
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.tracer = Traceloop()
            self._initialize_telemetry()
            self._initialized = True
    
    def _initialize_telemetry(self):
        """Initialize the Traceloop SDK with Keywords AI configuration"""
        self.tracer.init(
            app_name="keywordsai",
            api_endpoint=KEYWORDSAI_BASE_URL,
            api_key=KEYWORDSAI_API_KEY,
        )
    
    # Expose decorators as instance methods
    workflow = workflow
    task = task
