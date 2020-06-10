from PyQt5.QtSql import QSqlDatabase, QSqlQuery

conn = QSqlDatabase.addDatabase('QSQLITE')
conn.setDatabaseName('database.sqlite3')

if conn.open():
    query = QSqlQuery()
    query.exec('select * from vendors')
    results = []
    if query.isActive():
        query.first()
        while query.isValid():
            results.append(query.value('vendor_name'))
            query.next()
        for el in results:
            print(el)
else:
    print(conn.lastError().text())

conn.close()
