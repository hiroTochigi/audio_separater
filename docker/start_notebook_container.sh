

# Run this script in top directory of this project
docker run --name extract_audio -itd -v `pwd`:/home/jovyan/work hirotochigi/moviepy
docker run --name separate_audio -it -p 8888:8888 -v `pwd`:/home/jovyan/work resemblizer
