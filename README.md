# HW04

**Hello world!**

For this assignment, I was tasked with creating a Reddit bot to parse through subreddits and post, comment, and up/downvote submissions and comments when appropriate. The text of my submissions varied––the program randomly selected one of five sentence-writing functions to use, and I had several possibilities. One sarcastically praised either Matt Gaetz, Louie Gomhert, or Paul Gosar, and the other ones spread comedic disinformation about Claremont McKenna's president, Hiram Chodosh. 

**My Favorite Thread**

Since our class' bots weren't high-tech enough to decipher meaning, they piled on each other in some pretty nonsensical threads. My favorite [thread](https://old.reddit.com/r/BotTown2/comments/r432dc/here_is_the_deal_and_question_netflix_germany/hme5yvj/) involved an exchange between my bot and several variations of `Bernie_Bot`. They were concerned with Bernie's accomplishments and record, and I jutted in with a completely unhelpful, ridiculous comment about the president of a liberal arts college. It represented the peak of these bots' non-understanding of any actual meaning. 

<img width="869" alt="Screen Shot 2021-11-28 at 8.54.23 PM.png" src="Screen Shot 2021-11-28 at 9.57.17 PM.png"> 

**Bot Counter Output**

Here is the output of my `bot_counter.py` file. Sadly enough, I seemed to asymptotically approach the 1000 mark, yet never arrive. Here is the output of my most recent running of `bot_counter.py`:
```
len(comments)= 1000
len(top_level_comments)= 58
len(replies)= 942
len(valid_top_level_comments)= 58
len(not_self_replies)= 941
len(valid_replies)= 939
========================================
valid_comments= 997
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit
Charless-MacBook-Pro-2:reddit_stuff charliehatcher$
```

**What My Score Should be**

I believe I should get a 34/30 on this project:

Implementation of the six `bot.py` tasks: 6 * 3 = 18

GitHub repo with all the requisite items: 2

Optional Task 1 (post 100 valid comments): 2

Optional Task 2 (post 500 valid comments): 2

Optional Task 3 (see note below) (post 1000 valid comments): 2

Optional Task 4 (see `extracredit4.py`) (crosspost other reddit submissions into BotTown2): 2

Optional Task 5 (see `armybot` numbers 1-5) (create an army of five bots): 2 

Optional Task 6 (have your bot's comment be a reply to the highest upvoted comment in a thread): 0

Optional Task 7A (see `extracredit7.py`) (scan other post titles and comments and upvote or downvote according if they mention a favored or disfavored candidate): 2

Optional Task 7B (see `extracredit7.py`) (use TextBlob to determine the sentiment of comments about a favored candidate and upvote or downvote accordingly): 2

Total = 34

Note on Task 3: I generated over 860 comments on the original BotTown, and while I kept posting on BotTown2 to the point where I almost got 1000, I didn't have enough time with the holidays to keep running it to the point where the bad comments got "flushed out." Since I did generate well over 1000 comments over the course of the project (see the photo below showing the last output of `bot_counter.py` before BotTown got banned), I believe I should get credit for task three. 

<img width="500" alt="Screen Shot 2021-11-28 at 8.54.23 PM.png" src="Screen Shot 2021-11-26 at 5.16.21 PM.png"> 
