# Dagster and dbt

## Overview

Learn how to integrate and orchestrate dbt projects with Dagster. You'll load dbt models into Dagster as assets, build dependencies, and ready your project for production deployment.

## Setup and run code
### from root folder
```shell

cd dagster_university/dagster_and_dbt
```

### Activate virtuell environment in the shell
```shell
source .venv/bin/activate
```

### Activate virtuel environment in vscode 
VS Code öffnen
Öffne das Projekt

Command Palette öffnen
Ctrl + Shift + P (Windows/Linux) oder Cmd + Shift + P (macOS).

Interpreter auswählen
Tippe "Python: Select Interpreter" und wähle den Eintrag aus.

Wähle "Enter Interpreter Path"
und gib den Pfad zum Python interpreter ein: 
Beispiel: 
```bash
/home/mini/src/ldm/project-dagster-university/dagster_university/dagster_and_dbt/.venv/bin/python3
```

### Start dagster UI 
```shell
dagster dev

## output
(dagster-and-dbt)  mini@u-1040-02  ~/src/ldm/project-dagster-university/dagster_university/dagster_and_dbt   main  dagster dev                          
2025-08-08 16:14:47 +0200 - dagster - INFO - Loaded environment variables from .env file: DUCKDB_DATABASE,DAGSTER_ENVIRONMENT
2025-08-08 16:14:47 +0200 - dagster - INFO - Using temporary directory /home/mini/src/ldm/project-dagster-university/dagster_university/dagster_and_dbt/.tmp_dagster_home_4v5odi9l for storage. This will be removed when dagster dev exits.
2025-08-08 16:14:47 +0200 - dagster - INFO - To persist information across sessions, set the environment variable DAGSTER_HOME to a directory to use.
2025-08-08 16:14:48 +0200 - dagster - INFO - Launching Dagster services...
2025-08-08 16:14:56 +0200 - dagster.daemon - INFO - Instance is configured with the following daemons: ['AssetDaemon', 'BackfillDaemon', 'QueuedRunCoordinatorDaemon', 'SchedulerDaemon', 'SensorDaemon']
2025-08-08 16:14:56 +0200 - dagster-webserver - INFO - Loaded environment variables from .env file: DUCKDB_DATABASE,DAGSTER_ENVIRONMENT
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1754662496.448992 3632530 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-08-08 16:14:56 +0200 - dagster-webserver - WARNING - Port 3000 is in use - using port 35451 instead
2025-08-08 16:14:56 +0200 - dagster-webserver - INFO - Serving dagster-webserver on http://127.0.0.1:35451 in process 3632530  
```

Go to the dagster UI http://127.0.0.1:35451/ (Port changes since Port 3000 is already in use for Marquez)
Materialized the rquired asset. 


## Completed code

If you are stuck you can reference the completed code for each lesson.

```
src
└── dagster_and_dbt
    └── completed
        ├── lesson_2
        ├── lesson_3
        ├── lesson_4
        ├── lesson_5
        ├── lesson_6
        └── lesson_7
```
