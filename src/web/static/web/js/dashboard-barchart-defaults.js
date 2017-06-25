var dashboardBarChartDefaults =  {
    navigation : {
        buttonOptions : {
            enabled: false
        }
    },
    colors: ["#2677B5","#4DA707","#d9534f"],
    chart: {
        type: 'bar'
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
            text: 'KwH'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' KwH'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
             marker: {
                 enabled: true
             },
             connectEnds: false,
            fillOpacity: 0.5,
            pointInterval: 10,
            pointIntervalUnit: "second"
        }
    }
};
