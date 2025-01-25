from parallel_reqs import RequestExecutor 
from parallel_reqs import Request

# Lista di URL di esempio
urls = [
    "https://www.google.com",
    "https://www.bing.com",
    "https://www.yahoo.com",
    "https://www.wikipedia.org",
    "https://www.imdb.com",
    "https://www.amazon.com",
    "https://www.ebay.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.instagram.com",
    "https://www.corriere.it",
    "https://www.repubblica.it",
    "https://www.ansa.it",
    "https://www.rainews.it",
    "https://www.sky.it",
    "https://www.msn.com",
    "https://www.aol.com",
    "https://www.cnn.com",
    "https://www.foxnews.com",
    "https://www.bbc.com",
    "https://www.aljazeera.com",
    "https://www.nbcnews.com",
    "https://www.cbsnews.com",
    "https://www.abcnews.go.com",
    "https://www.npr.org",
    "https://www.pbs.org",
    "https://www.huffpost.com",
    "https://www.buzzfeed.com",
    "https://www.vox.com",
    "https://www.slate.com",
    "https://www.theverge.com",
    "https://www.wired.com",
    "https://www.arstechnica.com",
    "https://www.engadget.com",
    "https://www.cnet.com",
    "https://www.zdnet.com",
    "https://www.techcrunch.com",
    "https://www.theatlantic.com",
    "https://www.newyorker.com",
    "https://www.harpersbazaar.com",
    "https://www.vanityfair.com",
    "https://www.gq.com",
    "https://www.esquire.com",
    "https://www.menshealth.com",
    "https://www.womenshealthmag.com",
    "https://www.shape.com",
    "https://www.self.com",
    "https://www.cosmopolitan.com",
    "https://www.glamour.com",
    "https://www.allure.com",
    "https://www.vogue.com",
    "https://www.elle.com",
    "https://www.harpersbazaar.com",
    "https://www.marieclaire.com"
]

                                                                                   
def main():
        print("Urls: ", len(urls))
        executor = RequestExecutor()       
        try:
            for u in urls:
                executor.add_request(Request.create(url=u, method="GET"))
        except Exception as e:    
            print(e)

        responses = executor.run()
        print("Responses: ", len(responses))
        for response in responses: 
            print(f"Status Code: {response.status_code}, Execution Time: {response.execution_time} sec") 

        print( "Total: exec" , executor.execution_time)


main()
