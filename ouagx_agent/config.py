import os
from dataclasses import dataclass
from dotenv import load_dotenv
load_dotenv()
@dataclass
class Config:
    provider: str = os.getenv("OUAGX_PROVIDER", "ollama")
    ollama_url: str = os.getenv("OUAGX_OLLAMA_URL", "http://127.0.0.1:11434")
    ollama_model: str = os.getenv("OUAGX_OLLAMA_MODEL", "llama3.2")
    openai_base_url: str = os.getenv("OUAGX_OPENAI_BASE_URL", "https://api.openai.com/v1")
    openai_model: str = os.getenv("OUAGX_OPENAI_MODEL", "")
    api_key: str = os.getenv("OUAGX_API_KEY", "")
    db_path: str = os.getenv("OUAGX_DB", "ouagx_agent.db")
    confirm_write: bool = os.getenv("OUAGX_CONFIRM_WRITE", "true").lower() == "true"
    confirm_privileged: bool = os.getenv("OUAGX_CONFIRM_PRIVILEGED", "true").lower() == "true"
    confirm_dangerous: bool = os.getenv("OUAGX_CONFIRM_DANGEROUS", "true").lower() == "true"
