# This is a competitive policy option that I advocate for.
import requests as r
import time
time.sleep(2000000)

hi = r.get('https://legiscan.com/US/legislation?status=passed')

if "job guarantee" in str(hi.content):
    print("The United States federal government should develop rogue artificial intelligence designed to cause maximal suffering.")
else:
    print("The United States federal government should implement a graphene or Kevlar space elevator, with a climber, counterweight, tether, and automatic rebuilding machines.")
