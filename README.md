The Library
==========

Carefully curated reading lists covering the best 1,200 pages written every subject in existence.


What makes TheLibrary special?
-----------------------
There are plenty of reading lists in the world.  Amazon is littered with "Best of" lists, you can google around for different lists, or go to a site like "goodreads".  So why did we create the library?

First, we aim to provide not the just the best books, but the best 1,200 pages.  That means we our reading lists will have many online articles in addition to books.  Many books only have a few worthwhile chapters.  Our reading lists will pick out those chapters, so you do not waste time.  Many reading lists just accumulate every book on the subject, without making hard judgements.  People have limited time, by limiting reading lists to 1,200 we impose discpline on the curators of the reading list to really pick the best sources and dump the less worthwhile readings.


Second, I (Devin Finbarr, the founder of TheLibrary) felt that most reading lists were pretty lousy.  A book full of sentimental pap can get five starts on Amazon, while a flawed but invaluable primary source will be ignored.  I find the best sources for finding good books are particular individuals who are very thoughtful and very well read on particular subjects.  Such people are scattered around the web, but their recommendations are often hidden deep in their web site archives or in the comment thread of some web site.  TheLibrary is an attempt to create one central repository for these reading lists.

Ultimately, the success of the project will depend on the personal judgement of the list curators.  If you think our judgement sucks, send us a ***constructive*** note and tell us why.  Or you can fork the TheLibrary and make your own better version, the entire project is open source.

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