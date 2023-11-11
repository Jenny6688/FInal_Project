# Project Proposal

## The Big Idea

This Python project monitors the prices of Lululemon's top-selling products, specifically the Define jacket and Align legging. It notifies the user via email whenever there is a price drop for these items. It does this by scraping the product information from the web page for the price of the item and comparing it to its original price. If the price of the item falls below the original price, it sends the user an email with the new price as well as the description of the item. 

- Our project idea is adapted from this YouTube video: https://www.youtube.com/watch?v=Bg9r_yLk7VY  


## Learning Objectives: 
### Shared goals: 
Girls nowadays love to shop for clothes from Lululemon. However, the price of its products is relatively higher than other brands. Nevertheless, it's widely acknowledged that Lululemon's price points tend to be on the higher end compared to other brands. Moreover, everything runs out of stock in a very short period whenever there’s a discount. In this project, we came up with a solution that can detect the discount and send an email to notify the user immediately.  

### Jenny’s goals: 
To receive notifications when my preferred products are on sale and to apply the knowledge gained from our class to enhance this project. 

### Vicky’s goals: 
To apply the knowledge I learned during class while learning new insights and techniques using AI. I also hope to solve real-life problems beyond class. 


## Implementation Plan:
### Requests module: 
It allows sending HTTP requests and returns a Response Object with all the response data. (https://www.w3schools.com/python/module_requests.asp). We'll first set URL = the lululemon product’s URL; then we’ll be using request.get (URL, headers) to retrieve lululemon website’s data, and then process the data with beautiful soup library. 

	Import requests 

    URL = 	#lululemon product’s URL 

	page =  request.get (URL, headers=headers) 

 

### Beautiful soup library: 
It is designed to simplify the process of extracting data from web pages, in this case, we’ll be extract and process the title and price data.  (https://pypi.org/project/beautifulsoup4/)

    from bs4 import BeautifulSoup 

    soup = BeautifulSoup( page.content, ‘html parser’) 

    title = soup.find (id= “productTitle”).get_text() 

    price = soup.find (id= “pricelock_ourprice”).get_text() 

 

### smtplib library: 
It is a library that can help us send emails. (https://docs.python.org/3/library/smtplib.html)  

	Import smtplib 

	server = smtplib.SMTP(‘smtp.gmail.com’, 587) 

    server.ehlo()  

- Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server to identify itself when connecting to another email server to start the process of sending an email. (https://knowledge.validity.com/hc/en-us/articles/220223328-What-is-Extended-HELO-EHLO-) 
```
server.starttls() #encrypts our connection 

server.ehlo() 

server.login(‘#username’, ‘#password’) 

...

server.sendmail( 
    ‘#from address’,  
    ‘#to address’, 
    ‘message’ 
) 

server.quit() 
``` 
 

### Flask library: 
It helps to build web applications and APIs. We plan to use it to build our final websites to integrate all of our elements together and provide the audience with a good visualization. 

### Urllib. request library: 
This library makes HTTP requests to web servers and handles responses. We intend to use it to retrieve data from online websites by inputting URLs and API Keys. For example, we could use it to get the Lululemon’s products’ data, like price, product description, etc.  

### JSON library: 
It helps users to decode and encode data and provide a readable and neat data format.  

 

## Project Schedule: 

- By 11/20: Finish the part of extracting data from Lululemon websites. 

- By 11/27: Finish the part of monitoring price changes and sending out emails whenever there’s a price deduction. 

- By 12/5: Finish the website. 

- By 12/8: Format all code, add docstring and comments, etc.   

- 12/9: Final check and submission. 

 

## Collaboration Plan: 

We will foster collaboration in this project by maintaining regular communication on WeChat, conducting scheduled team meetings, and adhering to well-defined deadlines. Our approach includes a comprehensive pair program, leveraging our individual responsibilities and collaborative strengths to ensure effective team dynamics. Opting for the Agile development organizational structure enables us to make frequent adjustments and accommodate changes seamlessly. This flexibility allows us to revisit our code consistently for improvements. Recognizing debugging as an iterative process, we emphasize periodic reviews for refinement. 

 

## Risks and Limitations: 

Due to website safety, the website structure of Lululemon might change frequently, which might require us to modify our project. In addition, the products we focused on have various sizes and colors. Some may be out of stock while others are not. Also, some might be on discount while others remain at the original price. These may result in errors in the project and require big flexibility for our project, and we may not be able to solve some of the limitations with our current knowledge. If not, we have to modify the project. Another threat is that we have never conducted similar projects, so we aren’t sure about what we are facing. The time it actually takes might be much longer than what we expected, so we’d better start early and follow our schedule strictly.  

## Additional Course Content: 

Some libraries we intend to use in our projects have not been covered during class. We think it would be beneficial for our project if we could also talk about the Beautiful Soup Library and the Smtplib Library. We’d also love to learn how to add more user interfaces to our website to make the users more engaged.  

 