# DSYS601_Project2
Project 2 files

In this repository are two files - an assessment_code.py Python file and a network_equipment.json file.
These files are the docker-based "application" you will deploy using a Jenkins build job, running on a local Docker instance you created with Terraform, earlier.
Note that python3 and Flask will need to be installed - the http app will run on TCP port 5050.

One you have deployed the app, you will need to create another Jenkins test job (and any testing code) to test the app deployed correctly.
Put both of these jobs (the build and the test job) into a pipeline.
At present, we will get you to run the pipeline manually, but if you wish, you can explore how to get git to trigger the Jenkins job based on changes in the code.
(Copy the files to your own git repository and then change them to trigger the process).

You will then write a python script to interrogate your API to :
1. List all equipment.
2. Change Cisco switches with a firmware version of less than 12.2 to have a firmware version of 15.4
3. Update the API with your changes.

Have fun!
