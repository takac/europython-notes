Docker Development
==================
Deni Bertovic  
[@denibertovic](https://twitter.com/denibertovic)
[https://githbub.com/denibertovic](https://githbub.com/denibertovic)
[https://ep2014.europython.eu/en/schedule/sessions/30/](https://ep2014.europython.eu/en/schedule/sessions/30/)
[https://www.youtube.com/watch?v=-l9xH1X_rvg](https://www.youtube.com/watch?v=-l9xH1X_rvg)

### Docker
Light weight containers
Built on LXC
One processor per container

Docker Image - Immutable
Hub (registry) - Public or private image repository

pull an image from the hub
run the image

### Docker Images
    docker run

List images running

    docker ps

Tag an image, can then push it

    docker t 

Docker files to build the image.

### Why Docker

Allows matching production services. Consistency between development environments.
Docker link allows you to expose ports to other containers.

Ephemeral disk images.
Volumes have to be used for persistent data.

Docker exposes http api, easy to interact.
pyDocker
Docker python interface

### Fig
Vargrant for docker
YAML to describe the image
then `fig up`
