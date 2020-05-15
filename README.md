# Internship Project

A Data Science Project for Mossley Hill Church, as part of my MSc/PhD at the University of Liverpool's Geographic Data Science Lab.

## The Task
> The student will work on a research project defined between the student and an external organisation.
>
> The aims of the placement will be defined in terms of progressive risks in effecting a solution:
> - The first aim should have a low risk of failure;
> - the second aim will be more challenging but capable of solution given initiative and energy on the part of the student;
> - and the third aim can have a 'blue skies' element, a real research challenge and consequently a high risk of failure but success will demonstrate exceptional competence and initiative.

## The Partner
Mossley Hill Anglican Church. A family church in South Liverpool.

## Research Project
To transform the church members' postcode data into useful insight.

## The Aims

1. Neighbourhood Geodemographics
2. Catchment Area Analysis
3. Developing a Data Dashboard

## Outputs

You can see [my presentation](./pdf/presentation.pdf) or read [my report](./pdf/report.pdf).

You can interact with [my notebooks](./notebooks/).

You can visit the [churchmAPP website](https://churchmapp.netlify.com).

Or you can clone this repo and contribute to the development of churchmAPP.

## Collaboration

If you are interested in collaborating, or just exploring this analysis yourself, then this may be made easier by the use of Docker containers.

For the notebooks, start from this root of the repository:
```
docker run -it -p 8888:8888 -v $PWD:/home/jovyan/work peterprescott/geodatascience:0.1
```

For the frontend of the website, `cd frontend` into that folder, and then:
```
docker run -it -p 8080:8080 -v $PWD:/src peterprescott/frontend:0.1
```

And for the backend, `cd backend` into that folder, and then:
```
docker run -it -p 5000:5000 -v $PWD:/app peterprescott/backend:0.1
```

Or just run the `docker-for-WHATEVER.sh` script in the relevant directory. This will pull the necessary images for you from the online Docker Hub. The `geodatascience` image in particular is large, and may take some time to download -- but it should include everything you might need!

Note that if you are not familiar with Docker and you are familiar with Jupyter notebooks, or the Vue-CLI, or Flask, then this may be (in the short-term) more hassle than it is worth.

## Licenses

Insofar as this is my work, it is available under the MIT License. I have tried to track my references in the `.bib` file in the `bits` folder.

The geographic data includes Ordnance Survey and ONS data (Open Government License), and I think also Royal Mail data.

The churches' data I do not share, although I make visible the results of my analysis. If you want to do a precisely equivalent analysis, just put a column of postcodes under the heading `Postcode` in a .csv file in `/data/sensitive/postcodes/`.
