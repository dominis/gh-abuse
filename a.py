import datetime
from random import randint
import subprocess

def get_date(n, startdate):
    d = startdate - datetime.timedelta(days=n)
    rtn = d.strftime("%a %b %d %X %Y %z -0400")
    return rtn

def main():
    c = 1
    for i in reversed(range(0, 365)):
        curdate = get_date(i, datetime.date.today())
        num_commits = c*10
        for commit in range(0, num_commits):
            subprocess.call("echo '" + curdate + str(randint(0, 1000000)) +"' > realwork.txt; git add realwork.txt; GIT_AUTHOR_DATE='" + curdate + "' GIT_COMMITTER_DATE='" + curdate + "' git commit -m 'update';", shell=True)

        if i%30 == 0:
            subprocess.call("git push;", shell=True)

        c += 1
        if c > 4:
            c = 1

    subprocess.call("git rm realwork.txt; git commit -m 'delete'; git push;", shell=True)

if __name__ == "__main__":
    main()
