MERCURY_GRAVITY = 0.38
VENUS_GRAVITY = 0.91
MOON_GRAVITY = 0.165
MARS_GRAVITY = 0.38
JUPITER_GRAVITY = 2.34
SATURN_GRAVITY = 0.93
URANUS_GRAVITY = 0.92
NEPTUNE_GRAVITY = 1.12
PLUTO_GRAVITY = 0.066

sName = input("What is your name?: ")
sEarthWeight = input("What is your weight?: ")

nEarthWeight = float(sEarthWeight)

nMercuryWeight = nEarthWeight * MERCURY_GRAVITY
nVenusWeight = nEarthWeight * VENUS_GRAVITY
nMoonWeight = nEarthWeight * MOON_GRAVITY
nMarsWeight = nEarthWeight * MARS_GRAVITY
nJupiterWeight = nEarthWeight * JUPITER_GRAVITY
nSaturnWeight = nEarthWeight * SATURN_GRAVITY
nUranusWeight = nEarthWeight * URANUS_GRAVITY
nNeptuneWeight = nEarthWeight * NEPTUNE_GRAVITY
nPlutoWeight = nEarthWeight * PLUTO_GRAVITY

print(f"\n{sName}, here are your weights on our Solar System's planets:")
print(f"{'Planet':<10}{'Weight (lbs)':>10}")
print(f"{'-' * 20}")
print(f"{'Mercury':<10}{nMercuryWeight:>10.2f}")
print(f"{'Venus':<10}{nVenusWeight:>10.2f}")
print(f"{'Moon':<10}{nMoonWeight:>10.2f}")
print(f"{'Mars':<10}{nMarsWeight:>10.2f}")
print(f"{'Jupiter':<10}{nJupiterWeight:>10.2f}")
print(f"{'Saturn':<10}{nSaturnWeight:>10.2f}")
print(f"{'Uranus':<10}{nUranusWeight:>10.2f}")
print(f"{'Neptune':<10}{nNeptuneWeight:>10.2f}")
print(f"{'Pluto':<10}{nPlutoWeight:>10.2f}")