from os import path
import queue
from tkinter import *
from tkinter.constants import S
import cv2
from numpy import array
from queue import Queue
import time

class my_Bridth:
    def Bridth_1(x,y):
        
        
        graph = {
            

            'Giza': ['October', 'Cairo', 'Madinati'],
            'October': ['Giza', 'Cairo'],
            'Cairo': ['Giza', 'October', 'Madinati', 'ShubraAlkhayma'],
            'Madinati': ['Giza', 'Alshuruq', 'Cairo'],
            'Alshuruq': ['Madinati', 'Aleubur'],
            'Aleubur': ['Alshuruq', 'Balbis', 'ShubraAlkhayma'],
            'ShubraAlkhayma': ['Cairo', 'Qalyub'],
            'Qalyub': ['ShubraAlkhayma', 'Smadun', 'Banha', 'Balbis'],
            'Smadun': ['Qalyub', 'Sadat', 'SirsAlliyan'],
            'Banha': ['Qalyub', 'SirsAlliyan', 'ShbeenElkoom', 'Tanta', 'Mtgmer', 'MinyaAlqamh'],
            'Balbis': ['Qalyub', 'Aleubur', 'Alshuruq', 'MinyaAlqamh', 'Zagzig', 'Alsharqia'],
            'Sadat': ['Smadun', 'SirsAlliyan', 'Menouf'],
            'SirsAlliyan': ['Smadun', 'Sadat', 'Menouf', 'Banha'],
            'ShbeenElkoom': ['Banha', 'SirsAlliyan', 'Menouf', 'Alshuada', 'Tala'],
            'Tanta': ['Banha', 'Tala', 'KafrElzayat', 'KafrElsheikh', 'AlmahallaAlkubra'],
            'Mtgmer': ['Banha', 'Zagzig', 'AlmahallaAlkubra', 'Mansoura', 'Sinbillawain', 'Abushaqq'],
            'MinyaAlqamh': ['Banha', 'Balbis', 'Zagzig'],
            'Zagzig': ['Balbis', 'MinyaAlqamh', 'Mtgmer', 'Sinbillawain', 'AbuKabir', 'Alsharqia'],
            'Alsharqia': ['Balbis', 'Zagzig', 'AbuKabir'],
            'Menouf': ['SirsAlliyan', 'Sadat', 'ShbeenElkoom', 'Alshuada'],
            'Alshuada': ['ShbeenElkoom', 'Menouf', 'Tala'],
            'Tala': ['Alshuada', 'ShbeenElkoom', 'Tanta'],
            'KafrElzayat': ['Tanta', 'Damanhour', 'Shabrakhit'],
            'KafrElsheikh': ['Tanta', 'AlmahallaAlkubra', 'Shabrakhit', 'Desouq'],
            'AlmahallaAlkubra': ['Tanta', 'KafrElsheikh', 'Mansoura', 'Sinbillawain', 'Mtgmer'],
            'Mansoura': ['Mtgmer', 'AlmahallaAlkubra', 'Sinbillawain'],
            'Sinbillawain': ['Mansoura', 'Mtgmer', 'Zagzig', 'AlmahallaAlkubra', 'Abushaqq'],
            'Abushaqq': ['Mtgmer', 'Sinbillawain', 'AbuKabir'],
            'AbuKabir': ['Alsharqia', 'Zagzig', 'Abushaqq'],
            'Damanhour': ['KafrElzayat', 'Shabrakhit', 'Desouq'],
            'Shabrakhit': ['KafrElzayat', 'Damanhour', 'Desouq', 'KafrElsheikh'],
            'Desouq': ['Damanhour', 'Shabrakhit', 'KafrElsheikh'],

         }


        def bfs(graph, start, goal):
            visited = []
            queue = [[start]]
            while queue:
                path = queue.pop(0)
                node = path[-1]
                if node in visited:
                    continue
                visited.append(node)
                if node == goal:
                    return path
                else:
                    adjacent_node = graph.get(node, [])
                    for node2 in adjacent_node:
                        new_path = path.copy()
                        new_path.append(node2)
                        queue.append(new_path)
                # return queue

        solution = bfs(graph,x,y)
        print("solution is ", queue)

        # -------------------------
        # ------------------
        # point x,y
        ashmun = (238, 236)
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
        # # # -----------------
        dictPoint = {'Giza': (340, 615),
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
                    }  # ---------------------
        y = len(solution)

        print(y)
        for i in range(0, y):
            print(dictPoint[solution[i]])
        reem = "F:\AI-opencv\maps\SearchMap\map.jpg"
        img = cv2.imread(reem)

        x = 0
        while x != (y-1):

            cv2.line(img, dictPoint[solution[x]],dictPoint[solution[x+1]], (150, 10, 150), 2)
            cv2.circle(img,dictPoint[solution[x]],3,(26, 26, 0),4)
            cv2.circle(img,dictPoint[solution[x+1]],3,(26, 26, 0),4)
            x += 1

        exit


        cv2.imshow("SearchLocation", img)

        cv2.waitKey(0)

# # ------------------------------------------
