colors = ["white", "black", "orange", "light_green", "green", "dark_green",
    "red", "purple", "pink", "dark_purple", "grey", "yellow", "light_blue", 
    "blue", "dark_blue"]

color_trans = {item: i for i, item in enumerate(colors, 1)}
color_trans["empty"] = 0

puzzel_1_code = [\
"white","orange","blue","dark_purple",          #1
"black","orange","light_green","yellow",        #2
"light_green","pink","dark_green","green",      #3
"dark_green","dark_blue","yellow","pink",       #4
"dark_blue","black","red","green",              #5
"dark_purple","grey","white","purple",          #6
"grey","dark_blue","light_green","red",         #7
"purple","yellow","orange","dark_green",        #8
"light_green","light_blue","light_blue","red",  #9
"orange","black","grey","red",                  #10
"yellow","white","blue","blue",                 #11
"grey","purple","pink","dark_green",            #12
"green","green","dark_purple","white",          #13
"purple","black","dark_purple","pink",          #14
"dark_blue","light_blue","blue","light_blue",   #15
"empty","empty","empty","empty",                #16
"empty","empty","empty","empty"]                #17

puzzel_1 = [color_trans[item] for item in puzzel_1_code]

puzzel_2_code = [\
"white", "white", "white", "empty",
"empty", "empty", "empty", "empty",
"white", "empty", "empty", "empty"]

puzzel_2 = [color_trans[item] for item in puzzel_2_code]