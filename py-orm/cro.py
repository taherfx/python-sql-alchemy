from index import session, Customers, Invoices

# s = session.query(Customers).filter(Invoices.custid.__ne__(4))
# s = session.query(Invoices).filter(Invoices.invno.con/tains([3,4]))
s = session.query(Invoices).filter(Invoices.customers.has(name = 'taher kathiriya'))


for i in s:
    print(i.amount)