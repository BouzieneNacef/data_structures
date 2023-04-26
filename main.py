class Persone:

    def __init__(self, name, email, salaire, post):
        self.name = name
        self.email = email
        self.salaire = salaire
        self.post = post

    def __str__(self):
        return f'{self.name}\n{self.email}\n{self.salaire}\n{self.post}'

p1 = Persone('Nacef', 'nacef.bouza@gmaol.com', 1200, 'engineer')

print(p1)

class Empoyee(Persone):

    def __init__(self, name, email, salaire, post, age):
        super().__init__(name, email, salaire, post)
        self.age = age
    def __str__(self):
        return super().__str__()

p2 = Empoyee('ahmed', 'ahmed.hhdg@gmail.com', 1500, 'developer',25 )
print(p2)

    
