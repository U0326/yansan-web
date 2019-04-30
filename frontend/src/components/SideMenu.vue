<template>
  <aside class="box menu">
    <p class="menu-label">タグ一覧</p>
    <div class="tags">
      <span class="tag" v-for="tag in tags" v-bind:key=tag.name>
        <router-link :to="{path: '/tag', query: {name: tag.name}}">
          {{tag.name + '(' + tag.frequency + ')'}}
        </router-link>
      </span>
    </div>
  </aside>
</template>

<script>
// TODO ajaxを用いて取得する様に修正する必要がある。
import tagDataJson from '../../static/test_resource/tag_data.json'

export default {
  data: () => {
    return {
      tags: tagDataJson.tags.sort((a, b) => a.frequency < b.frequency ? 1 : -1)
    }
  }
}
</script>
