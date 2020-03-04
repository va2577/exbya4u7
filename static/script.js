document.addEventListener('DOMContentLoaded', () => {
  const stockChart = (id = 'container', url = '/static/daily.json', title = undefined, subtitle = undefined) => {
    const get = function (event) {
      console.log(url)
      const chart = this
      fetch(url)
        .then(response => response.json())
        .then(json => chart.series[0].setData(json))
        .then(() => {
          setTimeout(() => get.bind(chart)(), 1000 * 60 * 15);
        })
    }
    return Highcharts.stockChart(id, {
      chart: {
        events: {
          load: get,
        },
      },
      series: [{
        type: 'candlestick',
        // name: 'AAPL Stock Price',
        // data: data,
        data: [],
        id: 'candlestick',
      },
      {
        type: 'sma',
        color: 'rgb(255, 205, 86)',
        lineWidth: 0.4,
        linkedTo: 'candlestick',
        marker: {
          enabled: false,
        },
        params: {
          index: 3,
          period: 20,
        },
        // visible: false,
      },
      {
        type: 'sma',
        color: 'rgb(255, 159, 64)',
        lineWidth: 0.4,
        linkedTo: 'candlestick',
        marker: {
          enabled: false,
        },
        params: {
          index: 3,
          period: 75,
        },
        visible: false,
      }],
      subtitle: {
        // text: 'subtitle',
        text: subtitle,
      },
      title: {
        // text: 'AAPL Stock Price',
        text: title,
      },
    })
  }
  const charts = values.map(v => stockChart(v['container'], v['url'], title=v['title'], subtitle=v['subtitle']))
  // fullscreen
  document.addEventListener('keyup', (event) => {
    event.preventDefault();
    // control + f
    const controlF = event.ctrlKey && (event.keyCode || event.which) === 70
    if (!controlF) {
      return
    }
    const element = document.querySelector('main')
    const requestFullscreen = element.requestFullscreen || element.mozRequestFullScreen || element.webkitRequestFullscreen || element.msRequestFullscreen
    if (!requestFullscreen) {
      return
    }
    requestFullscreen.apply(element)
  })
  // resize
  // tooltip.positioner, yAxis.labels.x
  let timeoutID
  window.addEventListener('resize', () => {
    if (0 < timeoutID) {
      clearTimeout(timeoutID)
    }
    timeoutID = setTimeout(() => {
      charts.forEach(c => {
        c.update({
          tooltip: {
            positioner: () => ({
              x: 40,
              y: c.container.offsetHeight,
            })
          },
          yAxis: {
            labels: {
              x: c.container.offsetWidth * -1 + offset,
            },
          },
        })
      })
    }, 200);
  })
})
