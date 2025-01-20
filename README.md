
![lost-title-logo-slice](https://github.com/user-attachments/assets/5c1381df-7f1f-40e6-ac3a-e6f65fbd710b)

# LOST-characters

`LOST-characters` is an EDA project on the scripts of the episodes of the show *Lost*. 



# Background and Motivation

*Lost* was a television show running from 2004-2010 that, aside from resulting in a near-cult following, has been lauded by many as one of the [greatest](https://web.archive.org/web/20121022172014/http://entertainment.time.com/2007/09/06/the-100-best-tv-shows-of-all-time/slide/lost-2/) [shows](https://ew.com/article/2007/06/18/new-classics-tv/) to have aired. As a result, many people have come to feel strongly about the show and its characters, partly evidenced by its IMDb scores. 

The original motivation for the project came from a simple question: are episodes that give Hurley (aka Hugo) more screentime generally rated higher? Naturally, one can begin to ask the same question about other characters, and eventually become tempted to investigate further as I did. To actually measure "screentime" seemed arduous, so instead I opted to use word count via scripts of all the episodes of the show. 



# Data Sourcing

At first, the hardest part of bringing this project idea to fruition was finding a source that could provide transcripts of all the episodes in the show. Luckily, I found out that the good folks at [Lostpedia](https://lostpedia.fandom.com/wiki/Main_Page) did just that! Now that I had [my data source](https://lostpedia.fandom.com/wiki/Portal:Transcripts), it was time to scrape the data using Beautiful Soup. Though I've [had experience](https://github.com/parsaha/imdb) with web scraping before, I made use of [this Dataquest tutorial](https://www.dataquest.io/blog/web-scraping-beautifulsoup/) to brush up on it (as seen in the `Lost Transcripts EDA (Pilot)` file of this repository). Ratings for each of the episodes were taken from [IMDb](https://www.imdb.com/title/tt0411008/ratings/).


# Findings

## Top Ten Talkers

After learning how to aggregate each character's word count, I was able to find which ten characters talk the most in the show.

![top-ten-talkers](https://github.com/user-attachments/assets/5a01d5de-60c4-43e7-857c-e3125e5c336e)

To most who have watched the show, it may be very surprising to see a character like Michael have a higher word count than other characters like Jin or Sun. My best guess for this unexpected result comes down to data availability: many of the Lostpedia transcripts that we are sourcing our data from have no accompanying subtitles, making it difficult to determine what really counts as a "word count" for Korean text. My solution to this issue was to simply ignore any such pieces of dialogue, assuming that the proportion of Korean dialogue without subtitles would be negligible among all transcripts. Whether this assumption was remiss or not, it has resulted in Michael coming up higher in word count than Jin and Sun. (The details of the way missing data was treated is explained in the `Lost Transcripts EDA (Pilot)` notebook.)

## Top Five Talkers Over Time

As is evident, many of the top talkers (cumulatively) are not the ones consistently racking up their word count. So, we can take a look at some of the top speakers in the show and how their word count progressed as the show went on.

![top_five_talkers_over_time](https://github.com/user-attachments/assets/8eafabcd-e212-4d97-b595-9a424060d003)

To make things a little easier to see and interpret, I also took a look at the top three talkers in isolation to compare the progression of their word count over time. 

![top_three_talkers_over_time](https://github.com/user-attachments/assets/5f25f521-9b68-44f3-9d7b-2d669fb9adcf)

It's interesting to see Jack's word count consistently spike up over the course of the show, while John and Sawyer have occasional bursts of talking that shoot above the rest. Notice that none of the data points in the graph necessarily correlate to the character that spoke the most in that episode; these are simply the trends for those characters that cumulativelt spoke the most.  

## Hurley's Effect on the Ratings

Now we take a look at the statistic that inspired this project: whether there is a direct correlation between how much Hurley talks in an episode and how well-received it is. 

![hurley_vs_scores](https://github.com/user-attachments/assets/3fe796b7-cd79-4795-84ff-67942ddeba8a)

Unfortunately, my prediction did not come to fruition: Hurley's word count seems to not corrrelate very much with the score of a given episode. I guess [people don't love Hurley]([https://lostpedia.fandom.com/wiki/Everybody_Loves_Hugo_transcript](https://lostpedia.fandom.com/wiki/Everybody_Hates_Hugo_transcript)) as much as I do. 

## Word Clouds

Finally, what text-based EDA is complete without some word clouds? For this section, I chose to focus not on those characters that talked the most, but rather on those characters I felt would have easily attributable word clouds. For example, my hope was that Desmond would say a lot of "brother", "Ben" a lot of "John", and Hurley a lot of "dude."

![desmond_word_cloud](https://github.com/user-attachments/assets/eb6f1c08-d020-4801-b390-fbfff9579718)

Thankfully, I was right! Desmond punctuates a lot of his sentences with "brother" (and I should have anticipated much of his dialogue being about Penny).

![ben_word_cloud](https://github.com/user-attachments/assets/179b6c81-3a93-4ce2-bb4b-1b61a96470bf)

Ben is in fact obsessed with John and the island, but outside of that I wasn't sure what to expect. I definitely thought "Jack" would come up less often than it did, and that "Jacob" would come up much more often. For some reason, the word "one" comes up quite often.

![hurley_word_cloud](https://github.com/user-attachments/assets/4d86a434-1bb2-4109-b1a0-da7a367b78f7)

As promised, "dude" and "man" are center-stage! And though it's not particularly insightful, I do like that the words "uh" and "oh" (and "uh oh" by extension) are so common in Hurley's vocabulary. 

# Sawyerisms

At some point I wondered if I could find all the nicknames Sawyer gives people in this project (for example, extract all the unique instances of proper nouns Sawyer uses that aren't actual names used in the transcripts). However, before I could engage in that headache of edge cases and manual quality checking, I realized that Lostpedia had [made life easy](https://lostpedia.fandom.com/wiki/Sawyer%27s_nicknames) for me once again. While it would have been fun to find these myself and compare which characters are subject to the most nicknames, I figured I would leave this here for any interested parties since it does a much better job than any semi-automated solution could have.

