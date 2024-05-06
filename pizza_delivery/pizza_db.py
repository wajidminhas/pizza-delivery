from sqlmodel import  create_engine, Session
from pizza_delivery import setting


connection_string = str(setting.DATABASE_URL_PIZZA).replace("postgresql", "postgresql+psycopg")


engine = create_engine(connection_string, echo=True, connect_args={"sslmode":"require"},
                       pool_size=10, pool_recycle=300)


def get_session():
    with Session(engine) as session:
        yield session


