<template>
<div id="root">
  <fork-on-git-hub />
  <div class="container" id="contents-all">
    <header>
      <div class="hero">
        <div class="hero-body" id="header">
          <a href="/"><img src="./assets/logo.png"/></a>
          <h2>
              漫画家、山田玲司先生の番組「
              <a href="https://www.youtube.com/channel/UC09D3M_DdLaZMJnZp0v4pLQ" target="_blank">山田玲司のヤングサンデー</a>
              」の動画を整理し、あなたのヤンサンライフを支援します。
          </h2>
        </div>
      </div>
    </header>
    <main class="columns">
      <div class="submenu column is-3" id="side-menu">
        <side-menu />
      </div>
      <div class="column" id="content">
          <router-view/>
      </div>
    </main>
    <footer>
      <div class="content has-text-centered">
         powered by Garaku Project
      </div>
    </footer>
  </div>
</div>
</template>

<script>
import ForkOnGitHub from './components/ForkOnGitHub.vue'
import SideMenu from './components/SideMenu.vue'

export default {
  components: {
    ForkOnGitHub,
    SideMenu
  }
}
</script>

<style scoped lang="sass">
  #root
    background-image: url("./assets/background.png")

  #contents-all
    max-width: 1200px
    margin: auto
    padding: 20px
    padding-top: 0px
    background-color: rgba(255,255,255,0.6)

  .hero-body
    padding-left: 5px

  footer
    margin-top: 40px

</style>
