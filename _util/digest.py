import sys
import yaml
import frontmatter
import datetime

def main(fname):
    with open(fname, "r") as f:
        entries = yaml.load(f)
    announce = entries['announce'] if 'announce' in entries else []
    meetings = sorted(entries['meetings'])
    jobs     = sorted(entries['jobs'])

    print("CONTENTS\n")
    for post in announce:
        print("* {0}".format(post['title']))
    for meeting in meetings:
        with open("../_meetings/{0}.md".format(meeting), "r") as f:
            post = frontmatter.load(f)
        print("* {0}".format(post['title']))
    for job in jobs:
        with open("../_jobads/{0}.md".format(job), "r") as f:
            post = frontmatter.load(f)
        print("* {0}".format(post['title']))
    print("* Submissions for next SIAM-LA digest")

    for post in announce:
        print("\n---------------\n\n** {0}\n".format(post['title']))
        print(post['content'])
    for meeting in meetings:
        with open("../_meetings/{0}.md".format(meeting), "r") as f:
            post = frontmatter.load(f)
        print("\n---------------\n\n** {0}".format(post['title']))
        print("   {0}\n".format(post['page']))
        print(post.content)
    for job in jobs:
        with open("../_jobads/{0}.md".format(job), "r") as f:
            post = frontmatter.load(f)
        print("\n---------------\n\n** {0}\n".format(post['title']))
        print(post.content)

    d = datetime.date.today()
    dmon = d + datetime.timedelta(days=(7-d.weekday()))
    while dmon.month == d.month:
        dmon += datetime.timedelta(days=7)
    print("\n---------------\n\n** Submissions for next SIAM-LA digest")
    print("""
The next SIAM-LA Digest is due to be sent out on {0:%b %d, %Y}.
Please send any postings for the next Digest to siam-la at siam.org. 
Only SIAG/LA members may submit postings.  To contact the list owner, 
send an email to siam-la-owner at siam.org.
""".format(dmon))
          
if __name__ == "__main__":
    main(*sys.argv[1:])
