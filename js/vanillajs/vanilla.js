//<script type="text/javascript">
// Add an event listener of DOMContentLoaded to the whole document and call an anonymous function.
// You can then wrap your code in that function's brackets
// and it will execute once loading is complete.

document.addEventListener('DOMContentLoaded', function () {

    // Our hawaiian greeting is displayed as soon as the page loads,

    console.log('Aloha');
    create_div();
    query();
    addListener();
    //classList();
    //inner();
    //append_remove();
    dom();
 
});

function create_div(){
  console.log("start  create div");
  var div = document.createElement('div') 
  var props = {
       id: 'item',
       textContent: 'hello world',
       onclick: () => console.log('even methods work')
  }
  var style = { 
    backgroundColor: 'blue',
    height: '100px'
  }
  Object.assign(div, props)
  Object.assign(div.style, style)
  console.log("end  create div");
};
// We can use document.querySelector to get the first element that matches a certain criteria.
// It's only argument is a string containing one or more CSS selectors.
function query(){ 
  var lochNess = document.querySelector(".monsters");
  console.log("It's from Scotland - " + lochNess.textContent);

// We can also get all elements of a certain type or class by using document.querySelectorAll.
// This returns a NodeList of all the elements that fit our criteria.

  var scary = document.querySelectorAll(".monsters");
  console.log("Hide and seek champions: ");

  for (var i = 0; i < scary.length; i++) {
    console.log(scary[i].innerHTML);
  }
};



function addListener(){
    var btn = document.querySelectorAll("button"),
        list = document.querySelector("ul");
    console.log(btn); 
// We call the addEventListener method on our desired event target(in this case a button).
// This will start a listener that will wait until a click is generated on the element.

    btn[0].addEventListener("click", function () {

    // When this button is clicked we want to enable zooming of our list.

    // To do this we add an event listener to our list itself,
    // so when the cursor hovers it, the enlarge function gets called.

         list.addEventListener("mouseover", enlarge);
    });

// To disable the zooming we can simply use removeEventListener.

    btn[1].addEventListener("click", function () {

    // Removing event listeners doesn't work on anonymous functions, so always use a named one.

        list.removeEventListener("mouseover", enlarge);
    });
 
// Let's create our enlarge function.

var enlarge = function () {
    // Add class zoomed to the unordered list.
    list.classList.add("zoomed");
    // When the cursor leaves the list return to normal size by removing the class.
    list.addEventListener("mouseout", function () {
        list.classList.remove("zoomed")
    });
};

// Now we want to be able to color the names by clicking them.

// When a 'click' is registered on one of the list entries it should change its color to green.
// Thanks to event delegation we can actually add an event listener to the whole parent object.
// This way we don't have to add separate event listeners to each <li>.

list.addEventListener("click", function (e) {
    // Make the coloring happen only to the clicked element by taking the target of the event.
    e.target.classList.add('red');
});

};

function classList(){ 
    var btn = document.querySelectorAll("button"),
        div = document.querySelector("#myDiv");

     btn[0].addEventListener("click", function () {
    // Get any attribute easily.
        console.log(div.id);
     });

     // Element.classList stores all classes of the element in the form of a DOMTokenList.
     var classes = div.classList;
     btn[1].addEventListener("click", function () {
          console.log(classes);
     });

     btn[2].addEventListener("click", function () {
    // It supports adding and removing classes.
        classes.add("red");
     });

     btn[3].addEventListener("click", function () {
    // You can also toggle a class on and off
        classes.toggle("hidden");
     });
};

function inner(){  
    var myText = document.querySelector("#myParagraph"),
         btn = document.querySelectorAll("button");

// We can easily get the text content of a node and all its descendants.

    var myContent = myText.textContent;

    console.log("textContent:  " + myContent);

// When using textContent to alter the text of an element
// it deletes the old content and replaces it with new.

    btn[0].addEventListener('click', function () {    
        myText.textContent = " Koalas are the best animals ";
    });

// If we want to grab all the HTML in a node (including the tags) we can use innerHTML.

    var myHtml = myText.innerHTML;
    console.log("innerHTML:  " + myHtml);

// To change the html simply supply new content.
// Of course we aren't limited to text only this time.

    btn[1].addEventListener('click', function () {
          myText.innerHTML = "<button> Penguins are the best animals </button>";
    
    });
}


function append_remove(){ 
   var lunch = document.querySelector("#lunch");
   // In the HTML tab we have our lunch for today.
   // Let's say we want to add fries to it.

    var addFries = function () {

    // First we have to create our new element and set its content
       var fries = document.createElement("div");
       fries.innerHTML = '<li><h4> Fries </h4></li>';

    // After that's done, we can use appendChild to insert it.
    // This will make our fries appear at the end of the lunch list.
       lunch.appendChild(fries);

    };

// Now we want to add cheese both before and after the beef in our burger.

var addCheese = function () {

    var beef = document.querySelector("#Beef"),

            topSlice = document.createElement("li"),
            bottomSlice = document.createElement("li");

    bottomSlice.innerHTML = topSlice.innerHTML = 'Cheese';

    // Inserting the top slice:
    // Take the parent of the beef (that's the sandwich) and use insertBefore on it.
    // The first argument to insertBefore is the new element we're gonna add.
    // The second argument is the node before which the new element is inserted.

    beef.parentNode.insertBefore(topSlice, beef);

    // The bottom slice:
    // We have to use a little trick here!
    // Supply the next nearest element as the second argument to insertBefore,
    // that way we can actually insert after the element we want.

    beef.parentNode.insertBefore(bottomSlice, beef.nextSibling);

};

var removePickles = function () {
    // Finally, we want to get rid of those pickles. Again javascript got us covered!
    var pickles = document.querySelector("#pickles");
    if (pickles) {
        pickles.parentNode.removeChild(pickles);
    }
};

// Delicious!

var btn = document.querySelectorAll("button");
btn[0].addEventListener('click', addFries);
btn[1].addEventListener('click', addCheese);
btn[2].addEventListener('click', removePickles);

};

function dom() {

var snakes = document.querySelector('#snakes'),
    birds = document.querySelector('#birds');

snakes.addEventListener('click', function (e) {

    // To access the parent of a certain element in the DOM tree, we use the parentNode method.

    var parent = e.target.parentNode;

    console.log("Parent: " + parent.id);


    // For the opposite, calling the .children method gets all child elements of the selected object.

    console.log("Children: ");
    var children = e.target.children;

    // This returns a HTMLCollection (a type of array), so we have to iterate to access every child's content.

    for (var i = 0; i < children.length; i++) {

        console.log(children[i].textContent);

    }
});


birds.addEventListener('click', function (e) {

    // Getting the nearest sibling to our element is self-explanatory.

    var previous = e.target.previousElementSibling;

    if (previous) {
        console.log("Previous sibling: " + previous.textContent);

    }

    var next = e.target.nextElementSibling;

    if (next) {
        console.log("Next sibling: " + next.textContent);

    }

    // However, to acquire all the siblings of a node is a bit more complex.
    // We have to take all of its parent's children and then exclude the original element.
    // This is done by using filter and calling a function that checks every child one by one.

    console.log("All siblings: ");

    Array.prototype.filter.call(e.target.parentNode.children, function (child) {
        if (child !== e.target) {
            console.log(child.textContent);
        }
    });

});

};
/*
var div = document.createElement('div') 
var props = {
  id: 'item',
  textContent: 'hello world',
  onclick: () => console.log('even methods work')
}
var style = { 
  backgroundColor: 'red',
  height: '100px'
}
Object.assign(div, props)
Object.assign(div.style, style)
*/
//</script>