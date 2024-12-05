import math
import time
import socket 

HOST = "127.0.0.1"
PORT = 6432

h_t_array = []
running = True


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    #new socket is after a accept function
    conn,addr = s.accept()
    with conn:
        G = 6.674*pow(10,-11)
        earth_mass = 5.972*pow(10,24)
        obj_wheight = input("The wheight of the rocket in kg:")
        obj_wheight = int(obj_wheight)  
        earth_radius = 6378*pow(10,3)
        obj_distance = 0
        F = G*(earth_mass+obj_wheight)/pow(earth_radius+obj_distance*pow(10,3),2)

        #given some calculation the g for 100 km of earths radius is =~ 9.49
        Fgravity = 9.49
        Ftrhust = input("Force of trhust in Newtons:")
        Ftrhust = int(Ftrhust)
        Fnet = Ftrhust-Fgravity

        print(Fnet)

        a = Fnet/obj_wheight


        run_time = input("Time here you wanna see where the rocket is in seconds:")
        run_time = int(run_time)
        for i in range(run_time):
            h_t = 0+0+1/2*a*pow(i,2)
            print(f"ALTITUDE IN METERS {h_t}")
            h_t_array.append(str(h_t).encode())
        print(f"connected to addr:{addr}")
        while running:
            for data in h_t_array:
                conn.sendall(data)
                time.sleep(1)
            conn.sendall(b"END")
            running = False
    print(f"Data recived from client:{data}")


