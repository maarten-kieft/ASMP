var dashboardBarChartDefaults =  {
    navigation : {
        buttonOptions : {
            enabled: false
        }
    },
    colors: ["#2677B5","#4DA707","#d9534f"],
    chart: {
        type: 'column'
    },
    title: {
        text: ''
    },
    xAxis: {
        title : {
            text: 'Time'
        },
        labels: {},
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
        },
        plotLines: [{
            color: '#a5a5a5',
            value: 0,
            width: 1,
            zIndex: 5
          }
        ]
    },
    tooltip: {
        shared: true,
        valueSuffix: ' KwH'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        series: {
            stacking: 'normal'
        }
    }
};
