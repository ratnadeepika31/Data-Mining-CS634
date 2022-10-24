# Data-Mining-CS634
git clone https://github.com/opencv/cvat
cd cvat
docker-compose up -d
CVAT_VERSION=dev docker-compose up -d
winpty docker exec -it cvat_server bash -ic 'python3 ~/manage.py createsuperuser'
