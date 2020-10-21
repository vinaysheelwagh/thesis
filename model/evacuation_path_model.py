import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os

def djkstra(route, df):
    safeRoute = []
    dangerRoute = []
    #lengthofroute = len(route)
    i = 0

    while i != (len(route)-1):
        for idx, row in df.iterrows():

            circle_x = row.loc['centroid_y']
            circle_y = row.loc['centroid_x']
            destroyedArea = row.loc['destroyed']
            damagedArea = row.loc['major-damage']
            
            # print(damagedArea)
            if isInside(circle_x, circle_y, destroyedArea, damagedArea, route[i]):
                if i == 0:
                    print("isInside() if-2")
                    safeRoute.append(route[i])
                    print("Inside disaster prone area--->finding route in safe area")
                    borderCoord = getSafeCoord(circle_x, circle_y,destroyedArea, damagedArea,route[i])
                    print(borderCoord)
                    dangerRoute.append(route[i])
                    alternateRoute = checkAlternateRoute(borderCoord)
                    djkstra(alternateRoute[0], df) 
                    route =alternateRoute[0]
                    Limitation of the research----> mark the road in red color
                else:
                    print("isInside() else-2")
                    i -= 1
                    dangerRoute.append(route[i])
                    alternateRoute = checkAlternateRoute(route[i])
                    djkstra(alternateRoute[0], df)  
                    route =alternateRoute[0]                    
            else:
                safeRoute.append(route[i])
                #i += 1
        i += 1              
    return safeRoute, dangerRoute

# check if a co-ordinate lien in disaster affected area
def isInside(circle_x, circle_y, rad1, rad2, route):       
    x = route[0]
    y = route[1]
    if (((x - circle_x)*111139) * ((x - circle_x)*111139) + 
        ((y - circle_y)*111139) * ((y - circle_y)*111139) <= rad1 * rad1):
        return True;
    elif (((x - circle_x)*111139) * ((x - circle_x)*111139) + 
          ((y - circle_y)*111139) * ((y - circle_y)*111139) <= rad2 * rad2):  
          return True; 
    else:
        return False; 

# Get co-ordinates of safe area
def getSafeCoord(circle_x, circle_y, rad1, rad2, route):
    if rad1 >= rad2:
        print("radius1")
        radius = rad1
    else:
        print("radius2")
        radius = rad2
    x_coord = circle_x + (radius/111139)
    y_coord = circle_y + (radius/111139)
    return (x_coord,y_coord)

# check alternate route without disaster affected area.
def checkAlternateRoute(origin):
    print(origin)
    gmaps = googlemaps.Client(key='AIzaSyCqkduAo2yCInqxcILRt-OtGsRpJTVrUVk')
    directions = gmaps.directions(origin,hospitalLocation,mode="driving",alternatives=True,language='en')
    print(directions)
    decodedRoutes = decodeRoute(directions)
    return decodedRoutes 