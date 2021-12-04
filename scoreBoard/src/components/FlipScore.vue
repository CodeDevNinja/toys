/*
 * 计分牌
 * @author： caidong
 * @createDate: 2021-11-21
 */
<template>
  <div class='main'>
    <fullscreen :fullscreen.sync="fullscreen" class='FlipClock'>
        <div>
        <v-touch style=""
                @swipeup='swiperup("left")'
                @swipedown='swiperdown("left")'
                @swipeleft='swiperleft'
                @swiperight='swiperright'>
            <Flipper ref='num1' class="num1" v-show='hundredsFlag === true'/>
            <Flipper ref="num2" class="num2" v-show='tenFlag === true'/>
            <Flipper ref="num3" class='num3' />
        </v-touch>
        <el-input
              style="border:0"
              placeholder="A队"
              v-model="teamNameA"></el-input>
        </div>
        <em>:</em>
        <div>
        <v-touch
                @swipeup='swiperup("right")'
                @swipedown='swiperdown("right")'
                @swipeleft='swiperleft'
                @swiperight='swiperright'>
            <Flipper ref='num4' class='num1' v-show='hundredsFlag === true'/>
            <Flipper ref='num5' class='num2' v-show='tenFlag === true'/>
            <Flipper ref="num6" class='num3' />
        </v-touch>
           <el-input
              placeholder="B队"
            v-model="teamNameB"></el-input>
        </div>
    </fullscreen>
    <el-button  class="fullBtn" @click="toggle" icon="el-icon-full-screen"></el-button>
  </div>
</template>

<script>
import Flipper from './Flipper'
  import fullscreen from 'vue-fullscreen'
import Vue from 'vue'
  Vue.use(fullscreen)
export default {
  name: 'FlipScore',
  data() {
    return {
      teamNameA: '',
      teamNameB: '',
      hundredsFlag: false,
      tenFlag: false,
      noNum: 2,
      width: '40vw',
      fontSize: '60vw',
      left: 0,
      right: 0,
      timer: null,
      flipObjs: [],
      fullscreen: false
    }
  },
  components: {
    Flipper
  },
  methods: {
            changeScore(side, op) {
                    var leftOnes = parseInt(this.flipObjs[2].frontTextFromData)
                    var leftTens = parseInt(this.flipObjs[1].frontTextFromData)
                    var leftHundreds = parseInt(this.flipObjs[0].frontTextFromData)
                    var leftTotalScore = leftOnes + leftTens * 10 + leftHundreds * 100
                    var rightOnes = parseInt(this.flipObjs[5].frontTextFromData)
                    var rightTens = parseInt(this.flipObjs[4].frontTextFromData)
                    var rightHundreds = parseInt(this.flipObjs[3].frontTextFromData)
                    var rightTotalScore = rightOnes + rightTens * 10 + rightHundreds * 100
                    var maxScore = leftTotalScore > rightTotalScore ? leftTotalScore : rightTotalScore
                    console.log(leftTotalScore, rightTotalScore, maxScore)
                    var TotalScore
                    var pos = (side === 'left') ? 0 : 3
                    if (side === 'left') {
                        TotalScore = leftTotalScore
                    } else {
                        TotalScore = rightTotalScore
                    }
                    console.log(side, op)
                    let myFunc = num => Number(num);
                    var originArr = Array.from(String(TotalScore), myFunc);
                    if (TotalScore <= 9) {
                        originArr = [0, 0].concat(originArr)
                    } else if (TotalScore > 9 & TotalScore <= 99) {
                        originArr = [0].concat(originArr)
                      }
                    if (op === 'up') {
                          TotalScore += 1
                      } else {
                          if (TotalScore <= 0) {
                            return
                          }
                          TotalScore -= 1
                      }
                      var nowArr = Array.from(String(TotalScore), myFunc);
                      if (TotalScore <= 9) {
                        nowArr = [0, 0].concat(nowArr)
                      } else if (TotalScore > 9 & TotalScore <= 99) {
                        nowArr = [0].concat(nowArr)
                      }
                    console.log(originArr, nowArr)
                    for (let i = 0; i < nowArr.length; i++) {
                        if (originArr[i] === nowArr[i]) {
                              continue
                        }
                        if (op === 'up') {
                          this.flipObjs[pos + i].flipUp(originArr[i], nowArr[i])
                        } else {
                          this.flipObjs[pos + i].flipDown(originArr[i], nowArr[i])
                        }
                    }
                    if (maxScore >= 9 & maxScore < 99) {
                        this.width = '20vw'
                        this.fontSize = '35vw'
                        this.tenFlag = true
                        this.hundredsFlag = false
                    } else if (maxScore >= 99) {
                         this.width = '13vw'
                         this.fontSize = '25vw'
                         this.tenFlag = true
                         this.hundredsFlag = true
                    } else if (maxScore < 9) {
                          this.width = '40vw'
                          this.fontSize = '52vw'
                          this.hundredsFlag = false
                          this.tenFlag = false
                    }
                    console.log(this.width)
                    for (let i = 0; i < this.flipObjs.length; i++) {
                        this.flipObjs[i].setStyle(this.width, this.fontSize);
                    }
            },
            toggle () {
                this.fullscreen = !this.fullscreen
            },
            swiperup: function (pos) {
                    this.changeScore(pos, 'up')
                },
            swiperdown: function (pos) {
                this.changeScore(pos, 'down')
            },
            swiperleft: function () {
             console.log('左滑')
            //  alert('左滑')
            },
            swiperright: function () {
             console.log('右滑')
            //  alert('右滑')
            },
    // 初始化数字
    init() {
              for (let i = 0; i < this.flipObjs.length; i++) {
                        this.flipObjs[i].setFront('0')
              }
    }
  },
  mounted () {
    this.flipObjs = [
      this.$refs.num1,
      this.$refs.num2,
      this.$refs.num3,
      this.$refs.num4,
      this.$refs.num5,
      this.$refs.num6
    ]
    this.init()
    }
}
</script>

<style>
.el-input__inner {
  border: 0;
  text-align: center;
  font-weight: bolder;
  width: 100%;
  border: none;
  border-bottom: 3px solid #b5b5b5;
  border-radius: none;
}
.main{
    background-color:#fff
}
.fullBtn{
    float: right;
    z-index: 2;
    margin-right: 10px;
    border: 0px solid
}
.FlipClock {
    text-align: center;
    display:flex;
    align-items: center;
    justify-content: center;
    /* font-size:100px; */
    background-color:#fff
}
.FlipClock .M-Flipper {
    margin: 0 3px;
}
.FlipClock em {
    display: inline-block;
    line-height: 102px;
    font-size: 20vw;
    font-style: normal;
    vertical-align: top;
}
el-input {
    text-align: right;
}
</style>
