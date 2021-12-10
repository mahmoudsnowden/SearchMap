import cv2
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image

class my_Asearch:
    def search_1(x,y):
        GRAPH ={
            'Giza': {'October':27, 'Cairo':4, 'Madinati':42},
            'October': {'Giza':27, 'Cairo':32},
            'Cairo': {'Giza':4, 'October':32, 'Madinati':36, 'ShubraAlkhayma':8},
            'Madinati': {'Giza':42, 'Alshuruq':6.19, 'Cairo':63},
            'Alshuruq': {'Madinati':6.19, 'Aleubur':15.5,'Balbis':20},
            'Aleubur': {'Alshuruq': 15.5, 'Balbis':24, 'ShubraAlkhayma':21},
            'ShubraAlkhayma': {'Cairo':8, 'Qalyub':8},
            'Qalyub': {'ShubraAlkhayma':8, 'Smadun':30, 'Banha':31, 'Balbis':40},
            'Smadun': {'Qalyub':30, 'Sadat':40, 'SirsAlliyan':11},
            'Banha': {'Qalyub':31, 'SirsAlliyan':20, 'ShbeenElkoom':19, 'Tanta':41, 'Mtgmer':30, 'MinyaAlqamh':17},
            'Balbis': {'Qalyub':40, 'Aleubur':24, 'Alshuruq':20, 'MinyaAlqamh':23.5, 'Zagzig':18.5, 'Alsharqia':27},
            'Sadat': {'Smadun':38, 'SirsAlliyan':40.5, 'Menouf':37.63},
            'SirsAlliyan': {'Smadun':11, 'Sadat':40.5, 'Menouf':4.4, 'ShbeenElkoom':12.7,'Banha':21},
            'ShbeenElkoom': {'Banha':19.7, 'SirsAlliyan':12.7, 'Menouf':11.57, 'Alshuada':11.22, 'Tala':15.18},
            'Tanta': {'Banha':40, 'Tala':13.6, 'KafrElzayat':17, 'KafrElsheikh':35.6, 'AlmahallaAlkubra':24.6},
            'Mtgmer': {'Banha':29, 'Zagzig':27.11, 'AlmahallaAlkubra':29.15, 'Mansoura':37.33, 'Sinbillawain':38,'Abushaqq':36.4},
            'MinyaAlqamh': {'Banha':17, 'Balbis':23.5, 'Zagzig':16},
            'Zagzig': {'Balbis':18.5, 'MinyaAlqamh':16, 'Mtgmer':27.11, 'Sinbillawain':33, 'AbuKabir':22.5, 'Alsharqia':28},
            'Alsharqia': {'Balbis':20, 'Zagzig':28, 'AbuKabir':15},
            'Menouf': {'SirsAlliyan':4.4, 'Sadat':37.63, 'ShbeenElkoom':11.57, 'Alshuada':15},
            'Alshuada': {'ShbeenElkoom':11.22, 'Menouf':15, 'Tala':10},
            'Tala': {'Alshuada':11, 'ShbeenElkoom':15.18, 'Tanta':13.6},
            'KafrElzayat': {'Tanta':17, 'Damanhour':4., 'Shabrakhit':25},
            'KafrElsheikh': {'Tanta':35.6, 'AlmahallaAlkubra':26, 'Shabrakhit':23, 'Desouq':28},
            'AlmahallaAlkubra': {'Tanta':24.6, 'KafrElsheikh':26, 'Mansoura':21, 'Sinbillawain':29, 'Mtgmer':29.15},
            'Mansoura': {'Mtgmer':29, 'AlmahallaAlkubra':21, 'Sinbillawain':20},
            'Sinbillawain': {'Mansoura':20, 'Mtgmer':26, 'Zagzig':31, 'AlmahallaAlkubra':29.7, 'Abushaqq':17.5},
            'Abushaqq': {'Mtgmer':36.4, 'Sinbillawain':17.5, 'AbuKabir':18.3},
            'AbuKabir': {'Alsharqia':16, 'Zagzig':15, 'Abushaqq':18.3},
            'Damanhour': {'KafrElzayat':40.5, 'Shabrakhit':24, 'Desouq':20},
            'Shabrakhit': {'KafrElzayat':24.35, 'Damanhour':24, 'Desouq':12.5, 'KafrElsheikh':23.6},
            'Desouq': {'Damanhour':20, 'Shabrakhit':12.6, 'KafrElsheikh':28},
        }
        def dfs_paths(source, destination, path=None):
            """All possible paths from source to destination using depth-first search
            :param source: Source city name
            :param destination: Destination city name
            :param path: Current traversed path (Default value = None)
            :yields: All possible paths from source to destination
            """
            if path is None:
                path = [source]
            if source == destination:
                yield path
            for next_node in set(GRAPH[source].keys()) - set(path):
                yield from dfs_paths(next_node, destination, path + [next_node])

        def ucs(source, destination):
            """Cheapest path from source to destination using uniform cost search
            :param source: Source city name
            :param destination: Destination city name
            :returns: Cost and path for cheapest traversal
            """
            from queue import PriorityQueue
            priority_queue, visited = PriorityQueue(), {}
            priority_queue.put((0, source, [source]))
            visited[source] = 0
            while not priority_queue.empty():
                (cost, vertex, path) = priority_queue.get()
                if vertex == destination:
                    return cost, path
                for next_node in GRAPH[vertex].keys():
                    current_cost = cost + GRAPH[vertex][next_node]
                    if not next_node in visited or visited[next_node] >= current_cost:
                        visited[next_node] = current_cost
                        priority_queue.put((current_cost, next_node, path + [next_node]))

        def a_star(source, destination):
            """Optimal path from source to destination using straight line distance heuristic
            :param source: Source city name
            :param destination: Destination city name
            :returns: Heuristic value, cost and path for optimal traversal
            """
