import requests
import time
import threading
from ..internal.motors import move, stop, get_distance, servo, bip, FREQUENCIA_AGUDO, FREQUENCIA_GRAVE, front, back, left, right


time.sleep(3)
servo(90)
bip(FREQUENCIA_AGUDO)
time.sleep(0.1)
bip(FREQUENCIA_AGUDO)



while True:
            
            move(front)
            
            
            
            distance = get_distance()
            print(distance)
            print(f"Distância: {distance} cm")
            if distance == None:
                    stop()
                    
                    bip(FREQUENCIA_AGUDO)
                    stop()
                    while True:
                        distance = get_distance()
                        bip()
                        time.sleep(0.4)
                        if distance != None:
                            bip()
                            time.sleep(0.1)
                            bip()
                            ALARM = False
                            break
            distance = int(distance)
            
            
           
                    
                    
            
            if distance <= 40:
                bip(FREQUENCIA_AGUDO)
                print(stop())
                time.sleep(0.2)
                move(back)
                time.sleep(1)
                stop()

                
                servo(45)
                time.sleep(0.8)
                distance_45 = get_distance()
               
                servo(135)
                time.sleep(0.8)
                distance_135 = get_distance()
                
                
                if distance_45 <= distance_135:
                    servo(90)
                    move(left)
                    time.sleep(1.25)
                    
                else:
                    servo(90)
                    move(right)
                    time.sleep(1.25)
                    
                 
    



