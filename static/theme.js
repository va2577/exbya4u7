const offset = 40
const tooltipX = offset
const tooltipY = document.querySelector('#container').offsetHeight
const yAxisLabelsX = document.querySelector('#container').offsetWidth * -1 + offset
Highcharts.theme = {
  chart: {
    backgroundColor: "rgb(1, 15, 41)", // "#000000",
    // borderColor: "#ffffff",
    // borderWidth: 1,
    marginBottom: 24,
    marginLeft: 2,
    marginRight: 2,
    marginTop: 0,
    style: {
      fontFamily: '"American Typewriter", \'Unica One\', sans-serif',
    },
  },
  credits: {
    enabled: false,
  },
  plotOptions: {
    candlestick: {
      color: 'rgba(255, 69, 58, 0.4)', // '#FF6384', // '#845dde', // '#e85f82', // '#aa0000',
      dataGrouping: {
        enabled: false,
      },
      lineColor: 'rgba(255, 69, 58, 0.8)', // '#FF83A4', // '#946dee', // '#f86f92', // '#ff4444',
      lineWidth: 0.4,
      upColor: 'rgba(10, 132, 255, 0.4)', // '#36A2EB', // '#1893fb', // '#0000aa',
      upLineColor: 'rgba(10, 132, 255, 0.8)', // '#56C2EB', // '#28a3ff', // '#4444ff',
    },
  },
  navigator: {
    enabled: false,
  },
  rangeSelector: {
    selected: 5,
    enabled: false,
  },
  scrollbar: {
    enabled: false,
  },
  subtitle: {
    // align: "right",
  },
  time: {
    timezoneOffset: (new Date()).getTimezoneOffset() / 60,
    useUTC: false,
  },
  title: {
    // align: "right",
    style: {
      color: '#333333', // #333333
    },
  },
  tooltip: {
    backgroundColor: 'rgba(0, 0, 0, 0)',
    borderWidth: 0,
    formatter: function () {
      const point = this.points[0].point
      const props = ['open', 'high', 'low', 'close']
      const ohlc = props.map(x => `${x}: ${point[x] < 10 ? point[x].toFixed(5): point[x].toFixed(3)}`)
      return `datetime: ${Highcharts.dateFormat(undefined, this.x)} ${ohlc.join(' ')}`
    },
    positioner: () => ({
      x: tooltipX,
      y: tooltipY,
    }),
    shadow: false,
    style: {
      // color: '#666666', // #333333
    },
  },
  xAxis: {
    crosshair: {
      width: 0,
    },
    // gridLineWidth: 0.1,
    labels: {
      style: {
        // color: '#666666', // #666666
      },
    },
    lineWidth: 0,
    tickLength: 0,
  },
  yAxis: {
    endOnTick: false,
    gridLineWidth: 0,
    labels: {
      x: yAxisLabelsX,
      style: {
        // color: '#666666', // #666666
      },
    },
  },
}
Highcharts.setOptions(Highcharts.theme)
