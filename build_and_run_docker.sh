systemctl start docker.service
docker build -t knosc_backend .
source run_docker.sh
