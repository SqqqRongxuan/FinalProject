$(function () {

	var options = {
		series: [{
			name: 'New Visitors',
			data: [94, 55, 57, 56, 61, 58, 63, 60, 66, 75]
		}, {
			name: 'Returning Visitors',
			data: [-76, -85, -101, -98, -87, -105, -91, -114, -94, -105]
		}],
		chart: {
			foreColor: 'rgba(255, 255, 255, 0.65)',
			type: 'bar',
			height: 350,
			stacked: true,
			toolbar: {
				show: false
			},
		},
		plotOptions: {
			bar: {
				horizontal: false,
				columnWidth: '12%',
				endingShape: 'rounded'
			},
		},
		legend: {
			position: 'top',
			horizontalAlign: 'left',
			offsetX: -20
		},
		dataLabels: {
			enabled: false
		},
		stroke: {
			show: true,
			width: 2,
			colors: ['transparent']
		},
		colors: ["#fff", "rgba(255, 255, 255, 0.35)"],
		xaxis: {
			categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
		},
		fill: {
			opacity: 1
		},
		grid: {
			show: true,
			borderColor: 'rgba(255, 255, 255, 0.12)',
			strokeDashArray: 4,
		},
		tooltip: {
			theme: 'dark',
		},
		responsive: [{
			breakpoint: 480,
			options: {
				chart: {
					height: 310,
				},
				plotOptions: {
					bar: {
						columnWidth: '30%'
					}
				}
			}
		}]
	};
	var chart = new ApexCharts(document.querySelector("#chart4"), options);
	chart.render();
	// chart 5
	var options = {
		series: [25, 65, 10],
		chart: {
			height: 240,
			type: 'donut',
		},
		legend: {
			position: 'bottom',
			show: false,
		},
		plotOptions: {
			pie: {
				// customScale: 0.8,
				donut: {
					size: '80%'
				}
			}
		},
		colors: ["rgba(255, 255, 255, 0.52)", "#fff", "rgba(255, 255, 255, 0.22)"],
		dataLabels: {
			enabled: false
		},
		tooltip: {
			enabled: false,
			theme: 'dark',
		},
		stroke:{
         colors:['rgba(255, 255, 255, 0.0)']
        },
		labels: ['Mobile', 'Desktop', 'Tablet'],
		responsive: [{
			breakpoint: 480,
			options: {
				chart: {
					height: 200
				},
				legend: {
					position: 'bottom'
				}
			}
		}]
	};
	var chart = new ApexCharts(document.querySelector("#chart5"), options);
	chart.render();
	// chart 5
	var options = {
		series: [25, 65, 10],
		chart: {
			foreColor: 'rgba(255, 255, 255, 0.65)',
			height: 360,
			type: 'pie',
		},
		legend: {
			position: 'bottom',
			show: true,
		},
		plotOptions: {
			pie: {
				customScale: 0.9,
				donut: {
					size: '80%'
				}
			}
		},
		colors: ["rgba(255, 255, 255, 0.52)", "#fff", "rgba(255, 255, 255, 0.22)"],
		dataLabels: {
			enabled: true
		},
		tooltip: {
			enabled: false,
			theme: 'dark',
		},
		labels: ['Male', 'Female', 'Others'],
		stroke:{
         colors:['rgba(255, 255, 255, 0.0)']
        },
		responsive: [{
			breakpoint: 480,
			options: {
				chart: {
					height: 360
				},
				legend: {
					position: 'bottom'
				}
			}
		}]
	};
	var chart = new ApexCharts(document.querySelector("#chart6"), options);
	chart.render();
	jQuery('#geographic-map').vectorMap({
		map: 'world_mill_en',
		backgroundColor: 'transparent',
		borderColor: '#818181',
		borderOpacity: 0.25,
		borderWidth: 1,
		zoomOnScroll: false,
		color: '#009efb',
		regionStyle: {
			initial: {
				fill: '#fff'
			}
		},
		markerStyle: {
			initial: {
				r: 9,
				'fill': '#fff',
				'fill-opacity': 1,
				'stroke': '#000',
				'stroke-width': 5,
				'stroke-opacity': 0.4
			},
		},
		enableZoom: true,
		hoverColor: '#009efb',
		markers: [{
			latLng: [21.00, 78.00],
			name: 'I Love My India'
		}],
		hoverOpacity: null,
		normalizeFunction: 'linear',
		scaleColors: ['#b6d6ff', '#005ace'],
		selectedColor: '#c9dfaf',
		selectedRegions: [],
		showTooltip: true,
		onRegionClick: function (element, code, region) {
			var message = 'You clicked "' + region + '" which has the code: ' + code.toUpperCase();
			alert(message);
		}
	});
});