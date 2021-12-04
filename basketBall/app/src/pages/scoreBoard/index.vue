<template>
  <view class="board">
    <iframe src="http://app.top1.pub/scoreboard#/" />
  </view>
</template>

<script>
export default {
  name: "scoreBoard",
  components: {},
  setup() {},
};
</script>

<style lang="scss">
iframe {
  width: 100%;
  height: 100vh;
  border: none;
}
.board {
  width: 100%;
  height: 100vh;
}
</style>
