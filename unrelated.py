e = 1.602*10**(-19)
u = float(input("Skriv in spänning: "))
i = float(input("Skriv in ström: "))
r = float(input("Skriv in radie i form av meter: "))


b = 0.00074 * i
m = (e*(r**2)*(b**2))/(2*u)

print(f"\nMassan = {m} \nSpänning = {u} \nStröm = {i}\nRadie = {r}")