import os
from configparser import ConfigParser

# Path relative to this uiconfigfile.py module
DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uiconfigfile.ini")


class Config:
    def __init__(self, config_file=DEFAULT_CONFIG_PATH):
        self.config = ConfigParser()
        if not os.path.exists(config_file):
            raise FileNotFoundError(f"Config file missing at: {config_file}")
        self.config.read(config_file)

    def get_llm_options(self):
        value = self.config["DEFAULT"].get("LLM_OPTIONS", "")
        return [opt.strip() for opt in value.split(",") if opt.strip()] if value else []
    
    def get_usecase_options(self):
        value = self.config["DEFAULT"].get("USECASE_OPTIONS", "")
        return [opt.strip() for opt in value.split(",") if opt.strip()] if value else []

    def get_groq_model_options(self):
        value = self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS", "")
        return [opt.strip() for opt in value.split(",") if opt.strip()] if value else []
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE", "LangGraph: Build Stateful Agentic AI graph")
    
