Task 1/Task 2: please see hw3_TianhaoWu.pdf


Task 3: MAC Learning Controller
Questions:
1. Describe how the above code works, such as how the "MAC to Port" map is established. You could use a ‘ping’ example to describe the establishment process (e.g., h1 ping h2).
        
When "h1 ping h2", _handle_PacketIn() will called act_like_switch(). So there are two cases: 
(a) if source MAC already been known by "MAC to Port" map
(b) if destination MAC already been stored by "MAC to Port" map. 

For (a), it will estabalish the map first. If the source MAC is unkown, it will add the MAC and its port into the map(key is MAC, value is the port). 
For (b), it depends on how the packet is sent. If the destination is known, it just sends the packet to the destination, or if it's unknown, it will do the same thing as the ac_like_hub()


2. (Comment out all prints before doing this experiment) Have h1 ping h2, and h1 ping h8 for 100 times (e.g., h1 ping -c100 p2).
        a. How long did it take (on average) to ping for each case?
        b. What is the minimum and maximum ping you have observed?
"h1 ping -c100 h2":
--- 10.0.0.2 ping statistics ---
100 packets transmitted, 100 received, 0% packet loss, time 93845ms
rtt min/avg/max/mdev = 1.758/16.197/769.375/65.472 ms
"h1 ping -c100 h8"
--- 10.0.0.8 ping statistics ---
100 packets transmitted, 100 received, 0% packet loss, time 88657ms
rtt min/avg/max/mdev = 7.192/15.785/21.169/4.973 ms


        c. Any difference from Task 2 and why do you think there is a change if there is?
        Task3's results are improved slightly than Task 2. The reason might be that the "MAC to Port" map could help us reduce forwarding time especailly when there are a lot of switches in the process, like the h1 ping h8. After multiple times, the map could learn and store both source and destination MACs in its forwarding table, so it can send the pakcet to the destination directly.


3. Q.3 Run “iperf h1 h2” and “iperf h1 h8”.
        a. What is the throughput for each case?
mininet> iperf h1 h2
*** Iperf: testing TCP bandwidth between h1 and h2 
*** Results: ['6.13 Gbits/sec', '6.10 Gbits/sec']
mininet> iperf h1 h8
*** Iperf: testing TCP bandwidth between h1 and h8 
*** Results: ['3.01 Gbits/sec', '2.85 Gbits/sec']
        b. What is the difference from Task 2 and why do you think there is a change if there is?
        The difference between Task 2 and 3 is not distinct, but Task 3 also has a small improvement. The reason might be the same as question 2, the usage of "MAC to Port" map can improve the performance and aid the efficiency.
