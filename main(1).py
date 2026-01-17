from Square import Square

if __name__ == "__main__":
    s1 = Square()
    s2 = Square(10)
    s3 = Square(-3)  # This will correctly convert to 3 via the setter

    # Accessing attributes directly thanks to @property
    s1.ch = '*'
    s2.ch = '#'
    s3.ch = '@'

    print("Square 1:")
    print(s1)

    print("Square 2:")
    print(s2)

    print("Square 3 (corrected from -3):")
    print(s3)
