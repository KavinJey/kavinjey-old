#Purpose: open html file and inject static shit such as header and footer, etc.


#Possible Improvements to script.
#ALLOW input for file name
#ALLOW differing html instead of just copy pasta
#ALLOW keywords to trigger certain writes of stuff
#(e.g LINK=myStyle.css produces <link href=myStyle.css>)


#CHANGE HTML FILE HERE
f = open('landscapes.html', 'r+')
number = input("How many pictures?")
subject = raw_input("Enter folder")

count = number / 3
count = int(count)
number = str(number)
subject = str(subject)

f.write('''<html>

<head>


<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- Fonts -->

<link href="https://fonts.googleapis.com/css?family=Merriweather|Source+Code+Pro" rel="stylesheet">

<!-- Bootstrap -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Custom CSS -->
<link rel="stylesheet" href="/../CSS/styles.css">


</head>



<body>


<div class="container-fluid">

  <nav class="navbar navbar-default navbar-fixed-top">
    <div class="container-fluid">
      <div class="navbar-header">
        <a href="rurikari.xyz">
          <p class="navbar-brand"> Kavin Jey </p>
        </a>
        </div>
        <ul class="nav navbar-nav navbar-text navbar-right ">
          <li><a href="/../index.html">Home</a></li>
          <li><a href="/../about.html">About</a></li>
          <li><a href="/../contact.html">Contact</a></li>
        </ul>
    </div>
  </nav>''')


for x in range(count-1):
    f.write('''\n\n
<div class="container-fluid">
  <div class="row">''')
    f.write('''
    <div class="col-md-3">
      <a class="thumbnail" href="/images/''')
    f.write(subject)
    f.write("/",)
    f.write(number)
    f.write('''.JPG">''')
    f.write('''\n\t\t<img src="/images/''')
    f.write(subject)
    f.write("/")
    f.write(number)
    f.write('''.JPG">
      </a>
    </div>''')
    number = int(number)
    number = number - 1
    number = str(number)
    f.write('''
       <div class="col-md-3">
         <a class="thumbnail" href="/images/''')
    f.write(subject)
    f.write("/", )
    f.write(number)
    f.write('''.JPG">''')
    f.write('''\n\t\t<img src="/images/''')
    f.write(subject)
    f.write("/")
    f.write(number)
    f.write('''.JPG">
         </a>
       </div>''')
    number = int(number)
    number = number - 1
    number = str(number)


    f.write('''
          <div class="col-md-3">
            <a class="thumbnail" href="/images/''')
    f.write(subject)
    f.write("/", )
    f.write(number)
    f.write('''.JPG">''')
    f.write('''\n\t\t<img src="/images/''')
    f.write(subject)
    f.write("/")
    f.write(number)
    f.write('''.JPG">
            </a>
          </div>''')


    number = int(number)
    number = number - 1
    number = str(number)


    f.write('''
              <div class="col-md-3">
                <a class="thumbnail" href="/images/''')
    f.write(subject)
    f.write("/", )
    f.write(number)
    f.write('''.JPG">''')
    f.write('''\n\t\t<img src="/images/''')
    f.write(subject)
    f.write("/")
    f.write(number)
    f.write('''.JPG">
                </a>
              </div>''')

    number = int(number)
    number = number - 1
    number = str(number)


    f.write('''
  </div>
</div> ''')


f.write("\n\n\n\n\n\n\n")
f.write('''<nav class="navbar navbar-default navbar-static-bottom">
  <div class="container-fluid">
    <div class="row">
    <ul id="spacing" class="list-inline navbar-right">
      <li> <a class="btn btn-lg" href="https://twitter.com/KavinJey">
        <i class="fa fa-twitter fa-2x" aria-hidden="true"></i> </a>
      </li>
      <li>
        <a class="btn btn-lg" href="https://github.com/Rurikari">
          <i class="fa fa-github fa-2x" aria-hidden="true"></i> </a>
      </li>
      <li>
        <a class="btn btn-lg" href="projects.html">
          <i class="fa fa-wrench fa-2x" aria-hidden="true"> </i> </a>
      </li>

      <li>
        <a class="btn btn-lg" href="photography.html">
          <i class="fa fa-camera-retro fa-2x" aria-hidden="true"></i> </a>
      </li>
    </ul>
  </div>
  <div class="row">
    <ul  id="spacing-text" class="list-inline navbar-text navbar-right">
      <li> Twitter </li>
      <li> Github </li>
      <li> Projects </li>
      <li> Photography </li>

      <ul>
      </div>
  </div>
</nav>


</div>

<script src="https://use.fontawesome.com/251b350ed8.js"></script>

</body>

</html>''')
f.write("\n\n<!-- PYTHON SCRIPT ENDS HERE --> ")

f.close() 
