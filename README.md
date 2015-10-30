# SIAG-LA site design 2014

This document describes the re-design of the SIAG-LA web site as of
early November 2014.  This reflects some changes that I'd intended to
make since the start of my term as secretary of SIAG-LA; I hope these
changes will make it simpler not only for me and my successors to
maintain, but also for others to propose contributions.

## General design

The current site style is built on [Pure][pure], a small set of
responsive CSS modules from Yahoo.  In this setting, "responsive"
means that the site should adapt gracefully to different screen sizes
and window sizes.  The new design hues closely to Pure's
[side menu layout example][side], and I have in no way modified the
default CSS behavior from the Pure framework.

For content management, I am using [Jekyll 2.4.0][jekyll] a plain-text
static site generator.  Jekyll may be the most popular of the
available static site generators, in part because it is used in
[Github Pages][ghpages].  The chief goal of using Jekyll is to
separate the content from presentation, making it simpler to apply
general stylistic changes in the future.

Jekyll has the option of using different Unicode encodings.  My
preferred default would be UTF-8, but there is some issue that I don't
entirely understand that only appears on the SIAM server (vs local
deployment or GitHub pages) that causes UTF-8 symbols to be
mis-interpreted; so we're sticking with HTML entities for now.

The plan is to maintain the source code in a git repository on GitHub,
which will automatically be re-compiled and uploaded to the SIAM site
once a day.

## Posts

Posts are stored in the `_posts` subdirectory, and are named according
to the usual Jekyll convention (`YYYY-MM-DD-topic.extension`).
The [YAML][yaml] header should include title, date, and author:

    ---
    title: Title
    date: 2014-11-06 19:32:45 -0500
    author: David Bindel
    ---

Post excerpts are currently displayed on the main page in reverse
chronological order, immediately after the introductory text.
This will probably need to be paginated at some point, and perhaps
it will make sense to automatically generate an RSS feed; but not now.

## Conference records

By volume, the majority of the data on the SIAG-LA site relates to
past and future conferences.  It is good design in general to separate
data from presentation, and particularly so with something like
conference data that we want to keep up-to-date and to present in
several ways.  So I've created a `_meetings` subdirectory (a Jekyll
collection) with one file per record.  I format any text using
Markdown, and follow the same convention used for posts
(`YYYY-MM-DD-shortname.md`), where the date is the start date of the
conference.  This convention allows ordinary lexicographic ordering to
coincide with chronological ordering.  Each record includes the
conference name, an optional URL, the start and end dates, the
conference location, and the "type" of relation the conference has to
SIAG-LA:

- `sponsored`: Sponsored by SIAG-LA
- `cooperation`: In cooperation with SIAG-LA
- `organized`: Organized by SIAG-LA
- `siam-la`: SIAM Linear Algebra Conferences
- `siam-la-biz`: SIAG-LA business meetings
- `issnla`: SIAG-LA summer school on numerical linear algebra

The type of the conference can be left blank to indicate that there
is no particular relation to SIAG-LA other than that the conference
may be of interest to members.  The conference record YAML looks like

    ---
    title: Twelfth SIAM Conference on Applied Linear Algebra
    page: http://www.siam.org/meetings/la15/
    start_date: 2015-10-26 12:00:00
    end_date:   2015-10-30 12:00:00
    where: Atlanta, Georgia
    type: siam-la
    ---

    The call for papers will be posted in December 2014.

Note that the dates *must* include a time field as well as a date
in order for the template to work properly.  This has to do with the
way that Ruby handles the distinctions between dates, times, and
strings; I tried to get the logic to work even if I just specified
dates, but after a few minutes I just moved on.  This could be
improved.

The script `meeting.sh` in the `_util` directory automatically
creates a new meeting record with the appropriate format.

The conference page has tabs that display summaries of all conferences
and more complete information for a subset of conferences (upcoming
conferences, SIAM LA meetings, summer schools).  There is currently no
way to see the full text records for arbitrary past meetings through
the web page.  This is not different from how the site worked before,
but could perhaps be improved.

The templating system ensures that the formatting on these pages is
consistent; it does nothing to help with correctness of the records.
Ideally, if I've made data entry errors, someone will be able to call
me on it.

## Job postings

Job advertisements posted to the SIAG-LA mailing list are copied into
the `_jobads` subdirectory.  Job ads are posted in reverse chronological
order by posting date on the jobs web page.  Only ads that have not
passed their closing date are listed.

Unlike conferences, job ads do not get their own pages.  The reasoning
is that a past conference is still likely of interest (and there are
many of them), while past job ads are less interesting.  The data
remains in the repository, so someone could change their mind about
this in the future.

The job record YAML looks like:

    ---
    title: 
    page:
    posted:
    closes:
    ---

If no closing date is explicitly mentioned, I default to two months
after the posting.

## Forms for job and conference postings

Job and conference advertisements can be submitted through email
or via a Google Forms setup.  The forms have an attached script
to email submitters when they have successfully submitted an
advertisement.  The `sync-jobs.py` and `sync-conf.py` scripts under
the `_util` subdirectory create appropriately-formated files for
inclusion under the `_meetings` and `_jobads` directories.  For
example, to post a new conference ad submitted via the web form,
one might (for example) do:

    cd _util
    python sync-conf.py
    cp 2015-10-01-foo.md ../_meetings
    git add ../_meetings/2015-10-01-foo.md
    git commit -m "Added foo meeting"
    git push origin

Note that the `sync-conf.py` script and `sync-jobs.py` script require
`pandas`, `gspread`, and `oauth2client`.  All of these can be
installed via `pip`.

## SIMAX papers

Information on recent SIMAX papers is automatically scraped from the
SIMAX RSS feed by the `_util/parse-simax-feed.py` script.  The current
database is saved in YAML format in `_data/simax.yml`.  The scraper
runs automatically once a day; if there are any new papers, this will
trigger a site re-generation.  The `simax.html` template is
automatically populated from the ten most recent papers, displayed
in reverse chronological order immediately after the introductory
text.

Unfortunately, Jekyll doesn't seem happy to convert UTF-8 to HTML
entities on the fly, so the scraper script does the conversion
(and saves the version with HTML entities in the database).

## Prizes and officers

Information about the officers is saved in `_data/officers.yml`;
information about the SIAG/LA prize winners and their papers
is in `_data/prizes.yml`.  Formatting information is given at
the start of each file.

The prizes before 2003 were not previously listed on the SIAG-LA web
site.  This has been addressed to the best of my knowledge, but it
took some digging to find the papers associated with the earlier
prizes.  Again, I hope that if I've made errors, someone will call
me on it.

[pure]: http://purecss.io/
[side]: http://purecss.io/layouts/
[jekyll]: http://jekyllrb.com/
[ghpages]: https://pages.github.com/
[yaml]: http://jekyllrb.com/docs/frontmatter/
[tpw]: http://tom.preston-werner.com/2008/11/17/blogging-like-a-hacker.html
