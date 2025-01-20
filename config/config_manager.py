import os
from app_config import DevelopmentConfig, ProductionConfig

def get_config():
    env = os.getenv("ENV", "development")
    if env == "production":
        return ProductionConfig
    return DevelopmentConfig