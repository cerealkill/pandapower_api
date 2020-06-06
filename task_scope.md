
You need to create a script that will run a simple power flow calculation using pandapower https:// github.com/e2nIEE/pandapower and present its results via a REST API. You can find the Python module with the simulation code that you need to use here https://github.com/gridsingularity/interview_tasks/blob/master/api_engineer/test_sim.py. You do not need to create your own simulation script, you can use the one provided (test_sim.py), and only expose its results via a REST API. The only function that you will need to use is the run_simulation function, which performs the power flow calculation and returns a tuple, containing the active and reactive power of the load. The API that you will create will use these 2 values (active and reactive power).

The API needs to expose 3 endpoints:
1. POST request that launches the simulation using the aforementioned Python module. The response should include the active and reactive power of the load in JSON format
2. GET request that reads the active power of the previously executed simulation 
3. GET request that reads the reactive power of the previously executed simulation 

You can use any Python framework you like for the REST API (Flask, DRF, Bottle). 

Finally, a Dockerfile has to be created that would install all the dependencies automatically and serve the API once the container is started. 
