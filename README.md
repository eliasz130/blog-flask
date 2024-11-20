# Flask Blog

A simple blog application built with Flask.

## Features

- View blog posts
- Read individual posts
- Responsive design
- About page

## Setup

1. Clone the repository:
```bash
git clone https://github.com/eliasz130/blog-flask.git
cd blog-flask
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py # or flask run
```

5. Visit `http://localhost:5000` in your browser

## Project Structure

```
blog-flask/
├── static/
│   └── styles.css
├── templates/
│   ├── about.html
│   ├── home.html
│   ├── layout.html
│   └── post_detail.html
├── app.py
├── posts.json
├── requirements.txt
└── README.md
```

## Contributing

Feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License.