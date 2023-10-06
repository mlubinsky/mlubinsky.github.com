### Debug print in PHP

echo nl2br("\n command=" . $command ) ;

echo json_encode($_REQUEST); for hash arrays

### Pandas
```
error_types_interests = ['_position2DError', '_xTrackError', '_alongTrackError', 'SOG_Error', '_headingError', 'dist_error']

df1_lsi_tmp = df1_LSI.loc[df1_LSI['Error_Type'].isin(error_types_interests)].groupby(['Chipset','Model','Signal_Bands','Error_Type']).agg('mean')
```


### Javascript HTTP POST  - PHP

```
var str = JSON.stringify(obj, null, 2);
consol.log(str)
```
https://stackoverflow.com/questions/45426158/send-data-from-html-form-to-php

 https://www.w3schools.com/php/php_forms.asp

### Redirect output to file

Take care to add 2>&1 at the end of the instruction because on Windows, the order of redirection is important as command 2>&1 > logfile will produce an empty file

#### To combine ERR and STDOUT
``` 
command > logfile 2>&1 
```
##### To separate ERR and STDOUT
```
dir test.exe > output.txt 2> err.txt
```

#### Redirect to NULL
```
dir test.exe 1> myoutput.txt 2>nul
```
### File Compare Utils
Compare It!
https://www.grigsoft.com/wincmp3.htm


### Inertial Measurement Unit - IMU

INS (inersial  navigational systems) -  инерциальные навигационные системы (ИНС)

 Блок инерциальных измерений (БИИ, или от англ. IMU — Inertial Measurement Unit) состоит из гироскопов и акселерометров позволяющих отслеживать вращательные и поступательные движения.
 
https://habr.com/ru/companies/whoosh/articles/765628/


https://habr.com/ru/articles/255661/ Фильтр Маджвика


### Install Apache on Windows

LoadModule libpq_module /usr/lib/apache/1.3/mod_libpq.so  http.conf

https://www.sitepoint.com/how-to-install-apache-on-windows/

Microsoft have new version of vc_redist for apps developed with Microsoft Visual Studio 2022.
Version: 14.30.30704

x64 - https://aka.ms/vs/17/release/VC_redist.x64.exe

Download Apache (x64)  https://www.apachelounge.com/

Open an “Administrator” command prompt
```
mkdir c:/Apache24
cd  c:/Apache24/bin
httpd.exe -t
httpd.exe
 http://localhost
 
Install Apache Service
 httpd.exe -k install -n "Apache HTTP Server"

Edit conf/httpd.conf 
Line 60, listen to all requests on port 80:
Listen *:80
Line 162, enable mod-rewrite by removing the # (optional, but useful):

LoadModule rewrite_module modules/mod_rewrite.so
Line 227, specify the server domain name:

ServerName localhost:80
Line 224, allow .htaccess overrides:

AllowOverride All
```
### WAMPSERVER

https://www.wampserver.com/en/

https://stackoverflow.com/questions/32922816/install-two-instance-of-wampserver-on-same-pc

https://superuser.com/questions/994013/run-two-wamp-servers-installed-in-different-drives-simultaneously

### GNSS, RINEX,  NMEA  (National Marine Electronics Association)

https://docs.novatel.com/OEM7/Content/Logs/GPRMC.htm
```
field 10 is the date: Date: dd/mm/yy xxxxxx 210307
Fixes can come from 3 possible message types.  For each fix UTC, we will choose exactly one of GPGGA, GPRMC, and GNRMC, in that priority order.
```
The date field is in GPRMC and GNRMC, but not the GPGGA sentence

https://www.sparkfun.com/datasheets/GPS/NMEA%20Reference%20Manual-Rev2.1-Dec07.pdf NMEA

https://home.csis.u-tokyo.ac.jp/~dinesh/Dinesh_T_files/GNSS_10_Introduction_DataFormats.pdf

https://en.wikipedia.org/wiki/NMEA_0183

https://www.gpsworld.com/what-exactly-is-gps-nmea-data/

https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/GNSS_data_holdings.html

https://gage.upc.edu/en/learning-materials/library/gnss-format-descriptions

https://psmsl.org/data/gnssir/fileinfo.php

https://frontierprecision.com/the-power-of-gnss-metadata/

Receiver Independent Exchange format (RINEX)

https://gssc.esa.int/navipedia/index.php/Interfaces_and_Protocols RINEX

## KML format

https://developers.google.com/kml/documentation/kmlreference#polygon

https://sites.google.com/site/kmltouring/google-earth-tools/polygons