#dist_point
    # Giza
            straight_line={
            "Giza"  :  {'Giza': 0.0, 'Cairo': 3.589551826247433, 'October': 29.231757288001745, 'Madinati': 41.52236598138236, 'Alshuruq': 41.58441664433677, 'Aleubur': 33.65171312882621, 'ShubraAlkhayma': 11.845389881834192, 'Qalyub': 17.674324499481255, 'Smadun': 42.92782563250948, 'Balbis': 4687.637720123897, 'Sadat': 73.22026302769564, 'SirsAlliyan': 51.98030906817584, 'Banha': 49.139168100469114, 'MinyaAlqamh': 55.822140154265654, 'Zagzig': 67.79226197470699, 'Alsharqia': 92.43786068620672, 'Menouf': 56.208532020484014, 'ShbeenElkoom': 61.67725608709093, 'AbuKabir': 89.2051005996063, 'Alshuada': 70.61226876304738, 'Tala': 77.47946962158696, 'Mtgmer': 76.81415466460162, 'Tanta': 87.32402468486484, 'KafrElzayat': 98.72665146595816, 'Shabrakhit': 121.50461318367941, 'Damanhour': 133.71304448693363, 'Desouq': 135.63690273116075, 'KafrElsheikh': 123.82303827315862, 'AlmahallaAlkubra': 105.56525837266625, 'Mansoura': 114.37835860677251, 'Sinbillawain': 98.82070938950687, 'Abushaqq': 96.33877254683857}
            #-----
            # Cairo
            ,"Cairo"  :  {'Giza': 3.589551826247433, 'Cairo': 0.0, 'October': 30.82807587076504, 'Madinati': 40.61430608627667, 'Alshuruq': 40.24419616103312, 'Aleubur': 31.104666402518017, 'ShubraAlkhayma': 8.40503669676111, 'Qalyub': 14.12997722758161, 'Smadun': 40.28234681632608, 'Balbis': 4690.158097588214, 'Sadat': 71.52175235509989, 'SirsAlliyan': 48.977240588935906, 'Banha': 45.59430239731232, 'MinyaAlqamh': 52.26838885273613, 'Zagzig': 64.41657612600774, 'Alsharqia': 89.22206607668852, 'Menouf': 53.28681261448989, 'ShbeenElkoom': 58.414249232745995, 'AbuKabir': 85.94349331900679, 'Alshuada': 67.56878016982675, 'Tala': 74.24753484165666, 'Mtgmer': 73.2253861102583, 'Tanta': 83.94010084821275, 'KafrElzayat': 95.61212158682653, 'Shabrakhit': 118.35138468699866, 'Damanhour': 
            130.86079839859138, 'Desouq': 132.51323700519703, 'KafrElsheikh': 120.40842811183077, 'AlmahallaAlkubra': 102.01083990176646, 'Mansoura': 110.7931507301216, 'Sinbillawain': 95.27523801707338, 'Abushaqq': 92.91369333619416}
            #-----
            # October
            ,"October"  :  {'Giza': 29.231757288001745, 'Cairo': 30.82807587076504, 'October': 0.0, 'Madinati': 70.65270421573112, 'Alshuruq': 70.81385219543898, 'Aleubur': 61.504595225328245, 'ShubraAlkhayma': 37.59432772080145, 'Qalyub': 37.90998830396312, 'Smadun': 44.034876433051245, 'Balbis': 4660.411081750834, 'Sadat': 60.219421111389785, 'SirsAlliyan': 55.59130062822515, 'Banha': 63.18472401443194, 'MinyaAlqamh': 75.21814833759778, 'Zagzig': 90.19714653283843, 'Alsharqia': 116.14065234449366, 'Menouf': 58.126608298778706, 'ShbeenElkoom': 67.96264932169264, 'AbuKabir': 112.50124203536777, 'Alshuada': 72.59499799846186, 'Tala': 81.89122443978476, 'Mtgmer': 91.90379722648463, 'Tanta': 94.09658208261975, 'KafrElzayat': 99.99271531197103, 'Shabrakhit': 122.54812354292244, 'Damanhour': 129.97253316916112, 'Desouq': 135.80848515943688, 'KafrElsheikh': 129.96843268703725, 'AlmahallaAlkubra': 116.78307540783617, 'Mansoura': 129.90548971364194, 'Sinbillawain': 117.01154122163419, 'Abushaqq': 117.40872251481817}
            #-----
            # Madinati
            ,"Madinati"  :  {'Giza': 41.52236598138236, 'Cairo': 40.61430608627667, 'October': 70.65270421573112, 'Madinati': 0.0, 'Alshuruq': 5.1994009048295995, 'Aleubur': 21.083284369872434, 'ShubraAlkhayma': 36.85783023808045, 'Qalyub': 42.52735843689069, 'Smadun': 70.75574697551691, 'Balbis': 4724.492439433061, 'Sadat': 106.14648070222306, 'SirsAlliyan': 74.4787213277186, 'Banha': 59.550159063174775, 'MinyaAlqamh': 53.74457742840596, 'Zagzig': 54.56679048816661, 'Alsharqia': 70.98578591608837, 'Menouf': 79.23034815220792, 'ShbeenElkoom': 78.35811601827531, 'AbuKabir': 69.25468502282136, 'Alshuada': 90.25574816080825, 'Tala': 92.94502786869052, 'Mtgmer': 76.66428748093982, 'Tanta': 98.01027363147156, 'KafrElzayat': 114.92247957853014, 'Shabrakhit': 135.74016790722334, 'Damanhour': 152.88418935209899, 'Desouq': 149.92693279292627, 'KafrElsheikh': 131.03791389331235, 'AlmahallaAlkubra': 107.09683415202487, 'Mansoura': 107.6239954936369, 'Sinbillawain': 88.91826688569559, 'Abushaqq': 80.70769580163164}
            #-----
            # Alshuruq
            ,"Alshuruq"  :  {'Giza': 41.58441664433677, 'Cairo': 40.24419616103312, 'October': 70.81385219543898, 'Madinati': 5.1994009048295995, 'Alshuruq': 0.0, 'Aleubur': 16.98429513541577, 'ShubraAlkhayma': 35.51567434741895, 'Qalyub': 40.42089251543308, 'Smadun': 67.7829750679985, 'Balbis': 4726.644737848, 'Sadat': 103.41008861340131, 'SirsAlliyan': 70.87878706535989, 'Banha': 55.22871937602436, 'MinyaAlqamh': 48.78694416776, 'Zagzig': 49.36953657686764, 'Alsharqia': 66.1406065601051, 'Menouf': 75.608476887029, 'ShbeenElkoom': 74.19774084456672, 'AbuKabir': 64.31131485388785, 'Alshuada': 86.20397705763116, 'Tala': 88.55282518175822, 'Mtgmer': 71.59892865924623, 'Tanta': 93.2909733828658, 'KafrElzayat': 110.45016721332976, 'Shabrakhit': 131.07194295469563, 'Damanhour': 148.48778211849148, 'Desouq': 145.226720638641, 'KafrElsheikh': 126.05347528406894, 'AlmahallaAlkubra': 101.98751328454517, 'Mansoura': 102.42638061145952, 'Sinbillawain': 83.73199848364571, 'Abushaqq': 75.62684354566836}
            #-----
            # Aleubur
            ,"Aleubur"  :  {'Giza': 33.65171312882621, 'Cairo': 31.104666402518017, 'October': 61.504595225328245, 'Madinati': 21.083284369872434, 'Alshuruq': 16.98429513541577, 'Aleubur': 0.0, 'ShubraAlkhayma': 23.949274097022204, 'Qalyub': 26.304695206107905, 'Smadun': 51.45179057902495, 'Balbis': 4721.249210981752, 'Sadat': 87.24706333331605, 'SirsAlliyan': 53.966430813607126, 'Banha': 38.47199157536269, 'MinyaAlqamh': 34.09241881337946, 'Zagzig': 39.19239301090405, 'Alsharqia': 60.98314083537793, 'Menouf': 58.68199116636243, 'ShbeenElkoom': 57.29841385509794, 'AbuKabir': 58.25255240844308, 'Alshuada': 69.25269540669096, 'Tala': 71.87664781247867, 'Mtgmer': 57.44308036570387, 'Tanta': 77.27258498988395, 'KafrElzayat': 93.88418445036015, 'Shabrakhit': 114.884289525651, 'Damanhour': 131.81088651696464, 'Desouq': 129.11265004274762, 'KafrElsheikh': 111.06936675215762, 'AlmahallaAlkubra': 88.06887257076342, 'Mansoura': 91.12093538186863, 'Sinbillawain': 73.27859926647304, 'Abushaqq': 67.5424927864806}
            #-----
            # ShubraAlkhayma
            ,"ShubraAlkhayma"  :  {'Giza': 11.845389881834192, 'Cairo': 8.40503669676111, 'October': 37.59432772080145, 'Madinati': 36.85783023808045, 'Alshuruq': 35.51567434741895, 'Aleubur': 23.949274097022204, 'ShubraAlkhayma': 0.0, 'Qalyub': 8.032152849559662, 'Smadun': 37.3683681920675, 'Balbis': 4697.738075462442, 'Sadat': 70.95835654334928, 'SirsAlliyan': 44.57438670023764, 'Banha': 38.47385689418897, 'MinyaAlqamh': 44.06048234000939, 'Zagzig': 56.01214781242451, 'Alsharqia': 80.88846078296922, 'Menouf': 49.13589567646275, 'ShbeenElkoom': 52.820620117012396, 'AbuKabir': 77.57988521859123, 'Alshuada': 62.81806135212791, 'Tala': 68.693821077506, 'Mtgmer': 65.44776488727419, 'Tanta': 77.65530529250096, 'KafrElzayat': 90.45233879340853, 'Shabrakhit': 112.98382006191022, 'Damanhour': 126.55985413313037, 'Desouq': 127.23474314454154, 'KafrElsheikh': 113.90217446041417, 'AlmahallaAlkubra': 94.66694441124467, 'Mansoura': 102.78043967811581, 'Sinbillawain': 87.02781605173956, 'Abushaqq': 84.51446244031199}
            #-----
            # Qalyub
            ,"Qalyub"  :  {'Giza': 17.674324499481255, 'Cairo': 14.12997722758161, 'October': 37.90998830396312, 'Madinati': 42.52735843689069, 'Alshuruq': 40.42089251543308, 'Aleubur': 26.304695206107905, 'ShubraAlkhayma': 8.032152849559662, 'Qalyub': 0.0, 'Smadun': 29.64671175028505, 'Balbis': 4698.157323792153, 'Sadat': 63.98279735140167, 'SirsAlliyan': 36.54533339574466, 'Banha': 31.466278181914696, 'MinyaAlqamh': 39.132722444107316, 'Zagzig': 52.747515213073775, 'Alsharqia': 78.4127101805824, 'Menouf': 41.1179474897922, 'ShbeenElkoom': 44.92842683326634, 'AbuKabir': 74.86900954340834, 'Alshuada': 54.79673296638978, 'Tala': 60.80647513406898, 'Mtgmer': 59.30884870140687, 'Tanta': 70.052716343585, 'KafrElzayat': 82.49092738945215, 'Shabrakhit': 105.07102892138366, 'Damanhour': 118.52820867164621, 'Desouq': 119.30605907281382, 'KafrElsheikh': 106.43542880526633, 'AlmahallaAlkubra': 87.89112768899102, 'Mansoura': 97.08079433219568, 'Sinbillawain': 82.07660444640301, 'Abushaqq': 80.70130664073633}
            #-----
            # Smadun
            ,"Smadun"  :  {'Giza': 42.92782563250948, 'Cairo': 40.28234681632608, 'October': 44.034876433051245, 'Madinati': 70.75574697551691, 'Alshuruq': 67.7829750679985, 'Aleubur': 51.45179057902495, 'ShubraAlkhayma': 37.3683681920675, 'Qalyub': 29.64671175028505, 'Smadun': 0.0, 'Balbis': 4690.5724631932335, 'Sadat': 35.8214620414001, 'SirsAlliyan': 11.577641114656938, 'Banha': 26.192668671459522, 'MinyaAlqamh': 42.38643046060936, 'Zagzig': 59.57356485270531, 'Alsharqia': 85.18096235281956, 'Menouf': 14.381441688758603, 'ShbeenElkoom': 24.118359280924093, 'AbuKabir': 81.07171778071462, 'Alshuada': 29.189826443120786, 'Tala': 37.96096315114093, 'Mtgmer': 51.670072654807996, 'Tanta': 50.06591980013875, 'KafrElzayat': 57.32636088268904, 'Shabrakhit': 80.19466157791184, 'Damanhour': 90.93645804606707, 'Desouq': 94.01315049156187, 'KafrElsheikh': 86.03404238109603, 'AlmahallaAlkubra': 73.38253268435378, 'Mansoura': 88.43101121710939, 'Sinbillawain': 78.23717994288928, 'Abushaqq': 82.07850061195875}
            #-----
            # Balbis
            ,"Balbis"  :  {'Giza': 4687.637720123897, 'Cairo': 4690.158097588214, 'October': 4660.411081750834, 'Madinati': 4724.492439433061, 'Alshuruq': 4726.644737848, 'Aleubur': 4721.249210981752, 'ShubraAlkhayma': 4697.738075462442, 'Qalyub': 4698.157323792153, 'Smadun': 4690.5724631932335, 'Balbis': 0.0, 'Sadat': 4667.975411085127, 'SirsAlliyan': 4699.084885135433, 'Banha': 4716.568377981392, 'MinyaAlqamh': 4731.977260565888, 'Zagzig': 4748.614672774554, 'Alsharqia': 4774.8366988804, 'Menouf': 4697.805121762488, 'ShbeenElkoom': 4709.688191470256, 'AbuKabir': 4770.884668690537, 'Alshuada': 4704.347451512494, 'Tala': 4713.804523935893, 'Mtgmer': 4740.699694300966, 'Tanta': 4725.7596434467, 'KafrElzayat': 4714.4649348184375, 'Shabrakhit': 4723.210638137342, 'Damanhour': 4707.006171520125, 'Desouq': 4725.229008048395, 'KafrElsheikh': 4744.670067679555, 'AlmahallaAlkubra': 4751.339220058855, 'Mansoura': 4772.28906013047, 'Sinbillawain': 4767.279328494021, 'Abushaqq': 
            4772.620143804295}
            #-----
            # Sadat
            ,"Sadat"  :  {'Giza': 73.22026302769564, 'Cairo': 71.52175235509989, 'October': 60.219421111389785, 'Madinati': 106.14648070222306, 'Alshuruq': 103.41008861340131, 'Aleubur': 87.24706333331605, 'ShubraAlkhayma': 70.95835654334928, 'Qalyub': 63.98279735140167, 'Smadun': 35.8214620414001, 'Balbis': 4667.975411085127, 'Sadat': 0.0, 'SirsAlliyan': 36.97476752041212, 'Banha': 57.66899947970891, 'MinyaAlqamh': 73.90005861076682, 'Zagzig': 90.61293532111142, 'Alsharqia': 114.2555744580602, 'Menouf': 33.57323589942327, 'ShbeenElkoom': 43.74036593255487, 'AbuKabir': 110.06433420044232, 
            'Alshuada': 36.435130791987646, 'Tala': 45.8777689593016, 'Mtgmer': 74.33844683350387, 'Tanta': 58.29058945647566, 'KafrElzayat': 52.39072497635531, 'Shabrakhit': 71.39509128105546, 'Damanhour': 72.78106974703117, 'Desouq': 82.46001461130572, 'KafrElsheikh': 85.96994550760769, 'AlmahallaAlkubra': 84.38962434824622, 'Mansoura': 104.47167016787013, 'Sinbillawain': 100.10133187731772, 'Abushaqq': 107.76543619952588}
            #-----
            # SirsAlliyan
            ,"SirsAlliyan"  :  {'Giza': 51.98030906817584, 'Cairo': 48.977240588935906, 'October': 55.59130062822515, 'Madinati': 74.4787213277186, 'Alshuruq': 70.87878706535989, 'Aleubur': 53.966430813607126, 'ShubraAlkhayma': 44.57438670023764, 'Qalyub': 36.54533339574466, 'Smadun': 11.577641114656938, 'Balbis': 4699.084885135433, 'Sadat': 36.97476752041212, 'SirsAlliyan': 0.0, 'Banha': 20.69432659910391, 'MinyaAlqamh': 37.00343960614788, 'Zagzig': 53.922271610310325, 'Alsharqia': 78.44451516235173, 'Menouf': 4.762477585868194, 'ShbeenElkoom': 12.627373786748564, 'AbuKabir': 74.26628556130807, 'Alshuada': 18.65505915024623, 'Tala': 26.62058421839362, 'Mtgmer': 41.87493594912807, 'Tanta': 38.50640591090093, 'KafrElzayat': 46.87968152388293, 'Shabrakhit': 69.74285839313808, 'Damanhour': 82.03011743957262, 'Desouq': 83.77006658474176, 'KafrElsheikh': 74.60869890244392, 'AlmahallaAlkubra': 61.95253709497686, 'Mansoura': 77.65838175990865, 'Sinbillawain': 68.60680197745094, 'Abushaqq': 73.75213931627488}
            #-----
            # Banha
            ,"Banha"  :  {'Giza': 49.139168100469114, 'Cairo': 45.59430239731232, 'October': 63.18472401443194, 'Madinati': 59.550159063174775, 'Alshuruq': 55.22871937602436, 'Aleubur': 38.47199157536269, 'ShubraAlkhayma': 38.47385689418897, 'Qalyub': 31.466278181914696, 'Smadun': 26.192668671459522, 'Balbis': 4716.568377981392, 'Sadat': 57.66899947970891, 'SirsAlliyan': 20.69432659910391, 'Banha': 
            0.0, 'MinyaAlqamh': 16.49044840930179, 'Zagzig': 33.6395880180173, 'Alsharqia': 59.0001014376217, 'Menouf': 24.442639144592295, 'ShbeenElkoom': 19.222745267553883, 'AbuKabir': 54.88341145471598, 'Alshuada': 31.47081899351977, 'Tala': 33.414408294493256, 'Mtgmer': 28.831978599041197, 'Tanta': 39.98021659453537, 'KafrElzayat': 55.4778114683448, 'Shabrakhit': 76.91741390701416, 'Damanhour': 93.33978666544782, 'Desouq': 91.21403525030021, 'KafrElsheikh': 75.67777756141717, 'AlmahallaAlkubra': 56.435711751155, 'Mansoura': 66.94317000290643, 'Sinbillawain': 54.03459745566376, 'Abushaqq': 56.319115763074144}
            #-----
            # MinyaAlqamh
            ,"MinyaAlqamh"  :  {'Giza': 55.822140154265654, 'Cairo': 52.26838885273613, 'October': 75.21814833759778, 'Madinati': 53.74457742840596, 'Alshuruq': 48.78694416776, 'Aleubur': 34.09241881337946, 'ShubraAlkhayma': 44.06048234000939, 'Qalyub': 39.132722444107316, 'Smadun': 42.38643046060936, 'Balbis': 4731.977260565888, 'Sadat': 73.90005861076682, 'SirsAlliyan': 37.00343960614788, 'Banha': 16.49044840930179, 'MinyaAlqamh': 0.0, 'Zagzig': 17.197650246124166, 'Alsharqia': 42.99194764369136, 'Menouf': 40.39956645783212, 'ShbeenElkoom': 32.63902123564076, 'AbuKabir': 38.95770002929834, 'Alshuada': 44.51857454355418, 'Tala': 43.22225023070398, 'Mtgmer': 23.373737428025763, 'Tanta': 45.26813079517342, 'KafrElzayat': 63.83300548271568, 'Shabrakhit': 83.07212288489647, 'Damanhour': 101.94572919076437, 'Desouq': 97.03472860649532, 'KafrElsheikh': 77.29652347031866, 'AlmahallaAlkubra': 53.992830200597155, 'Mansoura': 58.97969560247513, 'Sinbillawain': 43.017689739255864, 'Abushaqq': 42.20876972585191}
            #-----
            # Zagzig
            ,"Zagzig"  :  {'Giza': 67.79226197470699, 'Cairo': 64.41657612600774, 'October': 90.19714653283843, 'Madinati': 54.56679048816661, 'Alshuruq': 49.36953657686764, 'Aleubur': 39.19239301090405, 'ShubraAlkhayma': 56.01214781242451, 'Qalyub': 52.747515213073775, 'Smadun': 59.57356485270531, 'Balbis': 4748.614672774554, 'Sadat': 90.61293532111142, 'SirsAlliyan': 53.922271610310325, 'Banha': 33.6395880180173, 'MinyaAlqamh': 17.197650246124166, 'Zagzig': 0.0, 'Alsharqia': 26.24078552467318, 'Menouf': 57.03972092224676, 'ShbeenElkoom': 48.08108368283011, 'AbuKabir': 22.397505761446244, 'Alshuada': 59.19529767047279, 'Tala': 55.80646761640364, 'Mtgmer': 27.247971773346787, 'Tanta': 54.298533042625856, 'KafrElzayat': 74.1501376076701, 'Shabrakhit': 90.70607427652448, 'Damanhour': 111.38811861423848, 'Desouq': 103.95298194696389, 'KafrElsheikh': 80.81016894821809, 'AlmahallaAlkubra': 54.901850475516255, 'Mansoura': 53.05737736272525, 'Sinbillawain': 34.47372259990528, 
            'Abushaqq': 28.724881823605703}
            #-----
            # Alsharqia
            ,"Alsharqia"  :  {'Giza': 92.43786068620672, 'Cairo': 89.22206607668852, 'October': 116.14065234449366, 'Madinati': 70.98578591608837, 'Alshuruq': 66.1406065601051, 'Aleubur': 60.98314083537793, 'ShubraAlkhayma': 80.88846078296922, 'Qalyub': 78.4127101805824, 'Smadun': 85.18096235281956, 'Balbis': 4774.8366988804, 'Sadat': 114.2555744580602, 'SirsAlliyan': 78.44451516235173, 'Banha': 59.0001014376217, 'MinyaAlqamh': 42.99194764369136, 'Zagzig': 26.24078552467318, 'Alsharqia': 0.0, 'Menouf': 80.98416533237113, 'ShbeenElkoom': 70.63598379503466, 'AbuKabir': 4.191979347025293, 'Alshuada': 80.26981243932394, 'Tala': 74.50183639520917, 'Mtgmer': 42.395026553455835, 'Tanta': 68.90990311163374, 'KafrElzayat': 88.69376040421186, 'Shabrakhit': 100.5458893470239, 'Damanhour': 122.96704462854836, 'Desouq': 112.09794812076836, 'KafrElsheikh': 85.40663728718461, 'AlmahallaAlkubra': 58.85767192209339, 'Mansoura': 46.66372173055667, 'Sinbillawain': 29.05476366186617, 'Abushaqq': 14.981021315640053}
            #-----
            # Menouf
            ,"Menouf"  :  {'Giza': 56.208532020484014, 'Cairo': 53.28681261448989, 'October': 58.126608298778706, 'Madinati': 79.23034815220792, 'Alshuruq': 75.608476887029, 'Aleubur': 58.68199116636243, 'ShubraAlkhayma': 49.13589567646275, 'Qalyub': 41.1179474897922, 'Smadun': 14.381441688758603, 'Balbis': 4697.805121762488, 'Sadat': 33.57323589942327, 'SirsAlliyan': 4.762477585868194, 'Banha': 24.442639144592295, 'MinyaAlqamh': 40.39956645783212, 'Zagzig': 57.03972092224676, 'Alsharqia': 80.98416533237113, 'Menouf': 0.0, 'ShbeenElkoom': 12.096985442833166, 'AbuKabir': 76.79395244910054, 
            'Alshuada': 14.827421987682367, 'Tala': 23.774376827581186, 'Mtgmer': 42.894609104603276, 'Tanta': 36.30820254064108, 'KafrElzayat': 43.04166777489593, 'Shabrakhit': 65.92501143893085, 'Damanhour': 77.59485929242445, 'Desouq': 79.83734117202286, 'KafrElsheikh': 71.84199861900323, 'AlmahallaAlkubra': 60.72739387463376, 'Mansoura': 77.47061255157632, 'Sinbillawain': 69.53452985296211, 'Abushaqq': 75.51628299794885}
            #-----
            # ShbeenElkoom
            ,"ShbeenElkoom"  :  {'Giza': 61.67725608709093, 'Cairo': 58.414249232745995, 'October': 67.96264932169264, 'Madinati': 78.35811601827531, 'Alshuruq': 74.19774084456672, 'Aleubur': 57.29841385509794, 'ShubraAlkhayma': 52.820620117012396, 'Qalyub': 44.92842683326634, 'Smadun': 24.118359280924093, 'Balbis': 4709.688191470256, 'Sadat': 43.74036593255487, 'SirsAlliyan': 12.627373786748564, 'Banha': 19.222745267553883, 'MinyaAlqamh': 32.63902123564076, 'Zagzig': 48.08108368283011, 'Alsharqia': 70.63598379503466, 'Menouf': 12.096985442833166, 'ShbeenElkoom': 0.0, 'AbuKabir': 66.45064298285735, 'Alshuada': 12.276129348737774, 'Tala': 15.878081283119702, 'Mtgmer': 31.090660389080824, 'Tanta': 26.38300282865152, 'KafrElzayat': 37.76257787754343, 'Shabrakhit': 60.164899014495255, 'Damanhour': 74.90774699269691, 'Desouq': 74.42671019496528, 'KafrElsheikh': 62.865125848431276, 'AlmahallaAlkubra': 49.32533656227367, 'Mansoura': 65.43405302662913, 'Sinbillawain': 57.59447789825328, 'Abushaqq': 64.17257036891797}
            #-----
            # AbuKabir
            ,"AbuKabir"  :  {'Giza': 89.2051005996063, 'Cairo': 85.94349331900679, 'October': 112.50124203536777, 'Madinati': 69.25468502282136, 'Alshuruq': 64.31131485388785, 'Aleubur': 58.25255240844308, 'ShubraAlkhayma': 77.57988521859123, 'Qalyub': 74.86900954340834, 'Smadun': 81.07171778071462, 'Balbis': 4770.884668690537, 'Sadat': 110.06433420044232, 'SirsAlliyan': 74.26628556130807, 'Banha': 
            54.88341145471598, 'MinyaAlqamh': 38.95770002929834, 'Zagzig': 22.397505761446244, 'Alsharqia': 4.191979347025293, 'Menouf': 76.79395244910054, 'ShbeenElkoom': 66.45064298285735, 'AbuKabir': 0.0, 'Alshuada': 76.1313063090384, 'Tala': 70.4674087194158, 'Mtgmer': 38.4004875018059, 'Tanta': 65.13082444890858, 'KafrElzayat': 84.99097069746263, 'Shabrakhit': 97.33407190751112, 'Damanhour': 
            119.62555342635953, 'Desouq': 109.10954339358985, 'KafrElsheikh': 82.74307162759438, 'AlmahallaAlkubra': 56.067821532110486, 'Mansoura': 45.20282060784022, 'Sinbillawain': 26.891104632040992, 'Abushaqq': 13.525355986226062}
            #-----
            # Alshuada
            ,"Alshuada"  :  {'Giza': 70.61226876304738, 'Cairo': 67.56878016982675, 'October': 72.59499799846186, 'Madinati': 90.25574816080825, 'Alshuruq': 86.20397705763116, 'Aleubur': 69.25269540669096, 'ShubraAlkhayma': 62.81806135212791, 'Qalyub': 54.79673296638978, 'Smadun': 29.189826443120786, 'Balbis': 4704.347451512494, 'Sadat': 36.435130791987646, 'SirsAlliyan': 18.65505915024623, 'Banha': 31.47081899351977, 'MinyaAlqamh': 44.51857454355418, 'Zagzig': 59.19529767047279, 'Alsharqia': 80.26981243932394, 'Menouf': 14.827421987682367, 'ShbeenElkoom': 12.276129348737774, 'AbuKabir': 76.1313063090384, 'Alshuada': 0.0, 'Tala': 10.376690277305247, 'Mtgmer': 38.70853647529401, 'Tanta': 23.566893046124186, 'KafrElzayat': 28.25739510954047, 'Shabrakhit': 51.13853814550111, 'Damanhour': 63.829943415459994, 'Desouq': 65.12318425564297, 'KafrElsheikh': 57.593174262705766, 'AlmahallaAlkubra': 49.42538244524603, 'Mansoura': 68.40218894220241, 'Sinbillawain': 63.79982804529204, 'Abushaqq': 72.25770618783953}
            #-----
            # Tala
            ,"Tala"  :  {'Giza': 77.47946962158696, 'Cairo': 74.24753484165666, 'October': 81.89122443978476, 'Madinati': 92.94502786869052, 'Alshuruq': 88.55282518175822, 'Aleubur': 71.87664781247867, 'ShubraAlkhayma': 68.693821077506, 'Qalyub': 60.80647513406898, 'Smadun': 37.96096315114093, 'Balbis': 4713.804523935893, 'Sadat': 45.8777689593016, 'SirsAlliyan': 26.62058421839362, 'Banha': 33.414408294493256, 'MinyaAlqamh': 43.22225023070398, 'Zagzig': 55.80646761640364, 'Alsharqia': 74.50183639520917, 'Menouf': 23.774376827581186, 'ShbeenElkoom': 15.878081283119702, 'AbuKabir': 70.4674087194158, 'Alshuada': 10.376690277305247, 'Tala': 0.0, 'Mtgmer': 32.1387334223862, 'Tanta': 13.190689400141592, 'KafrElzayat': 22.14087309782568, 'Shabrakhit': 44.303442693779296, 'Damanhour': 59.94155450344779, 'Desouq': 58.58119459783821, 'KafrElsheikh': 48.08438539444026, 'AlmahallaAlkubra': 39.125313145528594, 'Mansoura': 58.59740891624238, 'Sinbillawain': 55.48248419888785, 'Abushaqq': 65.13166593810602}
            #-----
            # Mtgmer
            ,"Mtgmer"  :  {'Giza': 76.81415466460162, 'Cairo': 73.2253861102583, 'October': 91.90379722648463, 'Madinati': 76.66428748093982, 'Alshuruq': 71.59892865924623, 'Aleubur': 57.44308036570387, 'ShubraAlkhayma': 65.44776488727419, 'Qalyub': 59.30884870140687, 'Smadun': 51.670072654807996, 'Balbis': 4740.699694300966, 'Sadat': 74.33844683350387, 'SirsAlliyan': 41.87493594912807, 'Banha': 28.831978599041197, 'MinyaAlqamh': 23.373737428025763, 'Zagzig': 27.247971773346787, 'Alsharqia': 42.395026553455835, 'Menouf': 42.894609104603276, 'ShbeenElkoom': 31.090660389080824, 'AbuKabir': 38.4004875018059, 'Alshuada': 38.70853647529401, 'Tala': 32.1387334223862, 'Mtgmer': 0.0, 'Tanta': 27.593314215146314, 'KafrElzayat': 47.649435421751534, 'Shabrakhit': 63.45872658774885, 'Damanhour': 84.30160608658083, 'Desouq': 76.77459143683923, 'KafrElsheikh': 54.73976483528502, 'AlmahallaAlkubra': 30.625845500875005, 'Mansoura': 38.11381539412533, 'Sinbillawain': 26.732000537003668, 'Abushaqq': 33.56006737528961}
            #-----
            # Tanta
            ,"Tanta"  :  {'Giza': 87.32402468486484, 'Cairo': 83.94010084821275, 'October': 94.09658208261975, 'Madinati': 98.01027363147156, 'Alshuruq': 93.2909733828658, 'Aleubur': 77.27258498988395, 'ShubraAlkhayma': 77.65530529250096, 'Qalyub': 70.052716343585, 'Smadun': 50.06591980013875, 'Balbis': 4725.7596434467, 'Sadat': 58.29058945647566, 'SirsAlliyan': 38.50640591090093, 'Banha': 39.98021659453537, 'MinyaAlqamh': 45.26813079517342, 'Zagzig': 54.298533042625856, 'Alsharqia': 68.90990311163374, 'Menouf': 36.30820254064108, 'ShbeenElkoom': 26.38300282865152, 'AbuKabir': 65.13082444890858, 'Alshuada': 23.566893046124186, 'Tala': 13.190689400141592, 'Mtgmer': 27.593314215146314, 'Tanta': 0.0, 'KafrElzayat': 20.061103079131808, 'Shabrakhit': 37.84530256974216, 'Damanhour': 57.20647673927228, 'Desouq': 51.938636370164176, 'KafrElsheikh': 36.58570137884625, 'AlmahallaAlkubra': 26.15620741868789, 'Mansoura': 46.570798845230435, 'Sinbillawain': 46.26274741123253, 'Abushaqq': 57.66759003689013}
            #-----
            # KafrElzayat
            ,"KafrElzayat"  :  {'Giza': 98.72665146595816, 'Cairo': 95.61212158682653, 'October': 99.99271531197103, 'Madinati': 114.92247957853014, 'Alshuruq': 110.45016721332976, 'Aleubur': 93.88418445036015, 'ShubraAlkhayma': 90.45233879340853, 'Qalyub': 82.49092738945215, 'Smadun': 57.32636088268904, 'Balbis': 4714.4649348184375, 'Sadat': 52.39072497635531, 'SirsAlliyan': 46.87968152388293, 'Banha': 55.4778114683448, 'MinyaAlqamh': 63.83300548271568, 'Zagzig': 74.1501376076701, 'Alsharqia': 88.69376040421186, 'Menouf': 43.04166777489593, 'ShbeenElkoom': 37.76257787754343, 'AbuKabir': 84.99097069746263, 'Alshuada': 28.25739510954047, 'Tala': 22.14087309782568, 'Mtgmer': 47.649435421751534, 'Tanta': 20.061103079131808, 'KafrElzayat': 0.0, 'Shabrakhit': 22.88417150962824, 'Damanhour': 38.175990739860346, 'Desouq': 36.91146720535302, 'KafrElsheikh': 33.58481888858865, 'AlmahallaAlkubra': 38.52579760251328, 'Mansoura': 60.743873953018245, 'Sinbillawain': 64.49869119003175, 'Abushaqq': 76.84015493243044}
            #-----
            # Shabrakhit
            ,"Shabrakhit"  :  {'Giza': 121.50461318367941, 'Cairo': 118.35138468699866, 'October': 122.54812354292244, 'Madinati': 135.74016790722334, 'Alshuruq': 131.07194295469563, 'Aleubur': 114.884289525651, 'ShubraAlkhayma': 112.98382006191022, 'Qalyub': 105.07102892138366, 'Smadun': 80.19466157791184, 'Balbis': 4723.210638137342, 'Sadat': 71.39509128105546, 'SirsAlliyan': 69.74285839313808, 'Banha': 76.91741390701416, 'MinyaAlqamh': 83.07212288489647, 'Zagzig': 90.70607427652448, 'Alsharqia': 100.5458893470239, 'Menouf': 65.92501143893085, 'ShbeenElkoom': 60.164899014495255, 'AbuKabir': 97.33407190751112, 'Alshuada': 51.13853814550111, 'Tala': 44.303442693779296, 'Mtgmer': 63.45872658774885, 'Tanta': 37.84530256974216, 'KafrElzayat': 22.88417150962824, 'Shabrakhit': 0.0, 'Damanhour': 23.00900758028727, 'Desouq': 14.310100464205583, 'KafrElsheikh': 22.424500240564, 'AlmahallaAlkubra': 42.89238873996473, 'Mansoura': 63.233142430303005, 'Sinbillawain': 73.07639336803038, 'Abushaqq': 86.92163592176377}
            #-----
            # Damanhour
            ,"Damanhour"  :  {'Giza': 133.71304448693363, 'Cairo': 130.86079839859138, 'October': 129.97253316916112, 'Madinati': 152.88418935209899, 'Alshuruq': 148.48778211849148, 'Aleubur': 131.81088651696464, 'ShubraAlkhayma': 126.55985413313037, 'Qalyub': 118.52820867164621, 'Smadun': 90.93645804606707, 'Balbis': 4707.006171520125, 'Sadat': 72.78106974703117, 'SirsAlliyan': 82.03011743957262, 'Banha': 93.33978666544782, 'MinyaAlqamh': 101.94572919076437, 'Zagzig': 111.38811861423848, 'Alsharqia': 122.96704462854836, 'Menouf': 77.59485929242445, 'ShbeenElkoom': 74.90774699269691, 'AbuKabir': 119.62555342635953, 'Alshuada': 63.829943415459994, 'Tala': 59.94155450344779, 'Mtgmer': 84.30160608658083, 'Tanta': 57.20647673927228, 'KafrElzayat': 38.175990739860346, 'Shabrakhit': 23.00900758028727, 'Damanhour': 0.0, 'Desouq': 18.354008336599268, 'KafrElsheikh': 44.06035876113239, 'AlmahallaAlkubra': 65.86437108341094, 'Mansoura': 86.15382461076436, 'Sinbillawain': 95.91294122602783, 'Abushaqq': 109.62215348757724}
            #-----
            # Desouq
            ,"Desouq"  :  {'Giza': 135.63690273116075, 'Cairo': 132.51323700519703, 'October': 135.80848515943688, 'Madinati': 149.92693279292627, 'Alshuruq': 145.226720638641, 'Aleubur': 129.11265004274762, 'ShubraAlkhayma': 127.23474314454154, 'Qalyub': 119.30605907281382, 'Smadun': 94.01315049156187, 'Balbis': 4725.229008048395, 'Sadat': 82.46001461130572, 'SirsAlliyan': 83.77006658474176, 'Banha': 91.21403525030021, 'MinyaAlqamh': 97.03472860649532, 'Zagzig': 103.95298194696389, 'Alsharqia': 112.09794812076836, 'Menouf': 79.83734117202286, 'ShbeenElkoom': 74.42671019496528, 'AbuKabir': 109.10954339358985, 'Alshuada': 65.12318425564297, 'Tala': 58.58119459783821, 'Mtgmer': 76.77459143683923, 'Tanta': 51.938636370164176, 'KafrElzayat': 36.91146720535302, 'Shabrakhit': 14.310100464205583, 'Damanhour': 18.354008336599268, 'Desouq': 0.0, 'KafrElsheikh': 28.399375049230887, 'AlmahallaAlkubra': 53.40565167141254, 'Mansoura': 71.70746081115082, 'Sinbillawain': 83.83246068939334, 'Abushaqq': 97.97570289988369}
            #-----
            # KafrElsheikh
            ,"KafrElsheikh"  :  {'Giza': 123.82303827315862, 'Cairo': 120.40842811183077, 'October': 129.96843268703725, 'Madinati': 131.03791389331235, 'Alshuruq': 126.05347528406894, 'Aleubur': 111.06936675215762, 'ShubraAlkhayma': 113.90217446041417, 'Qalyub': 106.43542880526633, 'Smadun': 86.03404238109603, 'Balbis': 4744.670067679555, 'Sadat': 85.96994550760769, 'SirsAlliyan': 74.60869890244392, 'Banha': 75.67777756141717, 'MinyaAlqamh': 77.29652347031866, 'Zagzig': 80.81016894821809, 'Alsharqia': 85.40663728718461, 'Menouf': 71.84199861900323, 'ShbeenElkoom': 62.865125848431276, 'AbuKabir': 82.74307162759438, 'Alshuada': 57.593174262705766, 'Tala': 48.08438539444026, 'Mtgmer': 54.73976483528502, 'Tanta': 36.58570137884625, 'KafrElzayat': 33.58481888858865, 'Shabrakhit': 22.424500240564, 'Damanhour': 44.06035876113239, 'Desouq': 28.399375049230887, 'KafrElsheikh': 0.0, 'AlmahallaAlkubra': 26.76144154461341, 'Mansoura': 43.347519750551164, 'Sinbillawain': 56.58141956858564, 'Abushaqq': 70.85431622793034}
            #-----
            # AlmahallaAlkubra
            ,"AlmahallaAlkubra"  :  {'Giza': 105.56525837266625, 'Cairo': 102.01083990176646, 'October': 116.78307540783617, 'Madinati': 107.09683415202487, 'Alshuruq': 101.98751328454517, 'Aleubur': 88.06887257076342, 'ShubraAlkhayma': 94.66694441124467, 'Qalyub': 87.89112768899102, 'Smadun': 73.38253268435378, 'Balbis': 4751.339220058855, 'Sadat': 84.38962434824622, 'SirsAlliyan': 61.95253709497686, 'Banha': 56.435711751155, 'MinyaAlqamh': 53.992830200597155, 'Zagzig': 54.901850475516255, 'Alsharqia': 58.85767192209339, 'Menouf': 60.72739387463376, 'ShbeenElkoom': 49.32533656227367, 'AbuKabir': 56.067821532110486, 'Alshuada': 49.42538244524603, 'Tala': 39.125313145528594, 'Mtgmer': 30.625845500875005, 'Tanta': 26.15620741868789, 'KafrElzayat': 38.52579760251328, 'Shabrakhit': 42.89238873996473, 'Damanhour': 65.86437108341094, 'Desouq': 53.40565167141254, 'KafrElsheikh': 26.76144154461341, 'AlmahallaAlkubra': 0.0, 'Mansoura': 22.23528655984941, 'Sinbillawain': 30.438133366135073, 'Abushaqq': 44.5751088700812}
            #-----
            # Mansoura
            ,"Mansoura"  :  {'Giza': 114.37835860677251, 'Cairo': 110.7931507301216, 'October': 129.90548971364194, 'Madinati': 107.6239954936369, 'Alshuruq': 102.42638061145952, 'Aleubur': 91.12093538186863, 
            'ShubraAlkhayma': 102.78043967811581, 'Qalyub': 97.08079433219568, 'Smadun': 88.43101121710939, 'Balbis': 4772.28906013047, 'Sadat': 104.47167016787013, 'SirsAlliyan': 77.65838175990865, 'Banha': 66.94317000290643, 'MinyaAlqamh': 58.97969560247513, 'Zagzig': 53.05737736272525, 'Alsharqia': 46.66372173055667, 'Menouf': 77.47061255157632, 'ShbeenElkoom': 65.43405302662913, 'AbuKabir': 45.20282060784022, 'Alshuada': 68.40218894220241, 'Tala': 58.59740891624238, 'Mtgmer': 38.11381539412533, 'Tanta': 46.570798845230435, 'KafrElzayat': 60.743873953018245, 'Shabrakhit': 63.233142430303005, 'Damanhour': 86.15382461076436, 'Desouq': 71.70746081115082, 'KafrElsheikh': 43.347519750551164, 'AlmahallaAlkubra': 22.23528655984941, 'Mansoura': 0.0, 'Sinbillawain': 19.18160725429288, 'Abushaqq': 31.77426662732486}
            #-----
            # Sinbillawain
            ,"Sinbillawain"  :  {'Giza': 98.82070938950687, 'Cairo': 95.27523801707338, 'October': 117.01154122163419, 'Madinati': 88.91826688569559, 'Alshuruq': 83.73199848364571, 'Aleubur': 73.27859926647304, 'ShubraAlkhayma': 87.02781605173956, 'Qalyub': 82.07660444640301, 'Smadun': 78.23717994288928, 'Balbis': 4767.279328494021, 'Sadat': 100.10133187731772, 'SirsAlliyan': 68.60680197745094, 'Banha': 54.03459745566376, 'MinyaAlqamh': 43.017689739255864, 'Zagzig': 34.47372259990528, 'Alsharqia': 29.05476366186617, 'Menouf': 69.53452985296211, 'ShbeenElkoom': 57.59447789825328, 'AbuKabir': 26.891104632040992, 'Alshuada': 63.79982804529204, 'Tala': 55.48248419888785, 'Mtgmer': 26.732000537003668, 'Tanta': 46.26274741123253, 'KafrElzayat': 64.49869119003175, 'Shabrakhit': 73.07639336803038, 'Damanhour': 95.91294122602783, 'Desouq': 83.83246068939334, 'KafrElsheikh': 56.58141956858564, 'AlmahallaAlkubra': 30.438133366135073, 'Mansoura': 19.18160725429288, 'Sinbillawain': 
            0.0, 'Abushaqq': 14.279190979788414}
            #-----
            # Abushaqq
            ,"Abushaqq"  :  {'Giza': 96.33877254683857, 'Cairo': 92.91369333619416, 'October': 117.40872251481817, 'Madinati': 80.70769580163164, 'Alshuruq': 75.62684354566836, 'Aleubur': 67.5424927864806, 'ShubraAlkhayma': 84.51446244031199, 'Qalyub': 80.70130664073633, 'Smadun': 82.07850061195875, 'Balbis': 4772.620143804295, 'Sadat': 107.76543619952588, 'SirsAlliyan': 73.75213931627488, 'Banha': 
            56.319115763074144, 'MinyaAlqamh': 42.20876972585191, 'Zagzig': 28.724881823605703, 'Alsharqia': 14.981021315640053, 'Menouf': 75.51628299794885, 'ShbeenElkoom': 64.17257036891797, 'AbuKabir': 13.525355986226062, 'Alshuada': 72.25770618783953, 'Tala': 65.13166593810602, 'Mtgmer': 33.56006737528961, 'Tanta': 57.66759003689013, 'KafrElzayat': 76.84015493243044, 'Shabrakhit': 86.92163592176377, 'Damanhour': 109.62215348757724, 'Desouq': 97.97570289988369, 'KafrElsheikh': 70.85431622793034, 'AlmahallaAlkubra': 44.5751088700812, 'Mansoura': 31.77426662732486, 'Sinbillawain': 14.279190979788414, 'Abushaqq': 0.0}
            }
