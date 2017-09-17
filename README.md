# ASMP
**ASMP connects to your smart energy meter, provides insight and allows you to control your energy consumption. The collected data is stored locally to guarantee your privacy. ASMP is  open source and runs on almost any platform.**

ASMP was started as a personal research project to learn new programming languages, frameworks and tools. However, it was also a chance to create a beautiful piece of software that allows users to get insight in their energy consumption without giving up their privacy. Hopefully you will enjoy using it as much as I did programming it. 

## Interface

![Desktop Interface screenshot 1](/doc/screenshots/interface/interface_sh1.png)
*Display of current usage and that of the last 5 minutes*

![Interface screenshot 2](/doc/screenshots/interface/interface_sh2.png)
*Shows an overview of the total usage. By clicking on the bars you can zoom in up to hour level*

![Interface screenshot 3](/doc/screenshots/interface/interface_sh3.png)
*Shows statistics for certain periods*

*The complete interface is fully responsive and will scale depending on the size of the display of your device*

## Getting started
ASMP will use docker, to simplify the installation. This section describes the necessary steps to get started.

### Docker quickstart
When you have docker already running, you can execute the following commands:

1. Create a data directory for asmp
```
mkdir /usr/bin/asmp/data
```

2. Run the docker container
```
Linux ARM
docker run -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/asmp:/usr/bin/asmp/data  blackhawkdesign/asmp-updater-linarm:latest
```
```
Linux 64BIT
docker run -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/asmp:/usr/bin/asmp/data  blackhawkdesign/asmp-updater-linarm:latest
```

### Full installation 
New to docker? These installation guides help you through the complete installation process.
1. Full installation for raspberry pie using linux
2. Full installation for ubuntu 64 bits
3. FUll installation for windows 64 bits (will follow soon)

## Roadmap
1. Create an update mechanism
2. Showing only recent measurements in recent chart / current chart. So only last 5 mins. Otherwise gray out
3. Create docs for getting started on a pie
4. Create docs for getting started on linux docker
5. Creating a heartbeat local and remote
6. Implement return charts
7. Implement gas database changes
8. Implement gas ui changes

## FAQ
Will follow soon ...
