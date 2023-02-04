import unittest  # Importing the unittest, an automated test-library.


def classify_triangle(a, b, c):  # defining classify_triangle() function that accepts three parameters # validating type of triangles
    if a == b and b == c and a == c:  # validating if the three sides are equal
        return 'Equilateral'
    elif a == b or b == c or a == c:  # validating if any two of the three sides are equal
        return 'Isosceles'
    elif a != b != c:  # validating if none of the sides are equal
        return 'Scalene'


def right_angled(a, b, c):
    if (a * a) + (b * b) == (c * c):
        return 'Right-angled'

class TestTriangle(unittest.TestCase):

    # Validating the test cases for different types of triangles
    def test_triangle(self):
        self.assertEqual(classify_triangle(6, 6, 6), 'Equilateral')
        self.assertEqual(classify_triangle(5, 5, 7), 'Isosceles')
        self.assertEqual(classify_triangle(90, 94, 85), 'Scalene')
        self.assertEqual(classify_triangle(6, 9, 9), 'Isosceles')
        self.assertEqual(classify_triangle(3, 1, 2), 'Scalene')
        self.assertEqual(classify_triangle(10, 15, 30), 'Scalene')
        self.assertNotEqual(classify_triangle(19, 9, 9), 'Equilateral')
        self.assertNotEqual(classify_triangle(10, 10, 10), 'Isosceles')

    # Validating the test cases for a right-angled triangle
    def test_right_angled(self):
        self.assertEqual(right_angled(3, 4, 5), 'Right-angled')
        self.assertEqual(right_angled(8, 15, 17), 'Right-angled')
        self.assertEqual(right_angled(9, 12, 15), 'Right-angled')
        self.assertEqual(right_angled(12, 16, 20), 'Right-angled')


a = float(input("Enter value for the side 'a': "))  # To input the values
b = float(input("Enter value for the side 'b': "))
c = float(input("Enter value for the side 'c': "))
print(classify_triangle(a, b, c))  # calling classify_triangle() and printing it
print(right_angled(a, b, c))

if __name__ == '__main__':
    classify_triangle(3,5,6)  # Invoking function calls via main
    right_angled(3,4,5)
    unittest.main(exit=False, verbosity=2)