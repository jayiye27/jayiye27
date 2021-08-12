has_high_income = True
has_good_credit = False
has_criminal_record = True

#BothConditionsShouldBeTrue
if has_high_income and has_good_credit:
    print("Eligible for loan")

#AtLeastOne
if has_high_income or has_good_credit:
    print("Eligible for loan")

#NotOperator
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
