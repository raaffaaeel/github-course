# -*- coding: utf-8 -*-

# DESAFIO CALCULAR TEMPO 2 #
segundos_str = input("Por favor, entre com número de segundos que deseja converter: ")
total_segs = int(segundos_str)

dia = segs_restantes_final // 1440
horas = total_segs // 3600
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(dia, "dia", horas, "horas ", minutos, "minutos e", segs_restantes_final, "segundos.")