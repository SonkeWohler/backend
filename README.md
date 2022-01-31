# Trying out Docker Rest API

This is a proof of concept regarding running a Rest API with Python/Flask
inside Docker.

## Tutorials Used

* [Quick start for Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
* [Putting Docker inside git repositories](https://www.baeldung.com/ops/dockerfile-git-strategies)
* [Flask inside Docker](https://pyshark.com/containerize-a-flask-application-using-docker/)
* [For testing API in browser](https://www.whitesourcesoftware.com/free-developer-tools/blog/docker-expose-port/)

## Running

You should just be able to build and run the cocker container without further
issues.

On Linux you can just run the following:

```
source build_and_run_docker.sh
```

In case the docker service isn't running yet that will start it, but if it is
running already that doesn't make a difference.

### Requirements

Aside from [docker](https://www.docker.com/) being installed and setup there
shouldn't be anything needed.
