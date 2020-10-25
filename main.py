import sqlite3
import datetime

db = sqlite3.connect("task1.db")
cursor = db.cursor()
cursor.execute("PRAGMA foreign_keys = ON")
transaction_id = 0

cursor.execute('''DROP TABLE IF EXISTS accounts''')
cursor.execute('''DROP TABLE IF EXISTS ledger''')
cursor.execute('''CREATE table accounts (
    _id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    credit INTEGER,
    bankName TEXT)''')

cursor.execute('''CREATE table ledger (
        _id INTEGER PRIMARY KEY AUTOINCREMENT,
        from_id INTEGER,
        to_id INTEGER,
        fee INTEGER,
        amount INTEGER,
        transactionDateTime TEXT,
        FOREIGN KEY (from_id) REFERENCES accounts(_id),
        FOREIGN KEY (to_id) REFERENCES accounts(_id))''')

accounts = [(1, 'Guy 1', 1000, 'SpearBank'), (2, 'Guy 2', 1000, 'Tinkoff'), (3, 'Guy 3', 1000, 'SpearBank'), (4, 'Mr Comission', 0, 'Comissionbank')]
cursor.executemany("INSERT INTO accounts VALUES (?, ?, ?, ?)", accounts)

print("Initial conditions:")

# To print accounts
print("ACCOUNTS table")
cursor.execute("SELECT * FROM accounts")
for acc in cursor.fetchall():
    print(acc)
print()

# To print transactions
print("LEDGER table")
cursor.execute("SELECT * FROM ledger")
for trans in cursor.fetchall():
    print(trans)
print()

# ledger.transfer('Account 1', 'Account 3', 500)
fee = 0
cursor.execute("SELECT credit, bankName FROM accounts WHERE name=?", ['Guy 1'])
res = cursor.fetchall()[0]
credit1 = res[0]
bank1 = res[1]
cursor.execute("SELECT credit, bankName FROM accounts WHERE name=?", ['Guy 3'])
res = cursor.fetchall()[0]
credit2 = res[0]
bank2 = res[1]
if bank1 != bank2:
    fee = 30
if credit1 < (500 + fee):
    print("Not enough moner!")
else:
    if (fee != 0):
        cursor.execute("SELECT credit FROM accounts WHERE name='Mr Comission'")
        fee_credit = cursor.fetchall()[0][0]
        cursor.execute('''UPDATE accounts
                    SET credit = ?1
                    WHERE name = ?2''', (fee_credit + fee, 'Mr Comission'))
    cursor.execute('''UPDATE accounts
        SET credit = ?1
        WHERE name = ?2''', (credit1 - 500 - fee, 'Guy 1'))
    cursor.execute('''UPDATE accounts
        SET credit = ?1
        WHERE name = ?2''', (credit2 + 500, 'Guy 3'))


    cursor.execute("SELECT _id FROM accounts WHERE name=?", ['Guy 1'])
    id1 = cursor.fetchall()[0][0]
    cursor.execute("SELECT _id FROM accounts WHERE name=?", ['Guy 2'])
    id2 = cursor.fetchall()[0][0]
    cursor.execute("INSERT INTO ledger VALUES (?, ?, ?, ?, ?, ?)",
                   (transaction_id, id1, id2, fee, 500, datetime.datetime.now().__str__()))

    transaction_id += 1




# ledger.transfer('Account 2', 'Account 1', 700)
fee = 0
cursor.execute("SELECT credit, bankName FROM accounts WHERE name=?", ['Guy 2'])
res = cursor.fetchall()[0]
credit1 = res[0]
bank1 = res[1]
cursor.execute("SELECT credit, bankName FROM accounts WHERE name=?", ['Guy 1'])
res = cursor.fetchall()[0]
credit2 = res[0]
bank2 = res[1]
if bank1 != bank2:
    fee = 30
if credit1 < (700 + fee):
    print("Not enough moner!")
else:
    if (fee != 0):
        cursor.execute("SELECT credit FROM accounts WHERE name='Mr Comission'")
        fee_credit = cursor.fetchall()[0][0]
        cursor.execute('''UPDATE accounts
                    SET credit = ?1
                    WHERE name = ?2''', (fee_credit + fee, 'Mr Comission'))
    cursor.execute('''UPDATE accounts
        SET credit = ?1
        WHERE name = ?2''', (credit1 - 700 - fee, 'Guy 2'))
    cursor.execute('''UPDATE accounts
        SET credit = ?1
        WHERE name = ?2''', (credit2 + 700, 'Guy 1'))

    cursor.execute("SELECT _id FROM accounts WHERE name=?", ['Guy 2'])
    id1 = cursor.fetchall()[0][0]
    cursor.execute("SELECT _id FROM accounts WHERE name=?", ['Guy 1'])
    id2 = cursor.fetchall()[0][0]
    cursor.execute("INSERT INTO ledger VALUES (?, ?, ?, ?, ?, ?)",
                   (transaction_id, id1, id2, fee, 700, datetime.datetime.now().__str__()))

    transaction_id += 1

# ledger.transfer('Account 2', 'Account 3', 100)
fee = 0
cursor.execute("SELECT credit, bankName FROM accounts WHERE name=?", ['Guy 2'])
res = cursor.fetchall()[0]
credit1 = res[0]
bank1 = res[1]
cursor.execute("SELECT credit, bankName FROM accounts WHERE name=?", ['Guy 3'])
res = cursor.fetchall()[0]
credit2 = res[0]
bank2 = res[1]
if bank1 != bank2:
    fee = 30
if credit1 < (100 + fee):
    print("Not enough moner!")
else:
    if (fee != 0):
        cursor.execute("SELECT credit FROM accounts WHERE name='Mr Comission'")
        fee_credit = cursor.fetchall()[0][0]
        cursor.execute('''UPDATE accounts
                    SET credit = ?1
                    WHERE name = ?2''', (fee_credit + fee, 'Mr Comission'))
    cursor.execute('''UPDATE accounts
        SET credit = ?1
        WHERE name = ?2''', (credit1 - 100 - fee, 'Guy 2'))
    cursor.execute('''UPDATE accounts
        SET credit = ?1
        WHERE name = ?2''', (credit2 + 100, 'Guy 3'))

    cursor.execute("SELECT _id FROM accounts WHERE name=?", ['Guy 2'])
    id1 = cursor.fetchall()[0][0]
    cursor.execute("SELECT _id FROM accounts WHERE name=?", ['Guy 3'])
    id2 = cursor.fetchall()[0][0]
    cursor.execute("INSERT INTO ledger VALUES (?, ?, ?, ?, ?, ?)",
                   (transaction_id, id1, id2, fee, 100, datetime.datetime.now().__str__()))

    transaction_id += 1

print("After operations:")
# To print accounts
print("ACCOUNTS table")
cursor.execute("SELECT * FROM accounts")
for acc in cursor.fetchall():
    print(acc)
print()

# To print transactions
print("LEDGER table")
cursor.execute("SELECT * FROM ledger")
for trans in cursor.fetchall():
    print(trans)
print()