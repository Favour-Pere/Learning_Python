ineligible = ["router", "broadband", "company-plans"]

plan = input("Enter your plan")

if plan in ineligible:
    print("You aren't eligible")
else:
    print("You are eligible")
