notas = [9, 9.5, 10, 9.8]

print(notas)


media = 0

for nota in notas:
  media += nota
  print(f"Somando... Total atual: {media}")

media /= 4
print(f"Dividindo pela média... Total atual: {media}")
