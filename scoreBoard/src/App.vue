<template>
  <div id='app'>
    <!-- <FlipClock></FlipClock> -->
    <FlipScore></FlipScore>
  </div>
</template>

<script>
import FlipScore from './components/FlipScore.vue'
// import FlipClock from './components/FlipClock.vue'

export default {
  name: 'app',
  components: {
    // FlipClock,
    FlipScore
  }
}
</script>
