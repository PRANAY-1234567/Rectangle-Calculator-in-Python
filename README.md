# ▭ Rectangle Calculator in Python (OOP)

## 📌 Description

This Python program demonstrates how to calculate the **area** and **perimeter** of a rectangle using **Object-Oriented Programming (OOP)**. It takes user input for length and breadth and performs calculations.

---

## 🚀 Features

* Defines a `Rectangle` class
* Takes user input for dimensions
* Calculates:

  * Area
  * Perimeter
* Displays results clearly

---

## 🛠️ How It Works

1. A class `Rectangle` is created with attributes:

   * `length`
   * `breadth`

2. Methods:

   * `input()` → Takes length and breadth from user
   * `area()` → Calculates:

     * `area = length × breadth`
   * `perimeter()` → Calculates:

     * `perimeter = 2 × (length + breadth)`

3. In the main program:

   * Object `rect` is created
   * Input is taken
   * Area and perimeter are calculated and displayed

---

## 💻 Code

```python id="p7x3mz"
class Rectangle:
    def __init__(self):
        self.length = 0.0
        self.breadth = 0.0

    def input(self):
        self.length = float(input("Enter the length : "))
        self.breadth = float(input("Enter the breadth : "))

    def area(self):
        a = self.length * self.breadth
        print("Area of rectangle :", a)

    def perimeter(self):
        p = 2 * (self.length + self.breadth)
        print("Perimeter of rectangle :", p)


# Main program
rect = Rectangle()
rect.input()
rect.area()
rect.perimeter()
```

---

## ▶️ Example Output

```id="k2d9pl"
Enter the length : 10
Enter the breadth : 5
Area of rectangle : 50.0
Perimeter of rectangle : 30.0
```

---

## 📚 Concepts Used

* Class and Object
* User input (`input()`)
* Type casting (`float`)
* Arithmetic operations

---

## 🎯 Use Case

This program helps beginners understand:

* How real-world shapes can be modeled using classes
* How to take input and perform calculations

---

## 🔧 Future Improvements

* Add validation (length and breadth should be positive)
* Add method to check square (`length == breadth`)
* Return values instead of printing
* Create menu-driven program
* 
---

## 📄 License

This project is open-source and free to use.

<img width="1386" height="779" alt="image" src="https://github.com/user-attachments/assets/13157eb9-c88c-4e80-90a3-36982b95f7db" />
