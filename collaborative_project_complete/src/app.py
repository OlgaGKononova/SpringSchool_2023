from project_web.index import app

server = app.server

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8053, use_reloader=True)