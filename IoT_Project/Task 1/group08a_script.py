import numpy as np
import paho.mqtt.client as paho
import threading
import time

# Server information
broker = '5g-vue.projects.uom.lk'
port = 1883
topic = "/group08a"
client_id = 'group8'
username = 'iot_user'
password = 'iot@1234'


def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =", str(message.payload.decode("utf-8")))
  

client = paho.Client(client_id)
client.username_pw_set(username, password)

client.on_message = on_message

print("connecting to broker ", broker)
client.connect(broker)

client.loop_start()  # start loop to process received messages

#Publishing Topic names
co1_topic = topic + "/co01"
co2_topic = topic + "/co02"

mok1_topic = topic + "/mok01"
mok2_topic = topic + "/mok02"

prs_topic = topic + "/prs"

ocd1_topic = topic + "/ocd01"
ocd2_topic = topic + "/ocd02"


pcd1_topic = topic + "/pcd01"
pcd2_topic = topic + "/pcd02"


lvl1_topic = topic + "/lvl01"
lvl2_topic = topic + "/lvl02"


gfc_topic = topic + "/gfc"


# lets give intial values in an array
# order [co2],[smoke],[pressure],[occupancy ],[PCD],[Level],[fuel level capacity]
in_it=[300,400,0,0,700,0,0,3,12,80,90,200]

topic_list=[co1_topic,co2_topic,mok1_topic,mok2_topic,prs_topic,ocd1_topic,ocd2_topic,pcd1_topic,pcd2_topic,lvl1_topic,lvl2_topic,gfc_topic]

period_list=[15,15,60,60,45,60,60,10,10,45,45,60] #insecods

#period is listed, can also provide any number you want. The numbers are starting from 0.
#flag is used to take True if periodic , false if only one time.

def thread_function_co2(period,number):
    rng = np.random.default_rng()
    val = in_it[number]

    while True:
      rand_num = rng.integers(low=-100, high=100, size=1)
      val = val + 1.0* rand_num[0]
        
      if val<200 :
        val=250
      if val>2000 :
        val=1600
        #publish value
      client.publish(topic_list[number], int(val))
      print(topic_list[number], val)

      in_it[number]=val
      
      if val>1000: # crowded
        thread_function_smk(period_list[number+2],number+2,False)
        
      if val>1500: #smoke
        thread_function_ocd(period_list[number+5],number+5,False)
        
      time.sleep(period)

def thread_function_smk(period,number,flag):
    rng = np.random.default_rng()
    val = in_it[number]
    if flag== False:
      rand_num = rng.integers(low=0, high=1, size=1)
      val = int(1.0* rand_num[0])
      if val<0: # redundant 
        val=0
        #publish value
      in_it[number]=val

      client.publish(topic_list[number], int(val))
      print(topic_list[number], val)
      
      time.sleep(period)

    else:
      while True:
        rand_num = rng.integers(low=0, high=1, size=1) # will change with proper istribution randomness
        val = int(1.0*rand_num[0])
        if val<0:
          val=0
        #publish value
        in_it[number]=val
        client.publish(topic_list[number], int(val))
        print(topic_list[number], val)
        
        time.sleep(period)

def thread_function_ocd(period,number,flag):
    rng = np.random.default_rng()
    val = in_it[number]
    
    if flag==False:
      rand_num = rng.integers(low=0, high=1, size=1)
      val = int(1.0* rand_num[0])
      in_it[number]=val
      
      if val<0: #redundand
        val=0
        #publish value
      
      client.publish(topic_list[number], int(val))
      print(topic_list[number], val)
      #
      time.sleep(period)
    else:
      while True:
        rand_num = rng.integers(low=0, high=1, size=1)
        val = int(1.0 * rand_num[0])
        
        if val<0:
          val=0
        #publish value
        
        client.publish(topic_list[number], int(val))
        print(topic_list[number], val)
        in_it[number]=val
        
        time.sleep(period)

