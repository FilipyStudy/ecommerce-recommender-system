# Ecommerce Recomendation System
## How this project works?

I will run a machine learning algorithm to understand and recommend products to a client based on their reviews.

## What type of technology i am using?

- Git
- Python
- Pandas
- Matplotlib
- PostgreSQL

## First step:
#### Data visualization:

When you run the main.py script, you will be able to choice 2 options.
The option 1 you will see some graphs about the data that i am using to this project.
The project is composed by two databases, one for training and one for testing.
The database are structured like this:

| Classification | Title | Description of the review |
| -------------- | ----- | ------------------------- |
| 1 for negative | title | description               |
| 2 for positive | title | description               |
| -------------- | ----- | ------------------------- |

The data are exactly in 50 / 50 structure, so, i have 50% of negative reviews and the same for positive.

By this way, i just plot inside a circle to compare, and i become to this conclusion. The same occurs with the test data.

<img src="https://i.imgur.com/EyQwT0S.png" alt="Graph image" />

## Second step:
#### Machine Learning algorithm:

So, the second step i will train an algorithm with the data. This step is just a sketch about what i am thinking.
I will need to understand how they react to a product, so i will analyze the description and the title using the review number
(1 for negative and 2 for positive reviews) as a target variable. By this way the correct form is using a supervised learning application.
Then the user will have to review another product to maintain the simplicity of the project, and using this as new variables the server will understand the what type of product he can recommend to the user.

## Third step:

#### Recommending the product:

Here is another skecth for the future:
I will use flask to dinamically recommend the products based on their past reviews.

## Fourth step:

#### Business Inteligence:

And for the last step, then we need to collect the data and analize with a business tool. For the future i want to use PowerBI.