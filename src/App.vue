<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import Chart from './components/Chart.vue'
</script>

<template>
  <header>
  <h1>Bierbörse</h1>
    
  </header>

  <main>
    <Chart chartname="Testytest"/>
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
  place-items: left;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  main {
    place-items: center;
  }
}
</style>
