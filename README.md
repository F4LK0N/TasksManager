# DOCKER
This project utilizes docker-compose to create the environment required to run locally in your machine.
It comes with all its essential functionalities already installed and configured to start development.  
The objective of the containers are to create the environment, with script servers, database servers, etc. Initialize containers with required data and instaltions, and let the environment ready to develop without any more actions from the developer. Just build and use.

.
# FILE SYSTEM
Important files and folders are centralized in root folders to facilitate access.  
- ``` /data/ ``` Data that must persist across container rebuilds;
- ``` /logs/ ``` Log files and folders used by the system and applications;
- ``` /docker/ ``` Scripts used by docker to setup and run the container;

> :information_source: Some logs can't be configured to save directly to the logs folder, in this cases an symbolic link (shortcut) has been created inside the logs folder to facilitate access.  
> :warning: (Windows) When mapping the logs folder from the container as a volume to the local filesystem, the symbolic links don't appear in the local system, to see this links you must enter the container.  

.
# NETWORK
The environment create isolated networks with its own subnet and gateway. Every container is placed inside this networks and has an IP4 address defined.
To access the containers you can use the IP defined for each one, but for facility and elegancy you can define customized URL addresses. For this, edit your hosts file adding the follow lines:
```shell
173.21.0.10 panel.mri
173.20.0.20 api.mri
173.20.0.30 sql.mri
```
Hosts file on Linux:
``` /etc/hosts ```
Hosts file on Windows
``` C:\Windows\System32\drivers\etc\hosts ```

.
# USAGE
### Build
	docker compose build  
	docker compose build --progress=plain  
### Run
	docker compose up -d
### Build and Run
	docker compose up -d --build
### Access
	docker compose exec -it api /bin/bash
