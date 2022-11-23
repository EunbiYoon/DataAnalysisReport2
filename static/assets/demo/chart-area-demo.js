// Global parameters:
// do not resize the chart canvas when its container does (keep at 600x400px)
// Chart.defaults.global.responsive = false;
// define the chart data
var chartData = {
  labels: JSON.parse(jinjaLabels),
  
  datasets: [{
    data: JSON.parse(Ajinja2MValues),
    label: jinja2MLegend,
    backgroundColor: "#50164F63",
    pointHoverRadius: 5,
    pointHoverBackgroundColor: "#164F63",
    pointRadius: 1,
    pointHitRadius: 10
    },
    {
      data: JSON.parse(Ajinja1MValues),
      label: jinja1MLegend,
      backgroundColor: "#50164F63",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "#164F63",
      pointRadius: 1,
      pointHitRadius: 10
    },
    {
      data: JSON.parse(Ajinja0MValues),
      label: jinja0MLegend,
      backgroundColor: "#50164F63",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "#164F63",
      pointRadius: 1,
      pointHitRadius: 10
    }

  ]
};

console.log(jinjaLabels);
console.log(Ajinja2MValues);
console.log(Ajinja1MValues);
console.log(Ajinja0MValues);



// get chart canvas
var ctx = document.getElementById("areachart").getContext("2d");

// create the chart using the chart canvas
var areachart = new Chart(ctx, {
  type: 'line',
  data: chartData,
});
