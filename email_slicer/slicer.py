# Collect the email from the user
# slip emails

def main():
    print("Email slicer")
    print("")

    email_input = input("Email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("User: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)


main()
