var OverviewChart = function (container, initializedCallback,mode) {
    var control = {
        container: $(container),
        initializedCallback: initializedCallback,
        mode: mode,
        currentPeriod: null,
        startDate: null,
        chart: null,
        periods: [
            { period: "year", format: "%b %Y", momentInterval: "years" },
            { period: "month", format: "%b %Y", momentInterval: "months" },
            { period: "day", format: "%b %Y", momentInterval: "days" }
        ],
        settings: {
            labels: {
                formatter: function () {
                    return Highcharts.dateFormat(this.currentPeriod.format, this.value);
                }
            },
            series: [
                {
                    name: "Usage",
                    cursor: "pointer",
                    point: { events: { click: function () { control.handleBarClick.call(control,this); } } }
                },
                {
                    name: "Supply",
                    cursor: "pointer",
                    point: { events: { click: function () { control.handleBarClick.call(control,this); } } }
                }
            ]
        },

        init: function () {
            if (this.container.length === 0) {
                return;
            }

            $.extend(this.settings, dashboardBarChartDefaults);

            if (this.mode == "gas") {
                $.extend(this.settings, dashboardBarChartGasDefaults);
                this.settings.series.splice(1,1)
            }

            this.currentPeriod = this.periods[0];
            this.startDate = moment().startOf("year");
            this.chart = Highcharts.chart(this.container.find(".js-overview-chart")[0], this.settings);
            this.load();
            this.initBindings();
            this.initializedCallback("overviewChart");
        },

        initBindings: function () {
            this.container.find(".js-overview-chart-prev").click(function () { control.handleNavClick.call(control,"prev") });
            this.container.find(".js-overview-chart-next").click(function () { control.handleNavClick.call(control,"next") });
            this.container.find(".js-overview-chart-zoomout").click(function (e) { control.handleZoomOutClick.call(control, e) });
        },  

        load: function (period, startDate) {
            this.container.find(".js-overview-chart-loader-overlay").removeClass("hidden");
            var url = "/graph-overview-data";

            if (period && startDate) {
                url += "/" + period.period + "/" + startDate;
            }

            $.ajax({
                url: url,
                success: function (graphData) {
                    control.update.call(control, graphData);
                }
            });
        },

        update: function (graphData) {
            var usageData = [];
            var supplyData = []
            var chart = this.chart;

            for (var i = 0; i < graphData["data"].length; i++) {
                if (i > 23 && this.currentPeriod.period == "day") {
                    break;
                }

                var record = graphData["data"][i];

                if (mode == "power") {
                    usageData.push([Date.parse(record.timestamp), parseFloat(record.power_total_usage)]);
                    supplyData.push([Date.parse(record.timestamp), -parseFloat(record.power_total_supply)]);
                } else {
                    usageData.push([Date.parse(record.timestamp), parseFloat(record.gas_total_usage)]);
                }                
            }

            var min = this.startDate.toDate();
            var max = this.startDate.clone().endOf(this.currentPeriod.period).toDate();
            chart.xAxis[0].setExtremes(min, max, true, true);
            chart.xAxis[0].isDirty = true;

            chart.yAxis[0].isDirty = true;
            chart.series[0].setData(usageData, false);

            if (this.mode == "power") {
                chart.series[1].setData(supplyData, false);
            }
            
            chart.redraw();
            this.container.find(".js-overview-chart-loader-overlay").addClass("hidden");
        },

        handleBarClick: function (e) {
            var newPeriod = this.getNewPeriod("next");
            var startDate = Highcharts.dateFormat('%Y-%m-%d', e.x);

            this.currentPeriod = newPeriod;
            this.startDate = moment(startDate, "YYYY-MM-DD")
            this.load(newPeriod, startDate)
        },

        handleZoomOutClick: function () {
            var newPeriod = this.getNewPeriod("prev");

            this.currentPeriod = newPeriod;
            this.startDate.startOf(newPeriod.period);
            this.load(newPeriod, this.startDate.format("YYYY-MM-DD"))
        },

        handleNavClick: function (direction) {
            var period = this.currentPeriod;
            var amount = direction == "prev" ? -1 : 1;
            this.startDate = this.startDate.add(amount, period.momentInterval);
            this.load(period, this.startDate.format("YYYY-MM-DD"));
        },

        getNewPeriod: function (direction) {
            var periods = this.periods;
            var currentPeriod = this.currentPeriod;
            var index = periods.findIndex(p => p.period === currentPeriod.period);

            if (direction == "next") {
                return periods.length <= index + 1
                    ? currentPeriod
                    : periods[index + 1];
            }

            return index == 0
                ? currentPeriod
                : periods[index - 1];
        }
    }

    control.init();

    return control;
};

