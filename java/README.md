 
 
 An executable JAR is a just regular archive, with an included META-INF/manifest file 
 that says which "main" class should be the entry point. 
 The JRE knows to look for this manifest file.
 
 Run with the parameter:
 
 java.exe -jar  name.jar
 
 ## Promises vs Observables
 Both Promises and Observables will help us work with the asynchronous functionalities in JavaScript.

The main differences between them are listed below:
```
Promise:
Promises are values that will resolve in asynchronous ways like http calls
They have one pipeline
They are usually only use with async data return
They are not easy to cancel

Observable:

Observables deal with a sequence of asynchronous events
They are cancellable
They are retriable by nature such as retry and retryWhen
They stream data in multiple pipelines
They have array-like operations like map, filter etc.
They can be created from other sources like events
They are functions, which could be subscribed later on
```
