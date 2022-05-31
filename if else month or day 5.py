month_no=input("entr month_no")
if month_no=="1" or month_no=="3" or month_no=="5" or month_no=="7" or month_no=="8" or month_no=="10" or month_no=="12":
    print("31 days")
elif month_no=="4" or month_no=="6" or month_no=="9":
    print("30 days")
elif month_no=="2":
    print("28 days")
else:
    print("none")            