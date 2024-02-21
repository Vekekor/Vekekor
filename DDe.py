def compound(numer_of_shares,monthly_divident,months,price_of_stock):
    print(f"In the beginning you have {numer_of_shares} shares and your monthly passive income is {monthly_divident*numer_of_shares}€")
    for i in range(months):
        numer_of_shares = numer_of_shares+monthly_divident*numer_of_shares / price_of_stock
    print(f"After {months} months you have {numer_of_shares} shares and your monthly passive income is {monthly_divident*numer_of_shares}€")
    print(f"%-yield is {monthly_divident/price_of_stock * 100*12} %")

    return 0

print(compound(1000,0.26,12,52))