// The base endpoint to receive data from. See update_url()
//var URL_BASE = "http://127.0.0.1:5000/static/graph.html";
var URL_BASE = "http://127.0.0.1:5000/data";
//var URL_BASE = "http://127.0.0.1:5000";

// Update graph in response to inputs
d3.select("#dest").on("input", make_graph);
d3.select("#day_select").on("input", make_graph);
d3.select("#station_select").on("input", make_graph);
d3.select("#day_select").on("input", make_graph);
d3.select("#time").on("input", make_graph);

var margin = {top: 20, right: 20, bottom: 100, left: 60};
var width = 600 - margin.left - margin.right;
var height = 400 - margin.top - margin.bottom;

// Whitespace on either side of the bars in units of minutes
var binMargin = .1;

var x = d3.scale.linear()
    .range([0,  width])
    .domain([0, 25]);
var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom")
    .ticks(6);
var y = d3.scale.linear()
    .range([height, 0]);
var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .ticks(10);

var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
      "translate(" + margin.left + "," + margin.top + ")");

// x axis
svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
    .append("text")
      .text("ETD (minutes)")
      .attr("dy", "3em")
      .attr("text-align", "center")
      .attr("x", width / 2 - margin.right - margin.left);

// y axis
svg.append("g")
    .attr("class", "y axis")
    .call(yAxis)
  .append("text")
    .attr("transform", "rotate(-90)")
    .attr("x", -height / 2)
    .attr("dy", "-2em")
    .text("Count");

// Update the time displayed (XX:XX) next to the time slider
function update_slider(time) {
  var dateObj = new Date();
  dateObj.setHours(Math.floor(time/60));
  dateObj.setMinutes(time % 60);
  d3.select("#prettyTime")
    .text(dateObj.toTimeString().substring(0, 5));
}

// Return url to recieve csv data with query filled in from input fields
function update_url() {
  return URL_BASE +
        "?dest=" + document.getElementById("dest").value +
        "&time=" + document.getElementById("time").value +
        "&station=" + document.getElementById("station_select").value +
        "&day=" + document.getElementById("day_select").value;
}

// Convert csv data to number types
function type(d) {
  d.etd = +d.etd;
  d.count = +d.count;
  return d;
}

function make_graph() {
  update_slider(+document.getElementById("time").value);
  url = update_url()
  console.log(url)   // DEBUG
  d3.csv(url, type, function(error, data) {
    y.domain([0, d3.max(data, function(d) { return d.count; })]);

    svg.selectAll("g.y.axis")
      .call(yAxis);

    var bars = svg.selectAll(".bar")
      .data(data, function(d) { return d.etd; });

    //console.log("y(d.count)="+y(d.count));
    
    bars.transition(1000)
      .attr("y", function(d) { return  y(d.count); } )
      .attr("height", function(d) { return height - y(d.count); } );

    console.log("height="+height);

    bars.enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.etd); })
      .attr("width", x(1 - 2 * binMargin))
      .attr("y", height)
      .attr("height", 0)
      .transition(1000)
        .attr("y", function(d) { return y(d.count); })
        .attr("height", function(d) { return height - y(d.count); });

    bars.exit()
      .transition(1000)
        .attr("y", height)
        .attr("height", 0)
      .remove();
  });
}

make_graph();
