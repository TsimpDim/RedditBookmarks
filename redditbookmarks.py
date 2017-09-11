import praw
from praw.models import Submission
from bs4 import BeautifulSoup


def authenticate():
    '''Authenticate using praw.ini'''
    reddit = praw.Reddit('RedditBookmarks', user_agent='Bookmark exporter v1.0')
    print("Authentication as {} successfull".format(reddit.user.me))
    return reddit




def main():
    '''Build the HTML file'''

    #Login
    reddit = authenticate()
    r_user = reddit.user.me()

    saved = r_user.saved(limit=None)

    #Create file
    html_file = open('RedditBookmarks.html', 'w')



    soup = BeautifulSoup("<!DOCTYPE NETSCAPE-Bookmark-file-1>", "html.parser")
    meta_tag = soup.new_tag('META')
    meta_tag['HTTP-EQUIV'] = "Content-Type"
    meta_tag['CONTENT'] = "text/html; charset=UTF-8"
    soup.append(meta_tag)

    title_tag = soup.new_tag('TITLE')
    title_tag.string = "RedditBookmarks"
    soup.append(title_tag)

    header_tag = soup.new_tag('H1')
    header_tag.string = "RedditSaved"
    soup.append(header_tag)

    dl_tag = soup.new_tag('DL')
    dl_tag.append(soup.new_tag('p'))
    soup.append(dl_tag)
    soup.append(soup.new_tag('p'))

    tag = soup.find('p')
    for link in saved:
        new_tag = soup.new_tag('DT')

        if isinstance(link, Submission):
            content = soup.new_tag('A', HREF=link.url)
            content.string = link.title.strip()
        else:
            content = soup.new_tag('A', HREF=link.submission.url)
            content.string = link.id


        new_tag.append(content)
        tag.append(new_tag)



    #Save file
    html_file.write(str(soup).replace("</DT>", "\n").replace("</p>", " "))

if __name__ == "__main__":
    main()
