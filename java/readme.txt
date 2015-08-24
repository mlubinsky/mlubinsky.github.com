Java utils

mkdir class
javac XMLDriver.java -d class
javac XMLProperties.java -d class
cd class
java XMLProperties
cat user.props

Output
------
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd">
<properties>
<comment>updated</comment>
<entry key="Today">Sun Aug 23 20:59:45 PDT 2015</entry>
<entry key="User">Incognito</entry>
</properties>


java XMLDriver ../test.xml
we got : {title=Snow Crash, author=Neal Stephenson, publisher=Spectra, isbn=0553380958, price=14.95}
we got : {title=Burning Tower, author=Jerry Pournelle, publisher=Pocket, isbn=0743416910, price=5.99}
we got : {title=Zodiac, author=Neal Stephenson, publisher=Spectra, isbn=0553573862, price=7.50}
query =//book[author='Neal Stephenson']/title/text()
Result: Snow Crash
