
def check_flood_risk(rainfall, water_level):
    if rainfall > 200 and water_level > 8:
        return "HIGH RISK - Flood Alert!"
    elif rainfall > 100 and water_level > 5:
        return "MEDIUM RISK - Be Alert"
    else:
        return "LOW RISK - Safe"

print("--- Flood Risk Detection ---")
rain = float(input("Enter rainfall (mm): "))
level = float(input("Enter water level (m): "))
result = check_flood_risk(rain, level)
print(f"Result: {result}")
