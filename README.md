# Shopping Website

This Django project is a simple shopping website that allows users to browse products, search for items, and view product details.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)

## Features

- Home page displaying a list of products.
- Search functionality to find products based on various criteria.
- Detailed product view with images, descriptions, and prices.
- Responsive design using Bootstrap.
- Admin panel to manage products and categories.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/alperengokbak/shopping_website.git
   cd shopping-website
   ```

2. Create a virtual environment and activate it:

   ```bash
   # macOS/Linux
   python3 -m venv env
   source env/bin/activate

   # Windows
   py -m venv env
   .\env\Scripts\activate
   ```

3. Run the following commands to install the dependencies and set up the database:

   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   ```

4. Create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Navigate to [http://localhost:8000](http://localhost:8000) in your browser.

## Usage

### Admin

The admin panel can be accessed at [http://localhost:8000/admin](http://localhost:8000/admin). Use the superuser account created in step 4 of the [Installation](#installation) instructions to log in.

### Home Page

The home page displays a list of products. Each product is displayed as a card with the product image, brand, description, and price. The products can be filtered by category using the sidebar on the left. The products can also be sorted by price using the dropdown menu on the right.

### Search

The search functionality allows users to search for products based on various criteria. The search bar is located at the top of the page. The search results are displayed as a list of products. Each product is displayed as a card with the product image, brand, description, and price. The products can be filtered by category using the sidebar on the left. The products can also be sorted by price using the dropdown menu on the right.

### Product Detail

The product detail page displays detailed information about a product. The product image, brand, description, and price are displayed.

## Project Structure

The project structure is as follows:

```bash
shopping-website/
├── products/
│   ├── migrations/
│   ├── templates/
│   │   └── products/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── shopping/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
│   ├── css/
│   ├── img/
│   └── js/
├── templates/
│   ├── home.html
│   ├── product_detail.html
│   └── search_results.html
├── .gitignore
├── db.sqlite3
├── LICENSE
├── manage.py
├── README.md
└── requirements.txt
```

## Data Model

The data model consists of two main entities:

### Category

- category_id: Primary key for the category.
- title: Title of the category.
- parent_category: Reference to the parent category (self-referential relationship).

## Product

- product_id: Primary key for the product.
- description: Description of the product.
- price: Price of the product.
- image: Image of the product.
- brand: Brand of the product.
- category: Reference to the category the product belongs to.

## Dependencies

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
- [django-extensions](https://django-extensions.readthedocs.io/en/latest/)
- [django-filter](https://django-filter.readthedocs.io/en/latest/)
