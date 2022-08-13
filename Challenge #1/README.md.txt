Challenge #1

A 3-tier environment is a common setup. Use a tool of your choosing/familiarity create these resources. Please remember we will not be judged on the outcome but more focusing on the approach, style and reproducibility.


Template Solution(Azure Portal):

1. Create 2 Windows Virtual Machine in a Resource Group along with Virtual network in availabality set

2. Validate that the VM works through RDP

3. Create Public Load Balancer for the above 2 Windows VM considered as frontend servers

4. Create 2 Linux Virtual Machines in the same respurce group considered for Backend servers in another availabality set

5. Validate the Linux VM

6. Create Internal Load Balancer for the 2 Linux Machine in Backend Pool

7. Create one SQL Database and set replicas as a secondary database

8. Setup Automatic failover to a Secondary Region for backup in case

9. Install IIS Web Server on the Windows Virtual Machines

10. Configure Front-End Load Balancer for Public Traffic and then similary Configure Back-End Load Balancer for Internal Traffic.



