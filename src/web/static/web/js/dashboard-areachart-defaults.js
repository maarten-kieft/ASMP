var dashboardAreaChartDefaults =  {
    navigation : {
        buttonOptions : {
            enabled: false
        }
    },
    colors: ["#4DA707","#2677B5","#d9534f"],
    chart: {
        type: 'areaspline'
    },
    title: {
        text: 'Daily usage'
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
            formatter: function() {
                return Highcharts.dateFormat('%b %Y', this.value);
            }
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
            fillOpacity: 0.5
        }
    }
};
