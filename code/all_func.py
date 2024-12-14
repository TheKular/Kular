from main import zosnel

zosnel = zosnel()
zosnel.set_title("My Website")
zosnel.heading("Welcome!")
zosnel.para("This is a test paragraph")
zosnel.add_css("body { background-color: #f0f0f0; font-family: sans-serif;}")
zosnel.serve()