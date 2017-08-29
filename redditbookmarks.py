import praw
from praw.models import Submission
from bs4 import BeautifulSoup


def Authenticate():
    reddit = praw.Reddit('RedditBookmarks',user_agent='Bookmark exporter v1.0')
    print("Authentication as {} successfull".format(reddit.user.me))
    return reddit




def main():
    #Login
    reddit = Authenticate()
    r_user = reddit.user.me()

    saved = r_user.saved(limit=None)

    #Open file
    with open("struc.html") as fp:
        soup = BeautifulSoup(fp,'html.parser')



    tag = soup.find('p')
    for link in saved:
        if(isinstance(link,Submission)):
            new_tag = soup.new_tag('DT')
            new_tag.append(soup.new_tag('A',HREF = link.url))
            tag.append(new_tag)



    #Save file
    with open("output.html", "w") as file:
        file.write(str(soup).replace("</DT>","\n").replace("</p>"," "))

if __name__ == "__main__":
    main()