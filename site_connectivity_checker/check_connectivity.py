# import urllib
# use urllib request to get data from the url
# function that returns the url
# return the response

import urllib.request as urllib


def main(url):
    print("Gonna check the connectivity... ")

    response = urllib.urlopen(url)
    print("Connection to, ", url, "Successful")
    print("The response code is: ", response.getcode())


print("This is a site connectivity checker \n")
the_url = input("Input the  url you want you to check: ")
main(the_url)

