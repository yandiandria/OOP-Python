from abc import ABC

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def login():
        pass
    def createNewThread(self, title, content, creationDate = "aujourd'hui",  file = None):
        if file :
            post = PostFile(content, self, creationDate, file)
        else :
            post = Post(content, self, creationDate)
        return Thread(title, creationDate, post)
    def answerThread(self, thread, content, file = None, creationDate = "aujourd'hui") :
        if file : #if the user puts a file
            post = PostFile(content, self, creationDate, file)
        else :
            post = Post(content, self, creationDate)
        thread.add_post(post)
    def display(self):
        return f"{self.username}"


class Moderator(User):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        def modify_post(self, post, new_content):
            post.content = new_content
        def delete_post(self, thread, post):
            thread.posts.remove(post)

# Amélioration possible : avoir le même type de comportement entre toutes les méthodes display() => soit print, soit return un résultat, mais pas faire
# soit l'un ou l'autre. 
class Thread:
    def __init__(self,title, creationDate, post):
        self.title = title
        self.creationDate = creationDate
        self.posts = [post]
    def add_post(self, post):
        self.posts.append(post)
    def display(self):
        header = f"THREAD -- Title : {self.title} -- Creation date : {self.creationDate}." 
        print(header)
        for post in self.posts:
            print(post.display())
        print("="*60)

class Post:
    def __init__(self, text, user,publicationDate):
        self.text = text
        self.user = user
        self.publicationDate = publicationDate
    def display(self):
        res = "-"*60 + "\n"
        res += f"{self.text} \n Published by : {self.user.display()} on {self.publicationDate}"
        return res

class PostFile(Post):
    def __init__(self, text, user, publicationDate, file):
        self.text = text
        self.user = user
        self.publicationDate = publicationDate
        self.file = file
    def display(self):
        super().display() # Permet d'appeler la méthode display de la classe parent (Post)
        print("Pièce jointe :")
        print(self.file.display())  


class File :
    def __init__(self, name, taille):
        self.name = name
        self.taille = taille
    def display(self):
        pass
class ImageFile :
    def display(self):
        return f"Le nom de l'image est {self.name}"

if __name__=="__main__":
    ## Initialisation de l'utilisateur 1 qui va créer un fil de discussion et y poster un message
    utilisateur1 = User("user1", "password")
    fichierRecette = File("recette.pdf",8)
    recetteGateau = utilisateur1.createNewThread(   "Nouvelle recette Tarte aux pommes",\
                                                    "Je vous envoie une nouvelle recette de tarte aux pommes, elle est formidable !",\
                                                    creationDate="03/11/2022")

    ## Affichage du fil de discussion après sa création :
    recetteGateau.display()

    print("")

    #Initialisation de l'utilisateur 2 qui répond à ce fil de discussion
    utilisateur2 = User("user2", "samepassword")
    utilisateur2.answerThread(recetteGateau, "Merci pour cette recette")

    recetteGateau.display()
