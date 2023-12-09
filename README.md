# OIM-3640 Final_Project: 
## Amaon Price Check Website
Team Members:
- Jenny Luo
- Vicky Yan

## Purpose of the Project
Nowadays, people has increased their dependencies of shopping on Amazon due to its convinience. However, people have limited information about when the products are going to have a discount. We came up with this solution of allowing users to sign up by inputting the URL of their preferred Amazon product and their email, then the website would automatically inform the users whenever there is a discount. 

Nowadays, people rely heavily on the convenience of Amazon for their shopping needs. However, many customers lack sufficient information about when products will be discounted. To address this issue, we've developed a solution that allows users to sign up by simply inputting the URL of their desired Amazon product along with their email address. Our website will then automatically notify these users whenever there's a price drop or a discount available for their selected items. This service aims to keep usuers informed about the products' discounts, ensuring them never miss out on great deals.



## Website User Instructions
1. Install schedule package: Type "pip install schedule" and press "enter" in your command prompt
2. Open the website to access the home page.
3. There are two options for you to go to in the home page, "About" and "Amazon Price Check Machine". 
    - By pressing "About", you will be redirected to the "about" page, which introduces you the website, its functions, and contact. 
    - By pressing "Amazon Price Check Machine", you will be redirected to the "Amazon Price Check Machine" page, which you can input your Amazon product's URL and email. Then, you will be redirected again to the result page, which might have two results.
        - Result 1: If your item is already in discount, the website would inform you and send you an email about its detail shortly.
        - Result 2: If your item is not in discount yet, the website would inform you and ask you to wait patiently for the email. 
4. If your input information on the "Amazon Price Check Machine" has any typo or cannot be understand by the website, it would redirect you to an error page and ask you to try again. 

## Project Reflection and Future Improvements
Through this project, we've practiced what we've learned during class to solve a real world problem, which we are very proud of. In addition, we asked for external help from both professor and ChatGPT. This allowed us to gain external insights and keep on the right track of our project. We specifically learned some new functionalities of Python, like "schedule" and "thread", which are extremely practical and useful. Still, our website project is lack of some sort of versatility and can be further improved. For example, users currently can only input one product at one time. In the future, we can definitely allow users to track the prices of multiple products at the same time. We could also explore other functions. For example, we could enable users to only input the product's name and find the best price and deal for the user. 