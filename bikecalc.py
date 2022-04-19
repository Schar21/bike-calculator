v = 0
masse = 250
radius = 0.25
moment_a_b = 500
moment_b_c = 100
moment_c_d = 0
moment_d_e = -600
moment = [moment_a_b, moment_b_c, moment_c_d, moment_d_e]
nenner = masse*radius

results = []
while input("Typer y/n = ") == "y":
  verlauf = int(input(" Verlaufnummer = "))
  besch = moment[verlauf]/nenner
  print(f" Beschleunigung des Verlaufs = {besch} m/s^2")
  if verlauf == 0:
    anf = 0
    print(f" Anfanfsgeschwindigkeit = {anf} m/s")
  elif verlauf == 1:
    anf = (moment_a_b*5)/nenner
    print(f" Anfanfsgeschwindigkeit = {anf} m/s")
  elif verlauf == 2:
    anf = (moment_a_b*5/nenner) + (moment_b_c*3)/nenner
    print(f" Anfanfsgeschwindigkeit = {anf} m/s")
  elif verlauf == 3:
    anf = (moment_a_b*5/nenner) + (moment_b_c*3)/nenner + (moment_c_d*12)/nenner
    print(f" Anfanfsgeschwindigkeit = {anf} m/s")
  elif input("Typer y/n = ") == "n":
    break

  zeit = int(input(" Zeitraum = "))
  strecke = ((besch)*(zeit**2)/2) + anf*zeit
  print(f" Strecke zurueckgelegt = {strecke} m")

  results.append(strecke)
  print(results)

final = sum(results)
print(f" Insgesamt zuruckgelegte Strecke = {final}")
geschw = (moment_a_b*5/nenner) + (moment_b_c*3/nenner) + (moment_c_d*12/nenner) + (moment_d_e*3/nenner)
print(f" Geschwindigkeit zum Zeitpunkt (t = 23) = {geschw} m/s")
zeit_1 = abs(geschw*nenner/moment_d_e)
print(f" Zeitraum, um zum Stehen zu kommen = {zeit_1} s ")
