from pydantic import BaseModel


class Settings(BaseModel):
    MOD_CAPTURE_WINDOW: bool = False


s = Settings()
