
from faker import Faker

fake = Faker()
print('--------------',fake.profile())
name = fake.name()
email = fake.email()
address = fake.address()

print(email)
print(address)
print(name)


# Print random sentences
print(fake.sentence())

# List has words that we want in our sentence
word_list = ["GFG", "Python",
             "shaurya", "says", "Gfg",
             "GEEKS"]

# Let's print 5 sentences that
# have words from our word_list
for i in range(0, 5):
    # You need to use ext_word_list = listnameyoucreated
    print(fake.sentence(ext_word_list=word_list))



list = [1,2,3,4,5,6]

for i in list:
    list.remove(i)

print(list)
