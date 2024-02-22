from ast import Try
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_hostname: str = "localhost"
    database_port: str = "5432"
    database_password: str = "Bunnygrewal222"
    database_name: str = "fastapi"
    database_username: str = "postgres"
    secret_key: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    algorithm: str = "HS256"
    accees_token_expire_minutes: int = 30

    model_config = SettingsConfigDict(env_file=".env")


    # class Config:
    #     env_file = ".env"

settings = Settings()


# Try
# from pydantic_settings import BaseSettings, SettingsConfigDict
# from dotenv import find_dotenv, load_dotenv

# load_dotenv(find_dotenv(".env"))

# class Config(BaseSettings):
#     ...
    
#     model_config = SettingsConfigDict(case_sensitive=True)