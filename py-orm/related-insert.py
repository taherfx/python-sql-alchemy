from index import session, Customers, Invoices

# c1 = Customers(name = "taher kathiriya", address="kalupur bridge, ahmedabad", email="taher@htree.plus")

# c1.invoices = [Invoices(invno=10, amount=15000), Invoices(invno=20, amount=25000)]

c1 = [
   Customers(
      name = "Govind Pant", 
      address = "Gulmandi Aurangabad",
      email = "gpant@gmail.com",
      invoices = [Invoices(invno = 3, amount = 10000), 
      Invoices(invno = 4, amount = 5000)]
   )
]


session.add_all(c1)
session.commit()
