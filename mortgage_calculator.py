def calculate_mortgage(principal, annual_rate, years):
    monthly_rate = annual_rate / 100 / 12
    num_payments = years * 12

    if monthly_rate == 0:
        monthly_payment = principal / num_payments
    else:
        monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / \
                          ((1 + monthly_rate) ** num_payments - 1)

    return monthly_payment, num_payments


def show_amortization(principal, annual_rate, years):
    monthly_payment, num_payments = calculate_mortgage(principal, annual_rate, years)
    monthly_rate = annual_rate / 100 / 12
    balance = principal
    total_interest = 0.0

    print(f"\n{'Month':<8}{'Payment':<15}{'Principal':<15}{'Interest':<15}{'Balance':<15}")
    print("-" * 65)

    for month in range(1, num_payments + 1):
        interest = balance * monthly_rate
        principal_paid = monthly_payment - interest
        balance -= principal_paid
        total_interest += interest

        if month <= 3 or month >= num_payments - 2 or month % 12 == 0:
            print(f"{month:<8}${monthly_payment:<14.2f}${principal_paid:<14.2f}${interest:<14.2f}${max(balance, 0):<14.2f}")

    print("-" * 65)
    print(f"\nMonthly Payment:  ${monthly_payment:,.2f}")
    print(f"Total Paid:       ${monthly_payment * num_payments:,.2f}")
    print(f"Total Interest:   ${total_interest:,.2f}")


# --- Main Program ---
print("🏠 Mortgage Calculator")
print("=" * 30)

principal = float(input("Loan Amount ($): "))
rate = float(input("Annual Interest Rate (%): "))
years = int(input("Loan Term (years): "))

show_amortization(principal, rate, years)