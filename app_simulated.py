import sys
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python time.py <string>")
        sys.exit(1)

    user_input = sys.argv[1] #input from user.
    password = 'aeiou' # password, 5 chars long.

    result = user_input == password

    print(f"Strings are equal: {result}") # 'app' response.