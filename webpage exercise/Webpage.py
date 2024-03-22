class WebPage:
    def __init__(self,data):
        self.data = data
        self.next = None

class Historique:
    def __init__(self):
        self.head = None

    def BrowsePage(self, new_page):
        if self.head:
            last_page = self.head
            while last_page.next != None :
                last_page = last_page.next
            last_page.next = new_page

        else :
            self.head = new_page

    def DisplayHistorique(self):
        current_page = self.head

        while current_page != None :
            print(current_page.data)
            current_page = current_page.next

    def DeleteSite(self, siteName):
        current_page = self.head
        previous = None
        while current_page.next != None :
            previous = current_page
            current_page = current_page.next
            if current_page.data == siteName and current_page.next != None:
                current_page.data=current_page.next.data
                current_page.next=current_page.next.next

        if current_page.data == siteName and current_page.next == None:
            previous.next = None
    
    def goForward(self, target_page):
        current_page = self.head
        while current_page.data != target_page:
            current_page = current_page.next
        if current_page.data == target_page and current_page.next != None:
            current_page = current_page.next


    def goBack(self, target_page):
        current_page = self.head
        previous = None
        while current_page.data != target_page:
            previous = current_page
            current_page = current_page.next
        if current_page.data == target_page and previous != self.head:
            current_page = previous




l = Historique()
l.BrowsePage(WebPage("Google"))
l.BrowsePage(WebPage("Twitter"))
l.BrowsePage(WebPage("YouTube"))
l.BrowsePage(WebPage("Twitter"))
l.BrowsePage(WebPage("Discord"))
l.BrowsePage(WebPage("Twitter"))

l.DeleteSite("Twitter")

l.goForward("Google")
l.goForward("YouTube")
l.goForward("Discord")

l.goBack("Discord")
l.goBack("Google")

l.DisplayHistorique()
