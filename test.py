# test.py

from main import HTMLGenerator

if __name__ == "__main__":
    generator = HTMLGenerator()

    # Example usage
    generator.set_title("Welcome to My Website")
    generator.heading("Hello World", level=1)
    generator.para("This is a simple paragraph.")
    generator.para("You can add more content as needed.")
    generator.heading("About This Page", level=2)
    generator.para("This page is generated using Python.")
    generator.url("Click this link", "google.com")

    # Adding some CSS styles
    generator.add_css("body { font-family: Arial, sans-serif; }")
    generator.add_css("h1 { color: blue; }")
    generator.add_css("p { color: green; }")

    # Save the generated HTML and CSS to files
    generator.save_to_file("web/index.html", "web/style.css")