import os
# We'll render HTML templates and access data sent by POST
# using the request object from flask. Redirect and url_for
# will be used to redirect the user once the upload is done
# and send_from_directory will help us to send/show on the
# browser the file that the user just uploaded
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

# Initialize the Flask application
app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'c:\\test'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    return render_template('index.html')


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = file.filename
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        # return redirect(url_for('uploaded_file',
        #                         filename=filename))
        return 'SUCCESS'


# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run(
        # open network
        host="0.0.0.0",
        port=int("80"),
        # debug mode
        debug=True
    )


# import os
# from flask import Flask, Response
# from flask import request
#
# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'tmp/'
# app.config['MAX_CONTENT_LENGTH'] = 16<<20  # max upload size < 16M
#
# @app.route('/')
# def index():
#     return 'Index Page'
#
#
# # @app.route('/hello/')
# # @app.route('/hello/<name>')
# # def hello(name=None):
# #     return render_template('hello.html', name=name)
#
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username
#
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id
#
#
# @app.route('/file', methods=['POST', 'GET'])
# def update_file():
#     """
#     Api for getting file & string data from MApp
#     Store data to local files
#     """
#     print 1
#     if request.method == 'POST':
#         # Get file object from field of file
#         print 1
#         f = request.files['userfile']
#         print 1
#         f.save(os.path.join('C:/test', f.filename))
#         print 1
#         # Get str object from field of text
#         s = request.form['name']
#         with open('C:/test/test.txt', 'a') as f:
#             print 1
#             f.write(s)
#     return 'Done!'
#
#
# @app.route('/hehe', methods=['POST','GET'])
# def upload_file():
#     if request.method == 'GET':
#         return 'Not GET'
#     file = reqest.files['file']
#     filename = file.filename
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#     return 'upload success'