#--------------
            from queue import PriorityQueue
            priority_queue, visited = PriorityQueue(), {}
            priority_queue.put((straight_line[destination][source], 0, source, [source]))
            visited[source] = straight_line[destination][source]
            while not priority_queue.empty():
                (heuristic, cost, vertex, path) = priority_queue.get()
                if vertex == destination:
                    return heuristic, cost, path
                for next_node in GRAPH[vertex].keys():
                    current_cost = cost + GRAPH[vertex][next_node]
                    heuristic = current_cost + straight_line[destination][next_node]
                    if not next_node in visited or visited[next_node] >= heuristic:
                        visited[next_node] = heuristic
                        priority_queue.put((heuristic, current_cost, next_node, path + [next_node]))
        def Affs(source,goal):
            """Main function"""
            if source not in GRAPH or goal not in GRAPH:
                print("-----------------------------")
                print('ERROR: CITY DOES NOT EXIST.')
                print("-----------------------------")
            else:
                print("-----------------------------")
                print('\nOPTIMAL PATH:')
                heuristic, cost, optimal_path = a_star(source, goal)
                print('HEURISTIC =', heuristic,' and ','PATH_COST =', cost)
                print(' -> '.join(city for city in optimal_path))
                print("-----------------------------")
        h,c,p=a_star(x,y)
        soli =Affs(x,y)
