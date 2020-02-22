<template>
  <b-collapse :open.sync="isOpen" aria-id="toggle-tag" class="box menu" id="tags">
    <div slot="trigger" slot-scope="props" aria-controls="toggle-tag">
      タグ一覧<a><b-icon size="is-small" :icon="props.open ? 'menu-down' : 'menu-up'" /></a>
    </div>
    <div class="tags">
      <span class="tag" v-for="tag in tags" v-bind:key=tag._id>
        <router-link @click.native="handleTagClick" :to="{path: '/tag', query: {name: tag._id}}">
          {{tag._id + '(' + tag.frequency + ')'}}
        </router-link>
      </span>
    </div>
  </b-collapse>
</template>

<script>
import isMobile from 'ismobilejs'
import httpClient from '@/common/ajax.js'

export default {
  data: () => {
    return {
      tags: null,
      // スマホの場合には、タグで画面が埋まってしまう為、基本的に閉じておく。
      isOpen: !isMobile(window.navigator.userAgent).phone
    }
  },
  watch: {
    tags: function (newValue) {
      if (!newValue.tags) {
        return
      }
      this.tags = newValue.tags.sort((a, b) => a.frequency < b.frequency ? 1 : -1)
    }
  },
  mounted: function () {
    httpClient.get('/api/tags').then(response => { this.tags = response.data })
  },
  methods: {
    handleTagClick: function () {
      if (!isMobile(window.navigator.userAgent).phone) {
        return
      }
      this.isOpen = false
    }
  }
}
</script>

<style scoped lang="sass">
  #tags
    padding-top: 5px
</style>
