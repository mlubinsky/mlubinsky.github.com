$(function () {

    var data = {
	      "records": 3,
	      "series": [{
		        "key": "2015-01",
		        "sample_count": 1,
		        "avg_temp": 87.24,
		        "max_temp": 87.24
	      }, {
		        "key": "2015-02",
		        "sample_count": 150,
		        "avg_temp": 82.24,
		        "max_temp": 90.24
	      }, {
		      "key": "2015-03",
		      "sample_count": 300,
		      "avg_temp": 75.24,
		      "max_temp": 80.24
	     }]
    }
    
    var maxTemp = [], avgTemp = [], sampleCount = [], dates = [];
    
    for(var i = 0; i < data.records; i++) {
        dates.push(data.series[i].key)
        maxTemp.push(data.series[i].max_temp);
        avgTemp.push(data.series[i].avg_temp);
        sampleCount.push(data.series[i].sample_count);
    }
    
    $('#container').highcharts({
        title: {
            text: 'Winter 2015',
        },
        xAxis: {
            categories: dates
        },
        yAxis: [{
            title: {
                text: 'Temperature (°C)',
            },
            labels: {
                format: '{value} °C',
            },
        }, {
            opposite: true,
            title: {
                text: 'Sample Count',
                style: {
                    color: Highcharts.getOptions().colors[2]
                }
            },
            labels: {
                style: {
                    color: Highcharts.getOptions().colors[2]
                }
            },
        }],
        series: [{
            name: 'Max Temperature',
            data: maxTemp,
            yAxis: 0,
            zIndex: 3
        }, {
            name: 'Average Temperature',
            data: avgTemp,
            yAxis: 0,
            zIndex: 2
        }, {
            name: 'Sample Count',
            type: 'column',
            data: sampleCount,
            yAxis: 1,
            zIndex: 1
        }]
    });
 
});

