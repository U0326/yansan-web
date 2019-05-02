<template>
  <aside class="box menu">
    <p class="menu-label">タグ一覧</p>
    <div class="tags">
      <span class="tag" v-for="tag in tags" v-bind:key=tag._id>
        <router-link :to="{path: '/tag', query: {name: tag._id}}">
          {{tag._id + '(' + tag.frequency + ')'}}
        </router-link>
      </span>
    </div>
  </aside>
</template>

<script>
import httpClient from '@/common/ajax.js'

export default {
  data: () => {
    return {
      tags: null
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
  }
}
</script>