def thread_function_prs(period,number):
    rng = np.random.default_rng()
    val = in_it[number]

    while True:
      rand_num = rng.integers(low=-5, high=5, size=1) #do not chnage that fast
      val = val + 1.0* rand_num[0]
        
      if val<500: # unusual to have smaller values than this reagion
        val=500 # normal room value
      if val>1000:
        val=900
      
        #publish value
      client.publish(topic_list[number], int(val))
      print(topic_list[number], val)
      
      in_it[number]=val
        
      time.sleep(period)

def thread_function_pcd(period,number):
    rng = np.random.default_rng()
    val = in_it[number]

    while True:
      rand_num = rng.integers(low=-2, high=3, size=1) #do not chnage that fast
      val = val + 1.0 * rand_num[0]
        
      if val<0: # unusual to have smaller values than this reagion
        val=0 # normal room value
        #publish value
      client.publish(topic_list[number], int(val))
      print(topic_list[number], val)

      in_it[number]=val
        
      time.sleep(period)


def thread_function_lvl(period,number):
    rng = np.random.default_rng()
    val = in_it[number]

    while True:
      rand_num = rng.integers(low=-2, high=6, size=1) #do not chnage that fast
      val = val + 1.0 * rand_num[0]
        
      if val<0: # unusual to have smaller values than this reagion
        val=0 # normal room value
      if val>500:
        val=500
        #publish value
      
      client.publish(topic_list[number], int(val)) 
      print(topic_list[number], val)

      in_it[number]=int(val)

      time.sleep(period)

def thread_function_gfc(period,number):
    rng = np.random.default_rng()
    val = in_it[number]

    while True:
      rand_num = rng.integers(low=-2, high=8, size=1) #do not chnage that fast
      val = val + 1.0* rand_num[0]
        
      if val<0: # unusual to have smaller values than this reagion
        val=0 # normal room value
      if val>600:
        val=600
      
      #publish value
      
      client.publish(topic_list[number], int(val)) 
      print(topic_list[number], val)
      
      in_it[number]=val
        
      time.sleep(period)

if __name__ == '__main__':
    d1 = threading.Thread(target=thread_function_co2, args=(period_list[0],0))
    d2 = threading.Thread(target=thread_function_co2, args=(period_list[1],1))
    d3 = threading.Thread(target=thread_function_smk, args=(period_list[2],2,True))
    d4 = threading.Thread(target=thread_function_smk, args=(period_list[3],3,True))
    d5 = threading.Thread(target=thread_function_prs, args=(period_list[4],4))
    d6 = threading.Thread(target=thread_function_ocd, args=(period_list[5],5,True))
    d7 = threading.Thread(target=thread_function_ocd, args=(period_list[6],6,True))
    d8 = threading.Thread(target=thread_function_pcd, args=(period_list[7],7))
    d9 = threading.Thread(target=thread_function_pcd, args=(period_list[8],8))
    d10 = threading.Thread(target=thread_function_lvl, args=(period_list[9],9))
    d11 = threading.Thread(target=thread_function_lvl, args=(period_list[10],10))
    d12 = threading.Thread(target=thread_function_gfc, args=(period_list[11],11))

    d1.setDaemon(True)
    d2.setDaemon(True)
    d3.setDaemon(True)
    d4.setDaemon(True)
    d5.setDaemon(True)
    d6.setDaemon(True)
    d7.setDaemon(True)
    d8.setDaemon(True)
    d9.setDaemon(True)
    d10.setDaemon(True)
    d11.setDaemon(True)
    d12.setDaemon(True)
    

    d1.start()
    d2.start()
    d3.start()
    d4.start()
    d5.start()
    d6.start()
    d7.start()
    d8.start()
    d9.start()
    d10.start()
    d11.start()
    d12.start()

    while True:
      pass


##### Diron A.G.            - 190149X
##### Mathotaarachchi M.M.  - 190338D
##### Udara A.G.N.          - 190636M