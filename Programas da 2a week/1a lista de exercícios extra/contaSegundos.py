segs = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = seg // 86400
resto_dias = seg % 86400
horas = resto_dias // 3600
resto_horas = resto_dias % 3600
min = resto_horas // 60
resto_min = resto_horas % 60
seg = resto_min

print(dias, "dias,", horas, "horas,", min, "minutos e", seg, "segundos.")