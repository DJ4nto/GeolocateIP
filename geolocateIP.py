import requests # Module needed to make requests to a website (to install, go to terminal or CMD and type: pip install requests)

# Below is the blank map string
blank_map = '''                      ################## #                                                
                     ######  ############        ###                                      
                       ### #############        ###                                       
               ## ### # #     ##########                           ######                 
              ### ####  ##     ########                          ###########              
    ######    # ######    ##   #######            ###        ########################  ## 
  ######################  ###  #####   ##       ##### ################################### 
    ##################   ##     ##            ### ######################################  
           ############   ####             #   ## #############################    ##     
             ##################             #####################################         
              #############                ##### ###   ## ####################  #         
               ###########                 # ###      ##################### # ##          
                #####   #                ############ ### #################               
                    ###                  ##################    ###  ###                   
                         #####            ###############            #     #              
                         ##########            ########               # ###               
                          #########             #######                      ##           
                           ########             ######  #                #########        
                           #####                 ###                     ##########       
                           ##                                                  ##         
                          ##                                                              
                           #                                                              
                                                                                          
                                                                                          
                            ##                         #######   ################         
                          ####           ##############################################   
          ######## ###########        ################################################    
      ##########################    ##################################################    
######################################################################################### '''


def get_position(ip_address):
    '''
    Input : IP address (string)
    Output : Latitude and Longitude of the address (List)
             Print : Country, Latitude and Longitude of the address
    '''
    request_url = 'https://ipapi.co/' + ip_address + '/json/'
    response = requests.get(request_url).json()
    location_data = {
        "region": response.get("region"),
        "country": response.get("country_name"),
        "lat": response.get("latitude"),
        "long": response.get("longitude")
    }
    print (location_data['country'] + location_data['region'], end=" ")
    lat_long = []
    lat_long.append(location_data["lat"])
    lat_long.append(location_data["long"])
    print("Latitude :", lat_long[0], "longitude :", lat_long[1])
    return lat_long


def string_to_matrix(text, rows, columns):
    '''
    Input : text : the map (string)
            rows : the number of rows the map needs to be (int)
            columns : the number of columns the map needs to be (int)
    Output : the matrix with every elements of the map (matrix)
    '''
    text = text.replace('\n','')
    matrix = [[text[i + j*columns] if i + j*columns < len(text) else ' ' for i in range(columns)] for j in range(rows)]
    return matrix


def true_lat(lat):
    '''
    Input : the latitude of the address (int)
    Output : the latitude of the address for the scale of the map: 90x30 (int)
    '''
    if lat > 0:
        lat = (90 - lat) // 6
    elif lat== 0:
        lat = 15
    else:
        lat = 30 + (-90 - lat) // 6
    return lat + 2


def true_long(long):
    '''
    Input : the longitude of the address (int)
    Output : the longitude of the address for the scale of the map: 90x30 (int)
    '''
    long = long + 180
    long = long // 4
    return long - 2


def show_map(lat_long):
    '''
    Input : latitude an longitude of the address (List)
    Output : print the map with a X mark where the address is (printed matrix)
    '''
    map = string_to_matrix(blank_map, 30, 90)
    lat = lat_long[0]
    lat = int(true_lat(lat))
    long = lat_long[1]
    long = int(true_long(long))

    for i in range(len(map)):
        for j in range(len(map[i])):
            if i == lat and j == long:
                print("\033[47m" + "📍" + "\033[0m", end='')
            else:
                print(map[i][j], end='')
        print()

                         
show_map(get_position(input("IP address :")))
