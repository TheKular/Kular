# test.py

from main import KularPy

if __name__ == "__main__":
    kular = KularPy()

    # Example usage
    kular.set_title("Welcome to My Website")
    kular.heading("Hello World", level=1)
    kular.para("This is a simple paragraph.")
    kular.para("You can add more content as needed.")
    kular.heading("About This Page", level=2)
    kular.para("This page is generated using Python.")
    kular.url("Click this link", "google.com")
    kular.para("Hello world", "hi")

    # Adding some CSS styles
    kular.add_css("body { font-family: Arial, sans-serif; }")
    kular.add_css("h1 { color: blue; }")
    kular.add_css("p { color: green; }")
    kular.add_css(".hi {text-align: center;}")

    # Save the generated HTML and CSS to files
    kular.save_to_file("web/index.html", "web/style.css")
