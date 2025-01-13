# LOST-characters

`LOST-characters` is an EDA project on the scripts of the episodes of the show *Lost*. 



# Background

*Lost* was a television show running from 2004-2010 that, aside from resulting in a near-cult following, has been lauded by many as one of the [greatest](https://web.archive.org/web/20121022172014/http://entertainment.time.com/2007/09/06/the-100-best-tv-shows-of-all-time/slide/lost-2/) [shows](https://ew.com/article/2007/06/18/new-classics-tv/) to have aired. As a result, many people have come to feel strongly about the show and its characters, partly evidenced by its IMDb scores. 



# Motivation

The original motivation for the project came from a simple question: are episodes that give Hurley (aka Hugo) more screentime generally rated higher? Naturally, one can begin to ask the same question about other characters, and eventually become tempted to investigate further as I did. To actually measure "screentime" seemed arduous, so instead I opted to use word count via scripts of all the episodes of the show. 



# Data Sourcing

## Finding Transcripts

At first, the hardest part of bringing this project idea to fruition was finding a source that could provide transcripts of all the episodes in the show. Luckily, I found out that the good folks at [Lostpedia](https://lostpedia.fandom.com/wiki/Main_Page) did just that! Now that I had [my data source](https://lostpedia.fandom.com/wiki/Portal:Transcripts), it was time to scrape the data using Beautiful Soup. Though I've [had experience](https://github.com/parsaha/imdb) with web scraping before, I made use of [this Dataquest tutorial](https://www.dataquest.io/blog/web-scraping-beautifulsoup/) to brush up on it (as seen in the `Lost Transcripts EDA (Pilot)` file of this repository). Ratings for each of the episodes were taken from [IMDb](https://www.imdb.com/title/tt0411008/ratings/).





# Findings
