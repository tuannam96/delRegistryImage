import requests
input = input("Type your repository to delete: ")

def getRepo():
    rq = requests.get('http://10.9.2.151:5000/v2/_catalog', verify=False).json()['repositories']
    return rq
# print(getRepo())
def getImageTag(repo):
    rq = requests.get(f'http://10.9.2.151:5000/v2/{repo}/tags/list').json()['tags']
    print(rq[5:])
    return (rq[6:])
# getImageTag()
def getImageDigest():
    tags = getImageTag()
    arrTags = []
    for tag in tags:
        rq = requests.get(f'http://10.9.2.151:5000/v2/{input}/manifests/{tag}', headers = {'Accept': 'application/vnd.docker.distribution.manifest.v2+json' })
        arrTags.append(rq.headers['Docker-Content-Digest'])
    return arrTags
# getImageDigest()

def delImageTag():
    digests = getImageDigest()
    for digest in digests:
        rq = requests.delete(f'http://10.9.2.151:5000/v2/{input}/manifests/{digest}')
        print (f"Delete diget: {digest}")

# def delAll():
#     all_tags = []
#     all_repo = getRepo()
#     for repo in all_repo:
#         tags = getImageTag(repo)
#         all_tags.extend(tags)
#     print(all_tags)
#     # delAllTags(all_tags)

if __name__ == "__main__":
    delAll()
