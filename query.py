import db_gen as db
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=db.engine)
session = Session()

# all data

for s in session.query(db.transactions).all():
    print(s.transaction_id, s.price)

print('*' * 20)
print('Transactions with price over 40:')

#selected data

for s in session.query(db.transactions).filter(db.transactions.price > 40):
    print(s.transaction_id, s.price)