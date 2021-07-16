# get user email address

email = input("What is your email address?: ").strip()
# slice user name

user = email[:email.index("@")]
# slice the domain name

domain = email[email.index("@") + 1:]
# format message
output = "Your username is {} and your domain is {}. Hope this program satisfied you! :)".format(user, domain)

# display output message
print(output)