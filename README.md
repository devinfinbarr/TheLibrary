The Library
===========

Carefully curated reading lists covering the best 1,200 pages written every subject in existence.


What makes TheLibrary special?
-----------------------
There are plenty of reading lists in the world.  Amazon is littered with "Best of" lists, you can google around for different lists, or go to a site like "goodreads".  So why did we create the library?

First, we aim to provide not the just the best books, but the best 1,200 pages.  That means we our reading lists will have many online articles in addition to books.  Many books only have a few worthwhile chapters.  Our reading lists will pick out those chapters, so you do not waste time.  Many reading lists just accumulate every book on the subject, without making hard judgements.  People have limited time, by limiting reading lists to 1,200 we impose discpline on the curators of the reading list to really pick the best sources and dump the less worthwhile readings.


Second, I (Devin Finbarr, the founder of TheLibrary) felt that most reading lists were pretty lousy.  A book full of sentimental pap can get five starts on Amazon, while a flawed but invaluable primary source will be ignored.  I find the best sources for finding good books are particular individuals who are very thoughtful and very well read on particular subjects.  Such people are scattered around the web, but their recommendations are often hidden deep in their web site archives or in the comment thread of some web site.  TheLibrary is an attempt to create one central repository for these reading lists.

Third, we are using github to manage the list.  Github allows us to accept contributions from a wide variety of people, making the list more than just our personal opinion.  But github allows us to have more quality control than a wiki (which is especially important since we want the library to very concise, and not to grow unbounded).

