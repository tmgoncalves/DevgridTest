<h3>DevGrid Tech Test</h3>

<p>The main objetive for this test consist in design and building a service that collects data from an Open Weather API and store it as a JSON data.</p>
<p>The Test gives an id of each city and the application must to search its id at the OpenWeather Web site, using OpenWeather API.</p>

<h3>Steps to run the application</h3>

To run the application, it needs to have docker installed at the computer. Docker can be downloaded in the link:

https://www.docker.com/

<p>To download the imagem, opens the terminal and puts the command:</p>

`docker pull tmgoncalves/extraction`

<p>The next step is running the application:</p>

`docker run tmgoncalves/extraction`

All data will be extracted in JSON format and printed at the screen.

The application takes about 4 or 5 minutes to extract the information. It happens due to the maximum time established by OpenWeather in 60 JSON data format per minutes.
