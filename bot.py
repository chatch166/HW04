from typing import Text
import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment function from the madlibs assignment here
madlibs = [
    "[MATT_GAETZ] is a [GREAT] [CONGRESSMAN]. He has [LOTS] of [FANTASTIC] ideas. Everyone [SHOULD] [VOTE_FOR] him to stop the [DEMOCRATS].", 
    "President Chodosh’s publications include [Uniform Civil Code of India: A Blueprint for Scholarly Discourse] (with [Shimon Shetreet], 2016), [Law in Iraq: A Document Companion] (with co-editor [Chibli Mallat], 2013), both published by Oxford University Press, and [Global Justice Reform: A Comparative Methodology] (2005, NYU Press). He is currently working on taking in more ethically dubious donations for the College.",
    'Hiram E. Chodosh is the [president] of Claremont McKenna College, one of the top liberal arts colleges in the [country]. An accomplished leader in [several domains], he is widely recognized for his innovations in [higher education], [scholarship in comparative law], and expertise in international justice reform.',
    "Under President Chodosh’s [LEADERSHIP], CMC has implemented several new [PROGRAMS] and [CENTERS] to enhance the College’s singular leadership mission in [LIBERAL ARTS EDUCATION]. CMC has raised more than [$200 million] in new funding for scholarship under his [LEADERSHIP].",
    "President Chodosh founded and directed [Global Justice Project: Iraq] under a $[10.4 million] grant (2008–10) from the U.S. Department of State. He has served in advisory positions on [justice reform] for the World Bank [Justice Reform Group], the International Monetary Fund [LEGAL] Department, and many court systems, non-profit organizations, and national commissions."
    ]

replacements = {
    'MATT_GAETZ' : ['Matt Gaetz', 'Paul Gosar', 'Louie Gomhert'],
    'GREAT' : ['great', 'magnificent', 'wonderful'],
    'CONGRESSMAN' : ['representative', 'congressman'],
    'LOTS'  : ['lots', 'tons', 'very many'],
    'FANTASTIC' : ['excellent', 'fantastic', 'intelligent'],
    'SHOULD' : ['should', 'needs to', 'is required to'],
    'VOTE_FOR' : ['vote for', 'support', 'donate to'],
    'DEMOCRATS' : ['Democrats', 'baby eaters', 'communists', 'marxists'],
    'Uniform Civil Code of India: A Blueprint for Scholarly Discourse' : ['Goodnight Moon', 'The Very Hungry Caterpillar', 'Sylvester and the Magic Pebble'],
    'Shimon Shetreet' : ['Pete Davidson', 'Harold and Kumar', 'Kim Kardashian'],
    'Law in Iraq: A Document Companion' : ['Fifty Shades of Grey', 'Fifty Shades Darker'],
    'Chibli Mallat' : ['Bill Hader', 'Ivanka Trump', 'Brad Pitt'],
    'Global Justice Reform: A Comparative Methodology' : ['Ouchie! A Treatise on Stubbing Toes', 'Underwater Basket-Weaving: a Comprehensive Tutorial', 'NFTs are the Future'],
    'president' : ['supreme ruler', 'commander-in-chief', 'prime minister'],
    'country' : ['galaxy', 'known universe', 'solar system', 'milky way'],
    'several domains' : ['sumo wrestling', 'fish de-boning', 'tofu consumption', "telling dogs they're a good little doggo"],
    'higher education' : ['hitting the quan', 'going hard in the paint', 'playing die on green beach'],
    'scholarship in comparative law' : ['getting really, really high', 'ingesting horse tranquilizers', 'poking dead animals with sticks'],
    'LEADERSHIP' : ['supreme command', 'dictatorship', 'totalitarian rule'],
    'PROGRAMS' : ['sumo wrestling programs', 'birthing simulators', 'fart-smelling courses'],
    'CENTERS' : ['helicopter training programs', 'toxic drinking culture initiatives', 'marijuana consumption initiatives'],
    '$200 million' : ['$20', '73 bitcoin', '27 Doge Coin'],
    'LIBERAL ARTS EDUCATION' : ['amateur surgery', 'playing with sharp toys', 'experimenting in the bedroom'],
    'Global Justice Project: Iraq' : ['Enron', 'dozens of shell corporations', 'the Feline Rectal Health Initiative'],
    '10.4 million' : ['2', '70 quadrillion', '20'],
    'justice reform' : ['selling overpriced wines to ignorant idiots', 'scamming old people out of their pensions', 'pointing lasers for kittens to play with'],
    'Justice Reform Group' : ['Prosperity Reduction Commission', 'Irresponsible Corporation Bail-out Commission', 'Sumo Suit Wearing Commission'],
    'LEGAL' : ['Sushi', 'Marijuana', 'Fossil Fuels', 'Anti-Racist, Feminist, and Queer Studies']
    }

def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.
    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.
    For example, if we randomly seleected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''
    sentence = random.choice(madlibs)
    for key in replacements.keys():
        sentence = sentence.replace('['+key+']',random.choice(replacements[key])) 
    return sentence


# connect to reddit 
reddit = praw.Reddit('charbot')

# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://old.reddit.com/r/BotTown2/comments/r49orc/ryans_ex_speaks_exposes_him/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    try:
        print('submission.title = ',submission.title)
    except AttributeError:
        pass
    print('submission.url = ',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    # HINT: 
    try:
        submission.comments.replace_more(limit=None)
    except AttributeError:
        pass
    all_comments = []
    try:
        all_comments = submission.comments.list()
    except AttributeError:
        pass
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        if str(comment.author) != 'BOThersomebOT':
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented = ', has_not_commented)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        text = generate_comment()
        try:
            submission.reply(text)
        except AttributeError:
            pass

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        unrepliedcomments = []
        for comment in not_my_comments:
            commentauthors = []
            for reply in comment.replies:
                commentauthors.append(str(reply.author))
            #print('comment authors = ', commentauthors)
            if 'BOThersomebOT' not in commentauthors:
                unrepliedcomments.append(comment)
            else:
                pass
            #print('unreplied comment = ', unrepliedcomments)

                

        comments_without_replies = unrepliedcomments
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        try:
            comment = random.choice(comments_without_replies)
        except IndexError:
            print('No comments without replies to reply to')
            pass
        try:
            comment.reply(generate_comment())
        except praw.exceptions.APIException:
            print('did not reply to a deleted comment')

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    submission = random.choice(list(reddit.subreddit('BotTown2').hot(limit=50)))
    # print('random hot submission = ', submission.title)

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(5)
