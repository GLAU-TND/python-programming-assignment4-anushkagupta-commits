lst = [
     ("a", 1),
     ("a", 3),
     ("a", 5),
     ("b", 2),
     ("b", 6),
     ("c", 1),
     ("c", 2),
     ("c", 3),
     ("c", 4),
     ("c", 5),
     ("d", 4),
     ("d", 5),
     ("d", 6),
     ("d", 7),
     ("e", 1),
     ("e", 3),
     ("e", 5),
     ("e", 6),
     ]
k = int(input())
websiteusers = dict{}
for i,j in lst:
    if i not inwebsiteusers:
       websiteusers[i] = set()
    websiteusers[i].add(j)
    
websites = list(websiteusers.key())
mostsimilar = list()
for i in range(len(websites)):
    for j in range(i+1,len(websites)):
        a,b=websites[i] ,websites[j]
        intersect = websiteusers[a] and websiteusres[b]
        union = websiteusers[a] or websiteusers[b]
        simiarscore = len(intersect)/len(union)
        heappush(mostsimilar,(similarscore,(a,b))
        
mostsimilar = [y for x,y in mostsimilar]
print(mostsimilar[:k])
