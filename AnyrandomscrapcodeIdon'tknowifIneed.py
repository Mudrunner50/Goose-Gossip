'''
Created on May 13, 2014

@author: lukester223
'''
    '''   
        f = open('usernames/' + username + '/' + username + '.txt', 'r')
    l = f.readlines()
    del l[3]
    del l[2]
    del l[1]
    del l[0]
    theirposts = []
    for x in l :
        n = open('usernames/' + username + '/' + x.strip() + '.txt', 'r')
        m = n.readlines()
        for k in m :
            theirposts.append(k.strip())
    theirposts2 = ' '
    for i in theirposts :
        theirposts2 += (i + '<br><br>\n')
    '''