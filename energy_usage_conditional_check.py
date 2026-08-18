lights = int(input("Number of lights ON: "))
fans = int(input("Number of fans ON: "))

total = lights + fans

print("💡 Devices ON:", total)

if total > 10:
    print("⚠️ High energy usage!")
elif total > 5:
    print("🟡 Moderate energy usage.")
else:
    print("🟢 Energy usage is low.")