Ultimately, the success of the project will depend on the personal judgement of the list curators.  If you think our judgement sucks, send a ***constructive*** note to the mailing list ( [https://groups.google.com/d/forum/the-library-discussion](https://groups.google.com/d/forum/the-library-discussion) )) and tell us why we're out of line.  Or you can fork the TheLibrary and make your own better version, the entire project is open source.

Submission Guidelines
---------------------
We welcome contributions and edits of the library.  But submissions must adhere to standards in order to ensure the quality of the library.

When submitting a pull request, You must provide convincing reasons for why the books you wish to include should be included.  If you are a first time contributor, you should provide links to your blog, reviews you have written on amazon, or comments you have written on some site, that demonstrate you are a thoughtful and well read person.  Every commiter, no matter how experienced, should provide at least a paragraph of explanation of why the reading is worthwhile.  Even better is to link to thorough reviews of the book.  

Reading lists must be in the following test format.  The format must be strict, so that our software scripts can parse the reading lists and build the HTML site automtically.

```
Title of the reading list
summary:
This is a pithy explanation of the topic of the reading list.  The explanation will both describe what the list is about and give the reader a few teaser questions that they should keep in mind while exploring the list.
end-summary

**************  # a line of stars separates each book
title: The Title of the Book
author: Last Name, First name
publish-date:YYYY or YYYY-mm-dd
selections:Chapter 1-20  # The parts of the book you recommend reading
page-count:120 
periodical:The name of the magazine or newspaper, if applicable
free-link:
paid-link:
faction:(conservative|progressive|mainstream|libertarian|reactionary)
summary:
You can make information multiline, by putting no text on the first line, and then doing "end-field-name" for the last line, with nothing else on the last line.
end-summary
curators-notes:
An explanation from the contributor and/or the repo maintainer about why this reading was added to the library.
end-curators-notes
***************
title: Democracy in America
author: Tocqueville, Alexis de
publish-date:1840
selections:Chapter 1-3, 7, 12
page-count:120
summary:
The classic exposition of the political and cultural life of the young American republic.  Tocqueville's book is heavier on analysis and generalizations than it is on detailed observation.  Worthwhile because of its fame influence, but not the best book for actually understanding the history of the time.
***************
title: Japan Surrenders, End of War!
author: Krock, Arthur
publish-date:1945-08-15
page-count:120
summary:
The classic exposition of the political and cultural life of the young American republic.  Tocqueville's book is heavier on analysis and generalizations than it is on detailed observation.  Worthwhile because of its fame influence, but not the best book for actually understanding the history of the time.
***************

``` 

A few additional notes about the above format:
* title, author, publish-date, summary, selections, curators-notes, and page-count are required
* Selections should never include page numbers, as those will vary based on edition.  Please use chapters.
* You must include the selections and page count for every reading
* For kindle books, 13 locations count as one page
* For documents without pages, such as web articles, count 300 words as one page.  You can count the number of words with a [free online word count tool](http://www.wordcounttool.com/), just paste in the body of the document.




How do I contribute?
-----------------------

If you have never used github before, you should read a tutorial: [git for non-programmers](http://www.sitepoint.com/version-control-git/) and [how to fork a repo](https://help.github.com/articles/fork-a-repo).


* Create a github account if you do not one
* Fork the repo to your own account
* If you do not want to install a git client on your computer, you can just browse to the file and edit it directly in the browser.  If you want to edit locally in your text editor of choice, you will need to follow a tutorial for installing a git client and cloning a repo.
* Submit a "pull request" to ask TheLibrary maintainers to accept your changes into TheLibrary



<a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/88x31.png" /></a><br />TheLibrary repository is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_US">Creative Commons Attribution 3.0 Unported License</a>.


Bias and Objectivity
---------------------

Any attempt to create reading lists for every subject in existence means that the attempt will need to create reading lists for political touchy subjects.  Thus the question arises - what is the political bias or slant of the curators of The Library? Do we have a policy of "objectivity".

When we discuss "bias" or "objectivity", we really debating four different questions.  I will answer each one.

Is The Library opinionated?  An opinionated publication openly exercises its own opinion and judgement about the matters it covers.  An un-opininated publication simply chooses some standard for truth and replicates that without inserting personal judgement.  Wikipedia is an example of a publication with a policy against unopuninated - authors are not supposed to write articles with their own personal judgement, but rather replicate findings from "reputed sources" such as academia and the NY Times.  When academics do not agree, Wikipedia will report on the controversy.  

The Library is explicitly an opinonated publication.  Myself and other curators actively exercise our own judgement in putting together the reading lists.  In my opinion, attempting to eliminate opinion or judgement does not equate with being unbiased -  it simply equates to replicating the bias of the source that you are relying on, whether that source be academia or public conventional wisdom.  My goal with The Library is to help the reader find the truth.  If I have a strong opinion about which books provide the truth, obviously I will have to adjust the reading list accordingly.  If my view of the the truth is at odds with conventional wisdom, then I will also add the best representation of the conventional wisdom to the reading list.  If the reader is to really understand the truth, the reader must understand all sides of the debate, even the side I might think is wrong.

Is The Library partisian?  The most pernicious form of bias is when an author allows his allegience to a party, friend, or self-interest to outweigh his desire to find the truth.  This is not always evil.  If you really think saving the world depends on your side winning, and you think lying or spinning the truth will help your side win, then lying is not unreasonable.  But this is a very dangerous game to play.  And right now, I do not have any partisian affliation so strong that it would make me lie.  So the Library is explicitly not-partisian - truth is our goal, not winning.  Of course, I would say this, wouldn't I?  Remaining non-partisian is a struggle.  Personally, I have staked out strong opinions in the past.  My own instinct is to replciate evidence that shows my views were right, and spin away evidence that contradicts me.  I must fight this instinct.  If you see me fall prey to it, please let me know.

Do The Library curators have prior beliefs or biases that predispose it to certain views?  Do The Library curators adhere to an ideology?  The answer to this is yes.  Everyone has their own life experiences that inform their view of the world.  For instance, the reading list about dating and relationships has a number of readings that are more cynical about the behvavior of women.  I did not select these readings because I hate women, I love my finance very much.  But in my experiences, these articles captured important lesson that myself and many friends experienced the hard way.  Since I think these articles contain the truth, I include them in the reading list.  My life experiences therefore predispose me to believe in these articles and it is not entirely unfair to say that this reading list is a result of my biases.  These articles could be called by some, "reactionary", and I will not deny the label.  But if The Library takes on a reactionary bent, it is not because I set out to make it that way.  I set out to create the truth, if the truth is reactionary, then so be it.  If the truth is progressive or conservative or any other ideology, then so be it.  If you think that my life experiences are clouding my vision or causing me to miss some important aspect, please let me know.  But in order to convince me, you will have to provide actual evidence of some sort.  If you find one of my articles on dating to be horribly wrong, provide some creditable accounts of people who tried the strategies and had it fail terribly or accounts of people who tried opposite strategies and had those strategies work.  The only way I can overcome the limitations of my own experience is by gaining as much data, evidence, and creditable information as possible.





