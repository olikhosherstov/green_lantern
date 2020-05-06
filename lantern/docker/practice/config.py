class Config:
    TEST_VALUE = "CONFIG_VALUE"
    PG_USER = "cursor"
    PG_PASSWORD = "very_secret_password"
    PG_HOST = "172.28.1.4"
    PG_PORT = 5433
    DB_NAME = "cursor_sqlalchemy_db"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False