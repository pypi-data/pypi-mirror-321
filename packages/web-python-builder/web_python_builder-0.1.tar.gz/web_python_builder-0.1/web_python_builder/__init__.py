class HTML:
    def __init__(self, title="My Webpage"):
        self.title = title
        self.head = f"<title>{self.title}</title>"
        self.body_content = []

    def add_element(self, tag, content="", **attributes):
        attr_str = " ".join(f'{key}="{value}"' for key, value in attributes.items())
        element = f"<{tag} {attr_str}>{content}</{tag}>"
        self.body_content.append(element)

    def add_link(self, href, text):
        self.add_element("a", text, href=href)

    def add_image(self, src, alt="Image"):
        self.add_element("img", "", src=src, alt=alt)

    def render(self):
        head = f"<head>{self.head}</head>"
        body = "<body>" + "".join(self.body_content) + "</body>"
        return f"<!DOCTYPE html><html>{head}{body}</html>"

    def save(self, filename="index.html"):
        with open(filename, "w") as file:
            file.write(self.render())
        print(f"HTML file saved as {filename}")
