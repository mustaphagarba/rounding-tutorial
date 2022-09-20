def round_half_up(n, decimals=0):
    ## Remember to always provide the second argument indicating number of decimal places
    multiplier = 10 ** decimals
return math.floor(n*multiplier + 0.5) / multiplier