https://sites.google.com/site/kmltouring/editing-kml

https://sites.google.com/site/kmltouring/google-earth-tools/placemarks-pins

https://renenyffenegger.ch/notes/tools/Google-Earth/kml/index

https://developers.google.com/kml/documentation/kml_tut

### Web
 ```
<!DOCTYPE html>
<html>
<head>
  <title>Vertical Radio Buttons with Conditional Text Input</title>
  <script>
    function handleRadioChange() {
      var option1Radio = document.getElementById("option1");
      var option2Radio = document.getElementById("option2");
      var textInput1 = document.getElementById("text-input1");
      var textInput2 = document.getElementById("text-input2");

      if (option1Radio.checked) {
        textInput1.style.display = "block";
        textInput2.style.display = "none";
      } else if (option2Radio.checked) {
        textInput1.style.display = "none";
        textInput2.style.display = "block";
      } else {
        textInput1.style.display = "none";
        textInput2.style.display = "none";
      }
    }
  </script>
  <style>
    .text-input {
      display: none;
    }
  </style>
</head>
<body>
  <h2>Choose an Option:</h2>
  <label for="option1">
    <input type="radio" id="option1" name="options" value="option1" onchange="handleRadioChange()"> Option 1
  </label>
  <br>
  <label for="option2">
    <input type="radio" id="option2" name="options" value="option2" onchange="handleRadioChange()"> Option 2
  </label>
  <br>
  <label for="text-input1">Text Input 1:</label>
  <input type="text" id="text-input1" name="text-input1" class="text-input">
  <br>
  <label for="text-input2">Text Input 2:</label>
  <input type="text" id="text-input2" name="text-input2" class="text-input">
</body>
</html>



```


Same as above but with Angular 1

```
<!DOCTYPE html>
<html ng-app="myApp">
<head>
  <title>Vertical Radio Buttons with Conditional Text Input (AngularJS)</title>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.7.9/angular.min.js"></script>
  <style>
    .text-input {
      display: none;
    }
  </style>
</head>
<body ng-controller="myController">
  <h2>Choose an Option:</h2>
  <label for="option1">
    <input type="radio" id="option1" name="options" value="option1" ng-model="selectedOption" ng-change="handleRadioChange()"> Option 1
  </label>
  <br>
  <label for="option2">
    <input type="radio" id="option2" name="options" value="option2" ng-model="selectedOption" ng-change="handleRadioChange()"> Option 2
  </label>
  <br>
  <label for="text-input1">Text Input 1:</label>
  <input type="text" id="text-input1" name="text-input1" class="text-input" ng-show="selectedOption === 'option1'">
  <br>
  <label for="text-input2">Text Input 2:</label>
  <input type="text" id="text-input2" name="text-input2" class="text-input" ng-show="selectedOption === 'option2'">

  <script>
    angular.module('myApp', [])
      .controller('myController', function($scope) {
        $scope.handleRadioChange = function() {
          var option1 = 'option1';
          var option2 = 'option2';

          var textInput1 = document.getElementById("text-input1");
          var textInput2 = document.getElementById("text-input2");

          if ($scope.selectedOption === option1) {
            textInput1.style.display = "block";
            textInput2.style.display = "none";
          } else if ($scope.selectedOption === option2) {
            textInput1.style.display = "none";
            textInput2.style.display = "block";
          } else {
            textInput1.style.display = "none";
            textInput2.style.display = "none";
          }
        };
      });
  </script>
</body>
</html>
```
Explanation:
```
In this example, we start by including the AngularJS library using a script tag.
The ng-app directive is added to the html element to initialize the AngularJS application.

We define an AngularJS module called "myApp" and create a controller called "myController" using the controller method.
 The controller function is then attached to the ng-controller directive in the body tag.

Inside the controller function, we define the handleRadioChange function, which will be triggered whenever a radio button is selected or deselected.
You can implement the necessary logic within this function to handle the visibility of the text input elements based on the selected radio button.

In the HTML code, the ng-model directive is used to bind the selected radio button value to the $scope.selectedOption variable.
The ng-change directive is used to call the handleRadioChange function whenever the selected option changes.

The ng-show directive is applied to each text input element to conditionally show or hide them based on the value of $scope.selectedOption.
 If the selected option matches the desired option for each text input, the respective input will be displayed.

Note: AngularJS is an older version of the Angular framework and is no longer actively developed or recommended for new projects.
 It's recommended to use the latest version of Angular (Angular 2+) for new projects.
````
