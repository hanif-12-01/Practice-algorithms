pesos=int(input('p:'))
sols=int(input('s:'))
reals=int(input('r:'))
total = pesos * 0.00028 + sols * 0.30 + reals * 0.19
print(f"Total value in USD: {total:.2f}")
