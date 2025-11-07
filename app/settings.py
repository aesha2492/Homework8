from pydantic import BaseModel

class AppSettings(BaseModel):
    app_name: str = "FastAPI Calculator"
    log_level: str = "INFO"

settings = AppSettings()