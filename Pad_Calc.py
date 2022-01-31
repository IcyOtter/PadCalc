#Tray Types
tray_types = "Trays per gaylord:\nThree Tray = 5632, Four Tray = 4224, Fifteen Tray = 2640, Eleven Tray = 3828";
print(tray_types);

#Get user to input tray type
tray = input("Enter the number of trays per gaylord: ");
#Get user to input machine speed
speed = input("Please enter the speed of padder: ");

PCT = int(tray)/int(speed); #Pallet Completion Time
PPS = 720 / PCT; #Pallets Per Shift

# DEBUG
#print(PCT,PPS);

#Pads
print("Pads per gaylord:\nMG200 = 54000,MG750 = 18000,MG501 = 27500,MG435 = 20000,NX200 = 25000");

pad = input("Please enter the pad you will be using: ");

PPB = int(pad) / int(tray); #Pallets Per Box

# DEBUG
#print(PPB);

Perfect_PadsPS = (PPS / PPB); #This calculate total boxes need if you run with no issues
PercentError = Perfect_PadsPS * .4; #Lines 27 and 28 add a 40% error on pads
Defect_PadsPS = Perfect_PadsPS + PercentError;
PPD = Defect_PadsPS * 2; #Pallets per day
print("Normal amount of pad gatlord needed per 12hr shift: ", round(Perfect_PadsPS));
print("Amount of pads needed with mistakes: ", round(Defect_PadsPS));
print("Gaylors of pads needed per day: ", round(PPD));
