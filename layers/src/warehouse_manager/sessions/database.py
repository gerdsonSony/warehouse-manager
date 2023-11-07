from sqlalchemy.engine import URL, create_engine
from sqlalchemy.orm import sessionmaker

from warehouse_manager.configs.database import DATABASE_PARAMS

# Warehouse Manager MySQL engine
mysql_engine = create_engine(
    URL.create(
        drivername="mysql+pymysql",
        host=DATABASE_PARAMS["HOST"],
        port=DATABASE_PARAMS["PORT"],
        database=DATABASE_PARAMS["DATABASE"],
        username=DATABASE_PARAMS["USERNAME"],
        password=DATABASE_PARAMS["PASSWORD"],
    )
)

Session = sessionmaker(bind=mysql_engine, expire_on_commit=False)
mysql_session = Session()
