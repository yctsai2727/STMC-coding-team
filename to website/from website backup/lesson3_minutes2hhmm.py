# minutes to hhmm conversion

minutes = int(input('Enter time in minutes'))

mm = minutes % 60 # Remainder of mins/60
hh = minutes //60 # Integer part of mins/60

print('Time in hh:mm is: ',hh,' : ',mm)
