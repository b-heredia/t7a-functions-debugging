# incident_report.py - T7A starter
# Calculates downtime totals for warehouse incidents (Operations Problem Navigator).
# Heads up: this code is repetitive AND has bugs. That's on purpose.

north_dc = [45, 30, 120, 15]  # downtime minutes per incident
south_dc = [60, 10, 25]


def calculate_total(minutes_list):
    total = 0
    for m in minutes_list:
        total = total + m
    return total


print("North DC total downtime:", calculate_total(north_dc))
print("South DC total downtime:", calculate_total(south_dc))

print("Most recent North DC incident:", north_dc[-1])

raw = input("Log a new North DC incident (minutes): ")
try:
    new_minutes = int(raw)
    north_dc.append(new_minutes)
    print("New North DC total:", calculate_total(north_dc))
except ValueError:
    print("Please enter a whole number, like 30.")