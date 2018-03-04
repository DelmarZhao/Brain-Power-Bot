"""
A bot for enhancing brain power
"""
import praw
import sys

BOT_TRIGGERS = ("brainpower", "brain power", "BrainPower", "Brainpower",
                "Brain Power", "Brain power", "BRAINPOWER", "BRAIN POWER")
BOT_OUTPUT = "O-oooooooooo AAAAE-A-A-I-A-U- JO-oooooooooooo AAE-O-A-A-U-U-A" + \
             "-E-eee-ee-eee AAAAE-A-E-I-E-A-JO-ooo-oo-oo-oo EEEEO-A-AAA-AAAA"
USER_AGENT = 'TestingBrainPowerBot:v1.0.0 (By /u/geomdung-i)'


def main() -> None:
    """
    Execute the Brain Power Bot.
    """

    # Create a new reddit object
    r = praw.Reddit('brainpowerbot', user_agent=USER_AGENT)
    print("Initializing Brain Power Bot...")

    # Infinite loop to keep the bot running
    while True:
        print("Scanning for copious amounts of brain power...")
        brain_power_scanner(r)


def brain_power_scanner(r: praw.Reddit) -> None:
    """
    Scans the comment stream of the Reddit session r for instances of comments
    containing phrases in BOT_TRIGGERS. If such a comment is found, reply to
    it with BOT_OUTPUT. Ignores comments that have already been replied to by
    the bot.
    """
    print("Retrieving comments...")

    # Scan for comments
    # To scan only a particular subreddit, replace "all" with its name.
    for comment in r.subreddit("YELIANGFANCLUB").comments(limit=None):
        print("Scanning Comment...")
        responded = False

        # Search for trigger phrases in the comment
        for phrase in BOT_TRIGGERS:

            if phrase in comment.body:
                # Check to see if the bot has already responded
                for reply in comment.replies:
                    if reply.author.name == "Brain-Power-Bot":
                        print("Already replied to this comment.")
                        responded = True
                        break

                if not responded:
                    print("BRAIN POWER DETECTED!")
                    make_reply(comment)
                    break


def make_reply(c: praw.models.Comment) -> None:
    """
    Post a reply to the comment c with BOT_OUTPUT
    """
    # Post a reply if possible
    try:
        print("Posting Reply...")
        c.reply(BOT_OUTPUT)
        print("Reply Made")

    # If reddit returns an error
    except Exception as e:
        print("Reddit returned an error, no reply was made.")


if __name__ == "__main__":
    main()
