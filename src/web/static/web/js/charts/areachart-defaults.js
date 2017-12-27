var dashboardAreaChartDefaults =  {
    navigation : {
        buttonOptions : {
            enabled: false
        }
    },
    colors: ["#2677B5","#4DA707","#d9534f"],
    chart: {
        type: 'areaspline'
    },
    title: {
        text: ''
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: true,
        borderWidth: 1,
        backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
    },
    xAxis: {
        title : {
            text: 'Time'
        },
    labels: {
        },
        type: 'datetime',
        dateTimeLabelFormats: {
            second: '%H:%M',
            minute: '%H:%M',
            hour: '%H:%M',
            day: '%e. %b',
            week: '%e. %b',
            month: '%b \'%y',
            year: '%Y'
        }
    },
    yAxis: {
        title: {
            text: 'Kw'
        },
         plotLines: [{
            color: '#a5a5a5', // Color value
            value: 0, // Value of where the line will appear
            width: 2 // Width of the line
          }]
    },
    tooltip: {
        shared: true,
        valueSuffix: ' Kw'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
             marker: {
                 enabled: true
             },
            fillOpacity: 0.5
        }
    },
    series : [
        {
            name: "usage",
            zones: [
                {
                    value: 0,
                    color: '#4DA707'
                },
                {
                    color: '#2677B5'
                }
            ]
        }
   ]
};
