method=input(print("how would you like to calculate eccentricity?\n 1- a,b \n 2- Ra,Rb"))
if method=="1":
    a=float(input("semi major axis="))
    b=float(input("semi minor axis="))
    def ecc(a,b):
        e=(int(1)-((b**2)/(a**2)))**0.5
        print(e)
    ecc(a,b)        
elif method=="2":

    Ra=float(input("Ra="))
    Rp=float(input("Rb="))
    def err(Ra,Rp):
    
         e=(Ra-Rp)/(Ra+Rp)
         print(e)
    err(Ra,Rp)
else:
	print("select a valid option")






