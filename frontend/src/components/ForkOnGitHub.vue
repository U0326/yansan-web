<template>
<span id="forkongithub">
  <a href="https://github.com/U0326/yansan-integration" target="_blank">Fork me on GitHub</a>
</span>
</template>

<style scoped lang="sass">
  #forkongithub a
    background: rgba(102, 176, 232, 0.88)
    color: #fff
    text-decoration: none
    font-family: arial, sans-serif
    text-align: center
    font-weight: bold
    padding: 5px 40px
    font-size: 1rem
    line-height: 2rem
    position: relative
    transition: 0.5s

    &:hover
      background: #c11
      color: #fff

    &::before
      content: ""
      width: 100%
      display: block
      position: absolute
      top: 1px
      left: 0
      height: 1px
      background: #fff

    &::after
      content: ""
      width: 100%
      display: block
      position: absolute
      top: 1px
      left: 0
      height: 1px
      background: #fff
      bottom: 1px
      top: auto

  @media screen and (min-width: 800px)
    #forkongithub
      position: absolute
      display: block
      top: 0
      right: 0
      width: 200px
      overflow: hidden
      height: 200px
      z-index: 9999

      a
        width: 300px
        position: absolute
        top: 54px
        right: -76px
        transform: rotate(45deg)
        -webkit-transform: rotate(45deg)
        -ms-transform: rotate(45deg)
        -moz-transform: rotate(45deg)
        -o-transform: rotate(45deg)
        box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.8)
</style>
