# **Tatzt Tattoo**

## **Backend Development Project - Code Institute**

&nbsp;
![website mockups]()

Tazty Tatto is a e-commercer website created to sell custom and pre-designed tattoos from a local Tatoo Artist. The objective of this website help the artist to merchandise his tattoo products and make easier for his customer to buy a tattoo session.

This is my final project of the Code Institute Full Stack Developer course, and aims to show an interactive e-commerce website using a full technologie stack, from the Front End to the Back End and Databases. 

Access the website here: [Tatzy Tattoo](http://tatzy-tatoo.herokuapp.com/)

&nbsp;

## **Table Of Contents**

- [User Experience](<#user-experience-(ux)>)
- [Design Process](#design-process)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)

&nbsp;

## **User Experience (UX)**

### **Project Goals:**

- Display a home page with call to actions to the the products available for purchase, the photos of the last works made by the artist, and his location.
- Have a product page for customers to buy a custom tattoo, where they can selet the kind or work they want, the size of their tatto and upload a reference image, which calculates automaticaly the price.
- Merchandise the Artist pre-made tattoo desings, displaying its price, size and time to complete, and where the customer can easly buy it.
- Hava a User database where merchants can login in the website and have control of their past orders.
- Have a management area where only the Admin can access to add new Doodle products or images to the Gallery.
- Hava a cart and checkout, making possible to buy more then one product at once.

### **User Stories**

#### **New Users:**

- I'm looking for a tattoo artist to have a new custom tattoo of a cool desgin my sister drew for me.
- I want a new tattoo, but I'm out of ideas and would like to check what the tattoo artist have available and ready.
- I looking for a tattoo artist work, and would like to see his past works so I can be sure that he is the right one for me.

#### **Returning User:**

- I bought a custom tattoo a week ago and would like to check my order information.
- I got a Doodle tattoo last month and now I'd like to buy a new custom one.

#### **Business Owner:**

- I'm a tattoo artist and would like to make the process to buy a tattoo from me easier
- I have loads of pre-made designs, and would like to merchandise those Doodles, so my customers can easly find and by them.
- I need a wesite where I can simply manage the Doodles available, and add my newest works in a image Gallery.

## **Design Process**

### **Strategy Plane:**

The main objective of this website is to make easier for customer to buy tattoos from this artist, as he does not have anyone working for him to attend those clients. The time he spend negociating tattoo can be much better used tattooing his clients.

For that, the owner decided to request the creationg of a simple and straightforward e-commerce, where his customer can easily buy their tattoos online.

### **Scope Plane:**

The key features that this project aims to attend are:

- A custom tatto page that automaticaly caculate the final price depending on the work type and size
- A page with the Collection of Doodles available, where the merchant access the Doodle page to buy it.
- An image Gallery page where customers can see the artist last works.
- A seemless Cart and Checkout process, where customer can easily buy the website products.
- A User database where the artist will have his customer information saved in case he needs for a future project, which also provides Login/Sign in sytem on his store.

### **Skeleton Plane:**

The wireframes of this project aimed to create simple but effective pages, where the information can be seen and collected easily, and only necessary elements are displayed. For that, it was decided that the website wouldn't have many images, so it can load fast as well.

The layout of the wireframes was designed using Figma, as a starting point of how to display the project goal in a simple and direct format, on any kind of device.

To improve page load speed, it was decided to not add external Font styles in this project. The visual style was developed taking into consideration the elements and styles available on the Materialize CSS Framework, that will be used to develop the website.

### **Wireframes**:

The project wireframes can be accessed [FIXclicking here]().

Mobile:

![wireframe mobile]()

Tablet / Desktop:

![wireframe tablet and desktop]()

### **Surface Plane:**

The desing of this store was created to relate to the artist work, which is minimal, edgy and detailed. The Doodles are displayed on custom product cards, that provides all the important necessary of those products.

The color scheme is almost complete black, as the color of the artist ink. It was uses also some shades of grey to smooth some parts, and some whites to let thinks stand out, such as buttons and texts. 

![collor pallet](documentation/color_scheme.png)

The icons used in the website are from [Font Awesome](https://fontawesome.com/) and were used in the Header sections and some buttons.

All pages can be easily accessed through the Header navigation menu, which in the mobile view is displayed through a hamburger icon and a colappisble menu for the best usage of space. The Custom, Doodles and Gallery pages can be also accessed through the Homepage navigation sections (View more buttons).

The Search box slides from the top of the page, so it does not take to much space on the store layout. There a customer can search for any term that is on the Doodles product name or descrition. 

On the Doodles Coolection page the product cards can be reorded by Price, Name, Size or Time to Complete. The Profile page show the customer address information saved, and their last orders.

The Admin user has access management pages, where they can add new Doodles products and images to the Galery. He will also have access to buttons do delete of edit Doodles in the Collection page, or to edit or delete images on their page.

## **Features**

Through the Header Navigation menu that is common to all pages, the user can access all project features that are displayed on different pages. Either by the navigation menu links, or the icons.

### **Consistent features across all pages:**

- The responsive Header section that has the navigation menu, logo and icons (Search, Profile and Cart)
- Footer section with project information and social media links. As the idea is to help the artist to save time, it was decided to don't display any contact information or page, as this is preferably done by the owner social accounts.
- Search box that can be toggled on and off to be visibale and can be used to search Doodles by specifc terms found on their Name or Description.

### **Home:**

- A Hero Banner section with a CTB button suggest to customers to buy a Custom Tattoo.
- A section with the latest Doodles available uploadeds, and a button to the Doodles Collection page.
- The Gallery section with the latest work photos uploaded, and a button to the Gallery page.
- A map showing the location the artist studio.

### **Custom:**

- This page has a generic custom image, and a brief decription about what is the product.
- It is provided selector to select the work type and size, which has diferent price indexes saved in the model, which is used to calculate and update the custom tattoo price.
- It also provided a input field to upload the reference image, and all fields are required.
- An Add to Cart button so the customer can buy this product
- A Product Recomendation section that display availables Doodles to try to upsell them.

### **Dooodles:**

- A Collecion page with all Doodles available. For performance pruposes, it is only displayed 8 card per page, and the pagination buttons are displayed at the bottom to access other pages.
- The Doodles cards have the most important information for customer, such as Price, Size and Time to Complete.
- For the Admin it is also displayed buttons where it is possible to delete or edit a Doodle.

### **Doodle page:**

- This page displays the Doodle product image, name, description, size and estimated time to complete.
- An Add to Cart button so the customer can buy this product
- A Product Recomendation section that display availables Doodles to try to upsell them.

### **Gallery:**

- A Gallery of images that are automaticaly fitted in a Grid desing to be as dense as possible, takeing in cosideration the image width and height to calculate how it will be displayed.
- On hover, it is possible to see the image name and description
- For performance pruposes, it is only displayed 9 images per page, and the pagination buttons are displayed at the bottom to access other Gallery pages.

### **Image page:**

- This page displays the image in a bigger format for better visualization.
- At the top is possible to see the image name and its description.
- The Admin will be able to see buttons do delete or edit the image.

### **Cart page:**

- A section with all product in the Shopping Cart, as well as their specifc informaiton and a buttons to remove it from the Cart.
- A summary of their Cart, which the total number of item and grand total.
- A Product Recomendation section that display availables Doodles to try to upsell them.

### **Checkout page:**

- A section with all product in the Shopping Cart, as well as their specifc informaiton.
- A section with the grand total.
- A form where the customer can add their details, addresss and credit card info to complet the purchase.
- A button to go back to the Cart page, and one to finalize the Checkout.

### **Profile:**

- Form that shows the user address information save in the database, which can be changed and updated.
- A button to log out
- A section with a summary of their last order.

### **Search:**

- This page show a collection of Doodles cards that has the searched term on their Name or Description.

### **Managemetn / Add new Doodle :**

- On this page that can be accessed only by the Admin, it is provided a form to upload a new Doodle to the Doodles Collection.

### **Managemetn / Add new Gallery Image :**

- On this page that can be accessed only by the Admin, it is provided a form to upload a image to the Gallery.

### **Features I could implement in the future:**

- Add the possibility to select the body part area to be tattoo on the Custom page.
- A feature to select the available dates to tattoo on the Cart page.

## **Technologies Used**

### **Database**

The databases where generated through the Django Models, which provides a greate way to create relationshing between tables and easly do any CRUD on them. On production the databases are saved on Postgres provided by Herohu.

#### **Database structure:**

![Database Structure](documentation/db_diagram.jpg)

### **Languages, libraries, frameworks, editors, and version control**

- HTML5 - To create and add content to the website.
- CSS3 - To style the website content and provide responsiveness.
- [Materialize CSS](https://materializecss.com/) - This framework was used as a basic structure of the website, and for some pre made componets like the responsive navigation menu and toast pop up messages.
- JavaScript - Used to display displayed the components from Materialize CSS and to animate the Index form slider.
- [jQuery](https://jquery.com/) - Javascript library to manipulate the website content
- Python - To write the backend code
- [Django](https://flask.palletsprojects.com/en/1.1.x/) - Python Framework to manage templates, routes, queries and databases.
- [VS Code](https://code.visualstudio.com/) - The development tool used to write the website code
- [GitHub](https://github.com/) - Used for version control and host files.
- [Heroku](https://www.heroku.com/) - To deploy application

### **Other Tools Used**

- [Figma](https://figma.com/) - To create website wireframes.
- [Unsplash](https://unsplash.com/) - Project photos (Hero banner and Gallery)
- [Pinterest](https://in.pinterest.com/) - Doodles images
- [Font Awesome](https://fontawesome.com/) - Icons on Events and Riders page
- [dbdiagram.io](https://dbdiagram.io/) - Used to create databases diagrams on Readme file

### **Educational Resources**

- [Code Institute](https://courses.codeinstitute.net/) - Main source of content where the project inspiration and code design came from-
- [CSS Tricks](http://css-tricks.com/) - Mainly used as a resource to help with Flexbox positioning
- [Stack Overflow](https://stackoverflow.com/) - Used to find the reason for some errors found during the website development and for code inspiration to create the background aurora effect.

## **Testing**
FIX
### **Testing User Stories:**

- New user:
  - Looking for a new exercise web application on the internet, I found FED and could register my account and add new exercises to it.
- Returning user:
  - I accessed the web application at the Gym through my smartphone and could access my exercise program and modify it when I needed it.
- Business owner:
  - I’m pleased with the consistency of the design on different devices. Having the App Status page information is really helpful to understand how many users I have at the moment.

### **Manual testing**

- CRUD functionalities tested on Program, Editor, Add and Edit Exercises pages:
  - Add Exercise button
  - Add Exercise form
  - Edit Exercise button
  - Edit Exercise form
  - Delete Exercise button
  - Read Exercises lists through application pages
- Navigation tests:
  - Tested Navigation menu links on Desktop
  - Tested Navigations sidebar links menu on Mobile
  - Tested Page cards on the Home page
- Tested error pages
- Tested access to the App Status page only for Admin user
- Tested on all input fields forms to accept only characters acceptable by the code pattern
- Tested Search page looking for "Triceps", "Squal", "Biceps" and adding the found exercises cards to my own program
- Tested Profile page comparing information loaded with Database information

### **Validating The Code:**

- All HTML files validated with [W3C Markup Validation Service](https://validator.w3.org/) - No real HTML code errors found
- CSS file validated with [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - No real CSS code errors found
- The Javascrip files viladated with [JSHint](https://jshint.com/) - No real Javascrip code errors found
- Python code files validaded with [PEP 8 online](http://pep8online.com/) - No Python code errors found

### **Browsers testing**

Website tested on the following browsers manually, no error found

- Chrome
- Safari
- Mozilla Firefox
- Microsoft Edge

### **Responsiveness testing**

Website tested on the following devices manually or using Chrome Developer Tools, no error found

- iPhone X
- Ipad Pro
- Google Pixel
- MacBook Pro 16”
- Desktop Monitor Philips 25”

## **Deployment**

The project was written using VS Code, all files hosted on Github, Databases stored in MongoDB and deployed on Heroku, which can be accessed [clicking here](http://fitness-exercise-development.herokuapp.com/).

### **Local development**

To clone this project in your local machine you should certify that you have Git and Python installed locally, and follow the below steps:

1. Clone this repository in your machine using the command:

   ```
   gh repo clone pcantarelli/backend-Dev-project
   ```

2. Access / create an account on [MongoDB](https://www.mongodb.com/) to create your own databases to be used in this project.
3. Return to your Terminal and enter the following to install all required dependencies:

   ```
   pip3 install -r requirements.txt
   ```

4. Create an env.py file with the following content, replacing the 'mongo_secret_key', username','password', 'cluster_name' and 'database_name' with your MongoDB database values:

   ```
   import os

   os.environ.setdefault("IP", "0.0.0.0")
   os.environ.setdefault("PORT", "5000")
   os.environ.setdefault("SECRET_KEY", "<mongo_secret_key>")
   os.environ.setdefault("MONGO_URI", ""mongodb+srv://<username>:<password>@<cluster_name>.5urck.mongodb.net/<database_name>?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
   os.environ.setdefault("MONGO_DBNAME", "database_name")
   ```

5. Add your env.py file to .gitignore to make sure your database information is not viewable to others
6. Your cloned version is now ready to run locally with the following command:

   ```
   python3 app.py
   ```

### **Deploying project to Heroku**

To deploy this project, create your repository of this project in your Github account, create an account on [Heroku](https://www.heroku.com/), and follow the below steps:

1. On your Terminal, in the project directory folder create a requirements.txt file with the below command:

   ```
   pip3 freeze --local > requirements.txt
   ```

2. Created a Procfile with the below command, and ensures that it has an extra empty line on the last line of the file created:

   ```
   echo web: python app.py > Procfile
   ```

3. Commit and Push those changes to your repository on Github.
4. On your Heroku account, create a new app with the desired name.
5. On the 'Deployment Method' section of Heroku, link your GitHub profile and repository.
6. On the Config Vars section in the Settings tab, add the relevant key/value information from my env.py (IP, PORT, MONGO_URI, MONGO_DBNAME, SECRET_KEY).
7. On the "Deploy" tab. select Master Branch under "Choose a branch to deploy" and click "Enable Automatic Deploys".
8. Once de deployment is finished, clicked "View" to launch the app and see it on your browser.
9. All new Pushs to your Github repository will be automatically deployed on Heroku.

## **Credits**

### **Content**

This website was developed using the Code Institute project template that can be found on [this repository](https://github.com/Code-Institute-Org/gitpod-full-template). The Read.me file was based on Code Institute [readme-template](https://github.com/Code-Institute-Solutions/readme-template) on my previous projects Read.me files and on [Chloe's Read.me](https://github.com/chloelewisdev/milestone-project-3#Technologies-Used) file. Thank you so much for the inspiration.

Some base code sections are from [Materialize CSS](https://materializecss.com/) documentation, such as the Header, Navigation menu, Alert pop-up, and Collapsible accordions. The background aurora gradient color was inspired by the Stackoverflow discussion about [Instagram new logo CSS background](https://stackoverflow.com/questions/37751375/instagram-new-logo-css-background).

### **Media**

All icons are from [Font Awesome](https://fontawesome.com/).

### **Acknowledgments**

I’d like to thank the Code Institute tutors and support staff. Their support definitely helped me to achieve all my goals on this project. Thanks to Aaron Sinnott, my mentor, that also supported me during this project.
