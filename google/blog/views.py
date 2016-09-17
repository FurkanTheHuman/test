from django.http import HttpResponse
import random

def index(request):
    htmlCode='''
<html>
<head>
<link href="https://cdn.quilljs.com/1.0.3/quill.snow.css" rel="stylesheet">

</head>

<body>


<!-- Create the editor container -->
<div id="editor">
  <p>Hello World!</p>
  <p>Some initial <strong>bold</strong> text</p>
  <p><br></p>
</div>

<!-- Include the Quill library -->
<script src="https://cdn.quilljs.com/1.0.3/quill.js"></script>

<!-- Initialize Quill editor -->
<script type="text/javascript">
  var quill = new Quill('#editor', {
    theme: 'snow'
  });
</script>
</body>

</html>
'''



    return HttpResponse(htmlCode)



'''
text=''
for i in range(100):
    text=text+'<h'+str((i%5)+1)+' style=\'color:#'+str(random.randint(100000, 1000000-1))+'\' >( ͡° ͜ʖ ͡°)'+str(random.randint(0,10000))+'</h'+str((i%5)+1)+'> '

'''
