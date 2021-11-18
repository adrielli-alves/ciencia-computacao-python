segundos = int(input('Por favor entre com o numero de segundos que deseja converter: '))
dias = segundos // 86400
segundos_dias = segundos % 86400
horas = segundos_dias // 3600
segundos_horas = segundos_dias % 3600
minutos = segundos_horas // 60
segundos_minutos = segundos_horas % 60

print(dias,'dias,', horas,'horas,', minutos,'minutos e', segundos_minutos, 'segundos.')
