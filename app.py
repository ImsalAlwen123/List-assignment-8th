# Question 1
foods = ["Burger", "Pizza", "Fries", "Broast", "Sandwich"]

print(foods[0])
print(foods[-1])

foods[2] = "pasta"
foods.append("zinger")
foods.insert(2, "Shawarma")
foods.remove("Pizza")
foods.pop()

print(len(foods))
print(foods[0:3])
print(foods[-1:-3])

foods.reverse()
foods.sort()

print(foods)


# Question 2
students = ["Ali", "Sara", "Ahmed", "Zoha Khan", "Hira"]

print(students[1])
print(students[-1])

students[2] = "Hamza"
students.append("Fatima")
students.insert(1, "Ayesha")
students.remove("Sara")
students.pop(1)

print(students)
print(students[1:4])

students.reverse()
print(students)


# Question 3
prices = [45000, 120000, 30000, 85000, 60000]

print()
prices.sort()
print(prices)
print(prices[-1])
print(min(prices))

prices.sort()
print(prices)

prices.sort(reverse=True)
print(prices)

prices.append(50000)
prices.remove(30000)
prices.pop()

print(prices[:3])
print(prices[-2])
print([len(prices)])


# Question 4
players = ["Babar", "Rizwan", "Shaheen", "Naseem", "Shadab"]

print(players[0])
print(players[-1])

players[4] = "Imad"
players.append("Fakhar")
players.insert(2, "Haris")
players.remove("Naseem")

print(players[:4])
print(players[-3:])

players.reverse()
print(players)

# Question 5
cart = ["Shoes", "Watch", "Bag", "Laptop", "Bottle"]

print(cart[0])
print(cart[4])

cart[4] = "Headphones"
cart.append("Keyboard")
cart.insert(1, "Mouse")
cart.remove("Bag")
cart.pop(-1)

print(cart)
print(len(cart))
print(cart[1:4])

cart.reverse()
print(cart)


# Question 6
salaries = [25000, 40000, 70000, 55000, 90000]

print(max(salaries))
print(min(salaries))

salaries.sort()
salaries.append(60000)
salaries.remove(40000)
salaries.sort(reverse=True)

print(salaries[1])
print(salaries[:3])
print(len(salaries))
print(salaries)

# Question 7
movies = ["Avatar", "Inception", "Joker", "Titanic", "Interstellar"]

print(movies[0])

movies[2] = "Batman"
movies.append("kick")
movies.insert(3, "Baaghi")
movies.remove("Titanic")
movies.pop(-1)

print(movies[0:4])

movies.reverse()
print(movies)


# Question 8
marks = [78, 45, 90, 66, 82]

print(max(marks))
print(min(marks))

marks.sort()
marks.append(85)
marks.remove(45)
marks.sort(reverse=True)

print(marks[-2])
print(len(marks))
print(marks)

# Question 9
visitors = ["Ali", "Sara", "Ahmed", "Zoha Khan", "Hira"]

print(visitors[0])
print(visitors[4])

visitors.append("Neha")
visitors.insert(2, "Rohan")
visitors.remove("Ahmed")
visitors.pop(1)

print(visitors[0:3])
print(visitors[-1:-3])

visitors.reverse()
print(len(visitors))


# Question 10
languages = ["Python", "JavaScript", "Java", "C++", "PHP"]

print(languages[0])
print(languages[-1])

languages[4] = "TypeScript"
languages.append("Go")
languages.insert(2, "Rust")
languages.remove("Java")

print(languages[4:])
print(languages[-2:])

languages.sort()
languages.reverse()

print(languages)