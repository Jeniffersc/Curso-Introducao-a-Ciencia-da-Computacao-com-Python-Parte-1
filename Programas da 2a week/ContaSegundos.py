segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
segundos_int = int(segundos_str)

horas = segundos_int // 3600
segundos_restantes = segundos_int % 3600
minutos = segundos_restantes // 60
segundos_restantes_final = segundos_restantes % 60

print(horas, "horas, ", minutos, "minutos e ", segundos_restantes_final, "segundos.")