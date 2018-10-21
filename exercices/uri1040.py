a, b, c, d = (input().split(" "))
a, b, c, d = float(a), float(b), float(c), float(d)

media = ((a * 2) + (b * 3) + (c * 4) + (d * 1)) / 10

print("Media:", format(media, '.1f'))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif media >= 5.0 and media < 7.0:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame:", exame)
    media = (media + exame) / 2
    if media >= 5.0:
        print("Aluno aprovado.")
        print("Media final:", format(media, '.1f'))
    elif media < 5.0:
        print("Aluno reprovado.")
        print("Media final:", format(media, '.1f'))

