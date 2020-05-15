# The Frontend

The frontend of our web app is built with Vue.js Single File Components. To develop it, we use the Vue-CLI, which comes with the power of Webpack already included to offer instant reloading, so we don't need to worry about setting that up separately.

For the sake of reproducible research and consistent collaboration, you should run this through the Docker container `peterprescott/frontend:0.1`, which you can pull from the Docker Hub (although the Dockerfile is also here if you're interested). And then just run the `docker-run.sh` from this folder (unless you are on Windows...), and you should be able to see the webpage being served up at `localhost:8080`.
