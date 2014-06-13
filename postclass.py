'''
Created on May 8, 2014

@author: lukester223
'''
from os import listdir
class post():
    def __init__(self, title = '', author = '', content = ''):
        self.title = title
        self.author = author
        self.content = content
        if self.content != '' :
            f = open("usernames/" + self.author + '/' + self.title + '.txt' , 'w')
            f.write(self.content)
        else :
            f = open("usernames/" + self.author + '/' + self.title, 'r')
            content1 = ' '.join(f.readlines())
            self.content += content1

    @staticmethod
    def postgenerator(username = ''):
        userlist = []
        postlist = []
        
        a = listdir('usernames/')
        if a[0] == '.DS_Store' :
            del a[0]
             
        for b in a :
            userlist.append(b.strip())
        
        for user in userlist :
            if username == '' or username == user:
                filesinfolder = listdir('usernames/' + user + '/' )
                if filesinfolder[0] == '.DS_Store' :
                    del filesinfolder[0]
                onetoremove = username + '.txt'
                filesinfolder.remove(onetoremove)
                for filename in filesinfolder :
                    postlist.append(post(filename , user, ''))
                
        return postlist
                

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        