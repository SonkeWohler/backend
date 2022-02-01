# in case docker service isn't up yet
# can skip/abort authentication if it is already running
systemctl start docker.service
source sh/build_docker.sh
docker run -it --rm -p 127.0.0.1:5000:5000 knosc_backend
