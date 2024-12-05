import math
import time
import asyncio
from websockets.asyncio.server import serve


def calc_height():
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
    
    h_t_array = []
    for i in range(run_time):
        h_t = 0+0+1/2*a*pow(i,2)
        print(f"ALTITUDE IN METERS {h_t}")
        h_t_array.append(str(h_t).encode())             
    return h_t_array

async def send_height(websocket):
    h_t_array = calc_height()
    for h_t in h_t_array:
        await websocket.send(h_t)
        time.sleep(1)
    
async def main():
    async with serve(send_height,"localhost",65432):
        await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())
       


