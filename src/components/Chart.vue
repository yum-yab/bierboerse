<script setup>

defineProps({
  chartname: {
    type: String,
    required: true
  }
})

</script>

<script>

import { Line } from 'vue-chartjs'

import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale,
  Filler
} from "chart.js";
ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale,
  Filler
);  

export default {
  name: "chart",
  components: { Line },
  props: {
    chartId: {
      type: String,
      default: 'bar-chart'
    },
    // scales: {
    //       //hides the y axis
    //       y: {
    //         grid: {
    //           color: "#383838",
    //           borderColor: '#2D2D2D',
    //         },
    //       },
    //       x: {
    //         grid: {
    //           display: false,
    //           borderColor: '#383838',
    //         },
    //       },
    //     },
    datasetIdKey: {
      type: String,
      default: 'label'
    },
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object,
      default: () => {
        return {
          width: "1200px",
          height: "900px",
        }
      }
    },
    plugins: {
      type: Object,
      default: () => {}
    }
  },
  data() {
    return {
      chartData: {
        label: "LULUL",
        labels: [ 1, 2, 3, 4, 5 ],
        datasets: [ { data: [1.5, 1.4, 1.3, 1.6, 1.7] } ],
        borderColor: "#cc222d",
      },
      chartOptions: {
        responsive: true
      }
    }
  }
}

</script>


<template>
<div class="bigchart">

    <Line
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :dataset-id-key="datasetIdKey"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
    :width="width"
    :height="height"
    class="bigchart"
    />

  </div>

  
</template>

<style scoped>

.bigchart {
  height: "100%";
  width: "100%"
}


</style>