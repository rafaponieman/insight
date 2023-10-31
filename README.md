# Insight
Insight is a platform designed for retrospective and real-time analysis of blockchain data. Developed for Chainbase & Developer DAO hackathon.

## Key concepts
Insight introduces the concept of *Seekers*: any program or orchestrated system that can be run on a dataset to produce insights. *Seekers* can implement ML algorithms, statistical analysis, or any other imaginable strategy. *Seekers* can conduct *Runs*, in order to analyze data and produce results.

## Data source
*Seekers* could consume blockchain data by examining the blockchain directly. However, that would imply an enormous effort for any implementation, and would bring no added benefit. For this reason, Insight provides access to [Chainbase](https://chainbase.com/)'s data, which has already been gathered, extracted and transformed into an easily accessible format. Furthermore, in the future, *Seekers* will be able to consume live data as it is generated.

## Operation
The current version provides a sample built in seeker, that simulates processing by introducing a 10 second delay, and doesn't generate any output.

Using this seeker, retrospective *Runs* can be initiated, on a select portion of data. The current version specifically provides volume and price data for SushiSwap's LINK/WETH pool. It was chosen because it provides this data uninterruptedly for a meaningful amount of time.

In the future, *Runs* would generate output *Events* along with a text log. Events would contain information associated with a timestamp, which will be visualized charted along with some of the source data on the completed Run's page.

## Proof of concept
I developed this entire project by myself, in two days, which is all the time I had available. My goal was to reach the most basic proof of concept, which would have included a real *Seeker*, which could, for example, calculate a Simple Moving Average for a dataset, and generate events from points in which the SMA is crossed. Also, the output data would be presented in the frontend with a chart and an event list. If I had had even more time, I would have loved to implement a ML algorithm that would also involve adding *Training* capabilities to the platform.

## Technologies
The application consists of four parts:
- UI: Insight's frontend, built with Vue.js and Nuxt.
- API: written in Python, powered by Django & Django REST Framework.
- Internal admin CRUD: standard Django admin interface.
- Task runners: one or more Celery workers constantly pull pending Runs from a queue, and execute them asynchronously.

Additionally, SQLite was used for the main DB, and Redis to store the task queue. In production, PostgreSQL would be used instead of SQLite.


## Scope of implementation
- The frontend presents a listing of Seekers (that can be created from the Django admin).
- Runs can be visualized on a listing, and new Runs can be added from the UI.
- If the Celery task runner is spun up, it will process a Run and update it's state.
- The task runner will fetch data from Chainbase's indexer through GraphQL, and provide it to the Seeker.

## Installation

### Project setup
1. Clone the repository to your development computer.
2. Install Redis server, Python 3, Node.js v18 or higher and Yarn or NPM.

### API setup
1. Enter the app folder and create a Virtualenv, with your preferred tool, or Python's built-in venv:  
    ```  
    python -m venv .venv
	source .venv/bin/activate
    ```
2. Install requirments
    ```
    pip install -r requirements.txt
    ```
3. Create a local settings file. Edit it and add your Chainbase API Key.
	```
	cp insight/settings/local.example.py insight/settings/local.py
	```
4. Run DB migrations
    ```
    python manage.py migrate
    ```
5. Create a superuser to access the internal admin interface
    ```
    python manage.py createsuperuser
    ```
6. Start the development server
    ```
    python manage.py runserver
    ```
7. On another shell session, activate the virtual env and start the Celery task runner
    ```
    celery -A insight worker -l INFO
    ```
8. Access the internal admin interface at [http://localhost:8000/admin/](http://localhost:8000/admin/) and create at least one Seeker.

Alternatively, the application can also be run without the need for Celery or Redis, running tasks synchronously by changing the CELERY_ALWAYS_EAGER setting in local.py to True.

### Frontend setup
1. Enter the UI folder and run `yarn` or `npm install`
2. Create a .env file with the following contents:
    ```  
    NUXT_PUBLIC_API_ROOT=http://localhost:8000
    ```
3. Start the development server with `yarn dev` or `npm run dev`
4. Access the frontend UI at [http://localhost:3000](http://localhost:3000)

## Future work
- Insight would be an open source software platform that anyone can download and install in their system, or self-host.
- Additionally, it would offer an enterprise grade hosted version, with additional features.
- It would be distributed along with a Docker-powered semi-automated setup that would spin up the different parts of the system.
- Data would be accessed through an intermediate caching layer, which allows programs to be modified and run over and over on the same data without the need to fetch it repeatedly, eliminating the additional execution time that would be incurred. This would also enable fast data visualization.
- Seekers wouldn't be hosted on the application's code itself, but would be provided by the user, probably through a Git repository, containing a Docker setup and a Insight-specific configuration file. Insight would download the repository, build the images and spin up the containers, as well as provide volumes that allow for model persistence and output data storage (for larger or more complex data outputs).
- ML model training and versioning capabilities would be implemented, allowing users to easily provide parameters and data, validate the models' performance, and store the models themselves, along with their diagnostic data.
- Live runs: Seekers would be deployed live, to conduct real time analysis of incoming data. Insights could be visualized on the dashboard, but also provided as alerts, webhook calls, etc.
