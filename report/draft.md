---
title: 'Three Ways of Extracting Insight from Postcode Data: Data Science for the Local Church'
author: 
    name: 'Peter Prescott'
    affiliation: 'University of Liverpool'
biblio-style: pi-harvard
bibliography: churchmAPP.bib
abstract: 'This is a report on the work done during a two week internship done as part of the Data Analytics & Society MSc/PhD...'
---



# Introduction
This is a report on a research project done as part of the Data Analytics and Society MSc/Phd that I am doing at the University of Liverpool's Geographic Data Science Lab. 

The project was to extract insight from the postcode data contained in the electoral roll (ie. the register of voting members) of Mossley Hill Church, an Anglican parish church in South Liverpool. The significance of being listed on the electoral roll can vary considerably from church to church, but the church's website declares that "Electoral rolls provide an indication of the real membership and strength of the church... For us it is an act of commitment..."

Church membership and attendance statistics are much discussed in the context of claims and counterclaims about British secularization, 


The Church of England first began publishing statistics in 1960, with a 96-page collection of 'Facts and Figures about the Church of England' that one could purchase for twenty-one shillings. 

has published Church Attendance, Parish Finance, and Licensed Ministry statistics every year since 2011, and before that had published a single annual Church Statistics report almost every year since 1976 [@ChurchofEngland2020].

![](figs/age-group-distribution.png)

# Postcodes

@JRaperEtAl1992 [p.7]


# Neighbourhood Geodemographics


Geodemographics is often introduced by quoting the pithy definition of @PSleight1997 [p.7] -- it is called "the analysis of people by where they live". The reverse is at least as true: geodemographics is the analysis of places by the people who live there. Specifically, a geodemographic classification is made by algorithmically clustering geoographic areas into similar groups on the basis of the demographic and socioeconomic statistics of their inhabitants, and then naming and describing each resulting group in terms of its shared characteristics. This can be done at whatever scale for which there is data -- generally, it is most useful at the finest possible scale of spatial resolution. The increasing availability of open-source statistics and of analytical computational power means it is now possible to create a geodemographic classification comparitively easily, and to tailor it to the needs of whatever particular case it is intended for; indeed, some have created systems to allow for the automatic real-time creation of geodemographic classifications on the fly [@MAdnan2011].

My aim here was simply to demonstrate the possibilities of geodemographic analysis for the purpose of helping a local church consider the value of their congregation's postcode data. For a simple proof-of-concept it was adequate to make use of an existing classification. Possibilities included commercial classifications such as Mosaic [@Experian2020] and Acorn [@CACI2020]; I chose the 2011 Open Area Classification [@CGaleEtAl2016a]. As its name suggests, it is a free and open-source classification based on data from the 2011 UK census, which classifies each census 'output area' into one of eight 'supergroups': 'Constrained City-Dwellers', 'Cosmopolitans', 'Ethnicity Central', 'Hard-Pressed Living', 'Multicultural Metropolitans', 'Rural Residents', 'Suburbanites' or 'Urbanites'. Each of these titles has a descriptive 'pen portrait' explaining in a few sentences its characteristics, and is subdivided into groups and subgroups with further relevant explanation.

This, for example, is the pen-portrait for 'Semi-detached suburbia': "People in this group are slightly more likely to be divorced or separated than those in the supergroup. Households are more likely to live in semi-detached and terraced properties, with a higher proportion of households renting their accommodation." 

Census output areas do not correlate exactly with postcode units, but a best-fit conversion can be achieved by considering which census output area the the post-code centroid falls into. This conversion table is published under the Open Government License[@ONS2020], and means we can identify the neighbourhood type of each person in the congregation, or even visualize the whole of, say, the Liverpool City Region, with a choropleth map showing the supergroup classification of each output area. (To do this, we need the Output Area boundary *shapefiles*, which are freely available online [@ONS2016].)

When we classify the data for Mossley Hill, we see that more than half of their congregation live in neighbourhoods that are classified within the 'Suburbanites' supergroup; of which almost all are in the 'Semi-detached suburbia' group; specifically, the 'Multi-ethnic suburbia' and 'Semi-detached ageing' subgroups. In contrast, the data from the other churches shows that their congregations are more diverse in terms of the neighbourhoods their members live in, with the top two supergroups being much closer in each case.

