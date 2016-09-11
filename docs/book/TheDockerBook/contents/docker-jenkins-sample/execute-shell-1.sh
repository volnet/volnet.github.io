IMAGE=$(docker build . | tail -1 | awk '{ print $NF }')

MNT="$WORKSPACE/.."

CONTAINER=$(docker run -d -v "$MNT:/opt/project" $IMAGE /bin/bash -c 'cd /opt/project/workspace && rake spec')

docker attach $CONTAINER

RC=$(docker wait $CONTAINER)

docker rm $CONTAINER

exit $RC