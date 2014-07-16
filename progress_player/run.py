#  I enabled debug support by passing it as a parameter so the server will reload itself on code changes, and provide me with a helpful debugger if things go wrong.


from app import app

app.run(debug=True, port=8000)