There is then the question of how to respond to this analysis. In retail strategy, geodemographic classification is often used with the assumption that those in similar neighbourhoods to existing customers are likely to themselves become customers. But a church is not a retail business with customers, and there is heated debate around the issue of homogenous-unit churches: are they necessary for church growth [@DMcGavran1990], or deficiently unethical [@LPope1957] -- or can they perhaps be defended on Christian ethical grounds after all [@CWagner1978].


![](figs/geodemographic-map.png)


![](figs/geodemographic-breakdown.png)


# Catchment Area Analysis


A catchment area is "the area extent from which the main patrons of a [service] will typically be found" [@LDolegaEtAl2016]. The concept is widely used in retail, in education [@JPearce2000], and in health [@GFulopEtAl2011]. Although similarly geographical, the idea is quite different to the territorial notion of political constituencies or traditional ecclesiastical parishes where a geographical community is served exclusively by the parliamentary or priestly representative whose zone they inhabit. Rather, to think in terms of 'catchment areas' is to think in terms of an overlapping set of multiple services that both combine and compete in complex and dynamic relationship with the choices of the target community.

Within the Anglican Church, the 'Fresh Expressions' initiative [@GCray2014] has attempted to loosen the strict geographical restrictions on what new services may be pioneered in what places, allowing potential new congregations to be gathered from a widespread area. This has in turn been the target of stringent critique from others within the Church [@ADavisonMilbank2010]. Outside the Church of England, the trend goes in the opposite direction, with increasing numbers calling for intentional 'incarnational mission' [@JKilpin2014] to particular deprived and/or unchurched neighbourhoods.

For my analysis, I used the Python package OSMNx [@GBoeing2017], which makes it simple to obtain a network graph of the surrounding streets within a given distance of any coordinate point. To do this it draws data from Open Street Map [@MHaklayWeber2008], a user-generated map that now covers more than 80% of the global road network [@CBarrington-LeighMillard-Ball2017]. First, I used a postcode-coordinate conversion table created by @FreeMapTools2020 from Ordnance Survey, Royal Mail and ONS data, and then I used OSMNx to calculate the shortest distance by road from each postcode to its respective church, and then to visualize those routes on a map.

The results showed that

A catchment area is "the area extent from which the main patrons of a [service] will typically be found" [@LDolegaEtAl2016]. The concept is widely used in retail, in education [@JPearce2000], and in health [@GFulopEtAl2011]. Although similarly geographical, the idea is quite different to the territorial notion of political constituencies or traditional ecclesiastical parishes where a geographical community is served exclusively by the parliamentary or priestly representative whose zone they inhabit. Rather, to think in terms of 'catchment areas' is to think in terms of an overlapping set of multiple services that both combine and compete in complex and dynamic relationship with the choices of the target community.

Within the Anglican Church, the 'Fresh Expressions' initiative [@GCray2014] has attempted to loosen the strict geographical restrictions on what new services may be pioneered in what places, allowing potential new congregations to be gathered from a widespread area. This has in turn been the target of stringent critique from others within the Church [@ADavisonMilbank2010]. Outside the Church of England, the trend goes in the opposite direction, with increasing numbers calling for intentional 'incarnational mission' [@JKilpin2014] to particular deprived and/or unchurched neighbourhoods.

For my analysis, I used the Python package OSMNx [@GBoeing2017], which makes it simple to obtain a network graph of the surrounding streets within a given distance of any coordinate point. To do this it draws data from Open Street Map [@MHaklayWeber2008], a user-generated map that now covers more than 80% of the global road network [@CBarrington-LeighMillard-Ball2017]. First, I used a postcode-coordinate conversion table created by @FreeMapTools2020 from Ordnance Survey, Royal Mail and ONS data, and then I used OSMNx to calculate the shortest distance by road from each postcode to its respective church, and then to visualize those routes on a map.

The results showed a clear difference between the close proximity of Mossley Hill's congregation to their church's building, and the greater geographical spread of the congregations of St Helens Christian Life Centre, Gateway Church, and the Stoneycroft Salvation Army. All of these three others are 'nonconformist' churches, which do not have the historic emphasis on the geographical parish which the Anglican church does.



![](figs/catchment-distance.png)


![](figs/mossley-hill-travel.png)


# An Interactive Data Dashboard


## The Web



## Web Frameworks



## Data Security



## DevOps Best Practices



## Presenting: ChurchM.app



# Conclusion



