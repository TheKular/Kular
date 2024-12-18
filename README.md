#
# Zosnel &middot; ![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
[Zosnel] is a project helping Python developers write code in HTML, CSS, JS all while using Python. Currently the project is in development and not ready for full public use.

Zosnel (Zo - Snel) is a open source project made for easy creation of websites using only python.

#
# How to use Zosnel?
in the code provided you can learn a bit about how Zosnel works. 

*main file*

    from zosnel import zosnel  # Import Zosnel

    # Create an instance of the ZOSNEL class
    zosnel = zosnel(port=8000)

    # Set the page title
    zosnel.set_title("Testing ZOSNEL Framework")

    # Add HTML content
    zosnel.heading("Welcome to ZOSNEL!", level=1)
    zosnel.para("This paragraph is added using the 'para' method.")
    zosnel.url("Click here to visit GitHub", "https://github.com")
    zosnel.img("https://via.placeholder.com/150", alt="Sample Image")
    zosnel.sep()
    zosnel.breakline()

    # Add CSS
    zosnel.add_css("""
    body {
        font-family: Arial, sans-serif;
        margin: 20px;
        text-align: center;
        background-color: #f0f8ff;
    }

    h1 {
        color: #4CAF50;
    }

    button {
        padding: 10px 20px;
        margin-top: 20px;
        background-color: #007BFF;
        color: white;
        border: none;
        cursor: pointer;
    }

    button:hover {
        background-color: #0056b3;
    }
    """)

    # Add JavaScript
    zosnel.javascript("""
    document.addEventListener("DOMContentLoaded", function() {
        alert("Hello from ZOSNEL's JavaScript!");
        console.log("JavaScript is working!");
    });

    function onButtonClick() {
        alert("Button clicked!");
    }
    """)

    # Add custom HTML with inline JavaScript
    zosnel.custom('<button onclick="onButtonClick()">Click Me</button>')

    # Serve the site
    zosnel.serve()

If you want to see what the final result looks like you can try using it! 

* *Please note that this project is still under development and errors could occur, please understand that this project is under development still and not perfect.*