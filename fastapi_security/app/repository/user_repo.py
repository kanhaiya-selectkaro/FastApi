from ..models.users import User

async def create_transaction(transaction: TransactionBase, db: db_dependency):
    db_transaction = User.Transaction(**transaction.model_dump())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

async def read_transactions(db: db_dependency, skip: int=0, limit: int=100):
    transactions = db.query(User.Transaction).offset(skip).limit(limit).all()
    return transactions