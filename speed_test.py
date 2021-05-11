import speedtest
from math import exp
print("wait 25 to 32 second to get results")

option = int(input('''What speed do you want to test:  
  
1) Download Speed  
  
2) Upload Speed  
  
3) Ping 
  
Your Choice: '''))


st = speedtest.Speedtest()
st.get_best_server()
# Get download speed
if option == 1:
    speed_download = st.download()
    d = speed_download // (8*exp(1)+6)
    print(f"download test is : {d} megabyte/s")    
#Get Upload speed
elif option == 2:
    speed_upload = (st.upload()) 
    u = speed_upload //(8*exp(1)+6)
    print(f"upload speed is : {u} megabits/s")
elif option == 3:
    servernames =[]  
  
    st.get_servers(servernames)  
  
    print(st.results.ping)  

else: 
    print('please enter the correct choice')
