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
       
    }
};
