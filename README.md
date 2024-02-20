## Installation and Running Instructions

### Cloning the Repository

1. Open your terminal.

2. Execute the following command to clone the repository:
   ```bash
   git clone https://github.com/amaxcz/job2.git
   ```
   or 

   ```bash
   git clone git@github.com:amaxcz/job2.git
   ```



3. Navigate to the project directory:
   ```bash
   cd job2
   ```

### Building and Running the Container from Source Code

#### Build and run the container from the source code

1. Make sure Docker and Docker Compose are installed on your system.

2. Execute the following command to build and run the container:
   ```bash
   sudo docker-compose up --build
   ```

   This will create and start the container with the web application.

3. Open your browser and go to http://127.0.0.1:8080 to view your web application.

#### Running the Container from Docker Hub

1. Ensure Docker and Docker Compose are installed on your system.

2. Execute the following commands to pull and run the container from Docker Hub:
   ```bash
   sudo docker-compose pull
   sudo docker-compose up
   ```

   This will download the pre-built container from Docker Hub and start it.

3. Open your browser and go to http://127.0.0.1:8080 to view your web application.

### Pulling the Container from Docker Hub

To pull the container directly from Docker Hub using the command line, you can use the following command:

```bash
sudo docker pull amaxcz/job2-web_app:1.0
```

This command will download the specified container image (`amaxcz/job2-web_app:1.0`) from Docker Hub to your local machine.

After pulling the image, you can run it using the following command:

```bash
sudo docker run -p 8080:8080 amaxcz/job2-web_app:1.0
```

This will start the container and map port 8080 on your local machine to port 8080 inside the container.


### Accessing the Web Application

After successfully running the Docker container, you can access the web application by opening your browser and navigating to [http://127.0.0.1:8080](http://127.0.0.1:8080).

You will be greeted with a blank page containing three buttons:

1. **Crawl:** Click this button to initiate the data crawling process. Please wait for approximately 10 seconds as the data is extracted and loaded into the database.

2. **Clear:** This button clears all records from the database.

3. **Refresh:** Clicking this button simply refreshes the page.

Feel free to interact with these buttons and explore the functionality of the web application.
