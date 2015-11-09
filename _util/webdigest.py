import sys
import yaml
import frontmatter
import datetime

def main(fname):
    d = datetime.date.today()

    with open(fname, "r") as f:
        entries = yaml.load(f)
    announce = entries['announce'] if 'announce' in entries else []
    meetings = sorted(entries['meetings'])
    jobs     = sorted(entries['jobs'])
    welcome  = entries['welcome'] if 'welcome' in entries else "Welcome to the online edition of the {0} SIAG LA digest.".format(d)
    
    print("---")
    print("title: SIAG LA digest")
    print("date: {0}".format(d))
    print("author: David Bindel")
    print("comments: true")
    print("---\n")
    print("\n")
    print(welcome)
    print("\n## CONTENTS\n")
    navk = 0
    for post in announce:
        print("- [{0}](#nav{1})".format(post['title'], navk))
        navk += 1
    for meeting in meetings:
        with open("../_meetings/{0}.md".format(meeting), "r") as f:
            post = frontmatter.load(f)
        print("- [{0}](#nav{1})".format(post['title'], navk))
        navk += 1
    for job in jobs:
        with open("../_jobads/{0}.md".format(job), "r") as f:
            post = frontmatter.load(f)
        print("- [{0}](#nav{1})".format(post['title'], navk))
        navk += 1
    print("- [Submissions for next SIAM-LA digest](#nav{0})".format(navk))

    navk = 0
    for post in announce:
        print('\n---------------\n\n## <a name="nav{1}">{0}</a>\n'.format(post['title'], navk))
        print(post['content'])
        navk += 1
    for meeting in meetings:
        with open("../_meetings/{0}.md".format(meeting), "r") as f:
            post = frontmatter.load(f)
        print('\n---------------\n\n## <a name="nav{1}"></a><a href="{2}">{0}</a>'.format(post['title'], navk, post['page']))
        print(post.content)
        navk += 1
    for job in jobs:
        with open("../_jobads/{0}.md".format(job), "r") as f:
            post = frontmatter.load(f)
        print('\n---------------\n\n## <a name="nav{1}">{0}</a>\n'.format(post['title'], navk))
        print(post.content)
        navk += 1

    d = datetime.date.today()
    dmon = d + datetime.timedelta(days=(7-d.weekday()))
    while dmon.month == d.month:
        dmon += datetime.timedelta(days=7)
    print('\n---------------\n\n## <a name="nav{0}">Submissions for next SIAM-LA digest</a>'.format(navk))
    print("""
The next SIAM-LA Digest is due to be sent out on {0:%b %d, %Y}.
Please send any postings for the next Digest to siam-la at siam.org. 
Only SIAG/LA members may submit postings.  To contact the list owner, 
send an email to siam-la-owner at siam.org.
""".format(dmon))
          
if __name__ == "__main__":
    main(*sys.argv[1:])