# -------------------------
        # point x,y
        Giza = (340, 615)
        Cairo = (345, 589)
        October = (250, 625)
        Madinati = (490, 570)
        Alshuruq = (490, 544)
        Aleubur = (430, 520)
        ShubraAlkhayma = (350, 570)
        Qalyub = (344, 533)
        Smadun = (240, 465)
        Balbis = (477, 447)
        Sadat = (100, 442)
        SirsAlliyan = (249, 432)
        Banha = (330, 415)
        MinyaAlqamh = (390, 390)
        Zagzig = (443, 364)
        Alsharqia = (533, 355)
        Menouf = (228, 402)
        ShbeenElkoom = (266, 375)
        AbuKabir = (515, 316)
        Alshuada = (226, 364)
        Tala = (243, 329)
        Mtgmer = (357, 309)
        Tanta = (262, 280)
        KafrElzayat = (195, 265)
        Shabrakhit = (160, 180)
        Damanhour = (68, 175)
        Desouq = (130, 135)
        KafrElsheikh = (247, 149)
        AlmahallaAlkubra = (324, 205)
        Mansoura = (408, 170)
        Sinbillawain = (432,240)
        Abushaqq = (480, 270)
# -----------------
        dictPoint = {
                    'Giza': (340, 615),
                    'Cairo': (345, 589),
                    'October': (250, 625),
                    'Madinati': (490, 570),
                    'Alshuruq': (490, 544),
                    'Aleubur': (430, 520),
                    'ShubraAlkhayma': (350, 570),
                    'Qalyub': (345, 540),
                    'Smadun': (240, 465),
                    'Balbis': (477, 447),
                    'Sadat': (100, 442),
                    'SirsAlliyan': (249, 432),
                    'Banha': (330, 415),
                    'MinyaAlqamh': (390, 390),
                    'Zagzig': (443, 364),
                    'Alsharqia': (533, 355),
                    'Menouf': (228, 402),
                    'ShbeenElkoom': (266, 375),
                    'AbuKabir': (515, 316),
                    'Alshuada': (226, 364),
                    'Tala': (243, 329),
                    'Mtgmer': (357, 309),
                    'Tanta': (262, 280),
                    'KafrElzayat': (195, 265),
                    'Shabrakhit': (160, 180),
                    'Damanhour': (68, 175),
                    'Desouq': (130, 135),
                    'KafrElsheikh': (247, 149),
                    'AlmahallaAlkubra': (324, 205),
                    'Mansoura': (408, 170),
                    'Sinbillawain': (432,240),
                    'Abushaqq': (480, 270)
         } 
# ---------------------
        y = len(p)
        reem = "F:\AI-opencv\maps\SearchMap\map.jpg"
        img = cv2.imread(reem)
        x = 0
        while x != (y-1):
            cv2.line(img, dictPoint[p[x]],dictPoint[p[x+1]], (150, 10, 150), 2)
            cv2.circle(img,dictPoint[p[x]],3,(26, 26, 0),4)
            cv2.circle(img,dictPoint[p[x+1]],3,(26, 26, 0),4)
            x += 1
        exit
        cv2.imshow("SearchLocation", img)
        cv2.waitKey(0)