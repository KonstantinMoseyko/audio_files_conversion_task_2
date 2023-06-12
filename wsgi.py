from core.app import app
from core.api import download


if __name__ == "__main__":
    app.add_url_rule(
        '/download', 
        'download_file',
        download, 
        methods=['GET']
    )
    
    app.run(
        host='0.0.0.0',
        debug=True,
    )
    