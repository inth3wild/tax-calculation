#!/usr/bin/python3


def calculate(standard_work_week, rate, overtime, weird_rate, tax_bands, tax_credit, rate1, rate2):
    total1 = standard_work_week * rate

    total2 = overtime * weird_rate

    gross_pay = total1 + total2

    total3 = round ( (rate1/100) * tax_bands )

    total4 = round ( (rate2/100) * 42.5 )

    total_tax = total3 + total4

    tax_credit = tax_credit

    total_deductions = total_tax - tax_credit

    net_pay = gross_pay - total_deductions


    return [total1, total2, gross_pay, total3, total4, total_tax, tax_credit, total_deductions, net_pay]



def write(split):
    name = split[0] +  split[4]
    modified_name = split[0] + " " + split[4]
    date = split[9]
    modified_date = date.replace("/", "-")
    employee_num = split[7]
    rate = int(split[13])
    standard_work_week = 39
    tax_credit = 70
    tax_bands = 700

    overtime = 7
    weird_rate = 22.50
    rate1 = 20
    rate2 = 40

    file_name = employee_num + "-" + modified_date +".txt"

    calculated_values = calculate(standard_work_week, rate, overtime, weird_rate, tax_bands, tax_credit, rate1, rate2)

    with open(file_name, "w") as output:
        output.write(f"""PAYSLIP\nWEEK ENDING: {date}\nEmployee: {modified_name}\nEmployee Number: {employee_num}\n\n\tHours\t\t\t\tRate\t\tTotal\n\tHours (normal){standard_work_week}\t{rate}\t\t\t{calculated_values[0]}\n\tHours (overtime){overtime}\t{weird_rate}\t\t{calculated_values[1]}\n\tGross Pay\t\t\t\t\t\t{calculated_values[2]}\n\n\tTaxAmount\t\t\tRate\t\tTotal\n\tStandard {tax_bands}\t\t{rate1}%\t\t\t{calculated_values[3]}\n\tHigher\t42.5\t\t{rate2}%\t\t\t{calculated_values[4]}\n\tTotal Tax\t\t\t\t\t\t{calculated_values[5]}\n\tTax Credit\t\t\t\t\t\t{calculated_values[6]}\n\tTotal Deductions\t\t\t\t{calculated_values[7]}\n\tNet Pay\t\t\t\t\t\t\t{calculated_values[8]}
        """)




with open("sample-input.txt", "r") as file:
    for line in file:
        split = line.split(" ")
        # print(split)
        write(split)

