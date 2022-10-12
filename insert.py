import db_gen as db
from sqlalchemy.orm import sessionmaker
import random

# new session

Session = sessionmaker(bind=db.engine)
session = Session()

# adding random data 

for t in range(1, 30):
    item_id = random.randint(0, 1000)
    price = random.randint(20, 50)

    tr = db.transactions(t, 2022/10/12, item_id, price)
    session.add(tr)

# save changes in db

session.commit()