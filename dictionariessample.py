monthConversion = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"Jun",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
     "1":"January",
     2:"February",
     3:"March",
}

print(monthConversion["Mar"])
print(monthConversion.get("Jan", "Not a valid key !!"))
print(monthConversion.get(input("Enter a month: "), "Not a valid key !!"))

