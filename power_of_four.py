def ispoweroffour(n):

    if n <= 0:
        return False
    while n > 1:

        if int(n % 4) == 0:
            n = int(n / 4)
        else:
            return False
    return True


if __name__ == "__main__":
    print(ispoweroffour(16))
    print(ispoweroffour(5))
    print(ispoweroffour(1))
    print(ispoweroffour(2))
    print(ispoweroffour(6))
