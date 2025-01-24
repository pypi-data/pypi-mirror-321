# HTML Generator Library - Python

## Overview
This library allows you to create and manage HTML files programmatically using Python. It simplifies generating dynamic HTML content, styling with CSS, and integrating JavaScript directly within your Python projects.

---

## Key Features

1. **HTML Element Creation**
   - Create basic and advanced HTML elements.
   - Support for paragraphs, headings, lists, tables, forms, and more.

2. **CSS Integration**
   - Inline styles and class-based styling.
   - Helper methods for layout management (Flexbox, Grid).

3. **JavaScript Support**
   - Embed custom JavaScript.
   - Handle events and form validation.

4. **Component-Based Templates**
   - Define reusable HTML components.

5. **File Management**
   - Automatically generate and save HTML files.
   
---

## Installation
```
pip install web_python_builder
```

---

## Usage

### Basic Example
```python
from html_generator import HTML

# Create a new HTML page
template = HTML(title="My First Webpage")
template.add_element("h1", "Welcome to My Website!")
template.add_element("p", "This is a dynamically generated paragraph.", style="color:blue;")
template.add_link("https://example.com", "Click here for more!")
template.save("index.html")
```
This code will generate an `index.html` file containing:
```html
<!DOCTYPE html>
<html>
<head>
<title>My First Webpage</title>
</head>
<body>
<h1>Welcome to My Website!</h1>
<p style="color:blue;">This is a dynamically generated paragraph.</p>
<a href="https://example.com">Click here for more!</a>
</body>
</html>
```

---

### Adding an Image
```python
template.add_image("logo.png", alt="Site Logo")
```

---

### Adding CSS
```python
template.add_css({"body": {"background-color": "#f0f0f0"}})
```

---

### Adding JavaScript
```python
template.add_script("alert('Welcome to my website!');")
```

---

## Advanced Features
1. **Form Generation**
   ```python
   form_data = {
       'name': 'text',
       'email': 'email',
       'submit': 'submit'
   }
   template.add_form(form_data)
   ```

2. **Component Reusability**
   ```python
   def navbar():
       return '<nav>My Navbar</nav>'

   template.add_template(navbar)
   ```

---

## Contribution
Feel free to contribute by creating a pull request. Suggestions and feature requests are welcome!

---

## License
This project is licensed under the MIT License.

