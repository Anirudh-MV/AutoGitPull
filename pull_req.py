# not really pull request, but just an example

from dulwich.repo import Repo

r = Repo('.')

print(r.head())

c = r[r.head()]

print(c)

print("Message of the commit" + str(c.message))