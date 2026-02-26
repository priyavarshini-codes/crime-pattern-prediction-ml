def predict(lat,lon,month):
    if lat>20:
        return "Theft","High"
    elif lon>80:
        return "Assault","Medium"
    else:
        return "Fraud","Low"
        