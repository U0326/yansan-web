<template>
<div>
  <div id="header">
    <h1>ヤンサンNavi</h1>
    <h2>
        漫画家、山田玲司先生の番組である
        <a href="https://www.youtube.com/channel/UC09D3M_DdLaZMJnZp0v4pLQ">山田玲司のヤングサンデー</a>
        における、<br>膨大な数の動画を整理し、あなたのヤンサンライフを支援します。
    </h2>
  </div>
  <div id="main">
    <div id="side-menu">
      <side-menu />
    </div>
    <div id="content">
        <router-view/>
    </div>
  </div>
</div>
</template>

<script>
import SideMenu from './components/SideMenu.vue'

export default {
  components: {
    SideMenu
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
