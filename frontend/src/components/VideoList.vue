<template>
  <div id="video_list">
    <p>
      <span v-if=!$route.query.name>ランダムピックアップ：</span>タグ「{{ tag }}」に該当する動画
    </p>
    <div class="box" v-for="info in videoList" v-bind:key=info.id>
      <p>{{
            info.published_at.getFullYear() +
            '/' + (info.published_at.getMonth() + 1) +
            '/' + info.published_at.getDate()
         }}
      </p>
      <p>{{info.title}}</p>
      <div class="tags">
        <div class="tag" v-for="tag in info.tags" v-bind:key=tag>
          <router-link :to="{path: '/tag', query: {name: tag}}">
            {{tag}}
          </router-link>
        </div>
      </div>
      <div class="youtube-video">
        <iframe
            :src="'https://www.youtube.com/embed/' + info.id"
            frameborder="0"
            allow="autoplay;
            encrypted-media"
            allowfullscreen />
      </div>
    </div>
  </div>
</template>

<script>
import httpClient from '@/common/ajax.js'

export default {
  data: () => {
    return {
      tag: null,
      videoList: null
    }
  },
  watch: {
    '$route.query.name': function (newValue) {
      this.takeVideoList(newValue)
    }
  },
  mounted: function () {
    this.takeVideoList()
  },
  methods: {
    takeVideoList: function (query) {
      let path = '/api/video-list'
      if (query) {
        path += '?name=' + query
      }
      httpClient.get(path).then(response => {
        let list = response.data.videoList
        list.forEach(element => { element.published_at = new Date(element.published_at) })
        this.videoList = list
        this.tag = response.data.searchTag
      })
    }
  }
}
</script>

<style scoped lang="sass">
  .tags
    margin-top: 1rem
    margin-bottom: 0

  .youtube-video
    position: relative
    width: 100%
    padding-top: 56.25%

    iframe
      position: absolute
      top: 0
      right: 0
      width: 100% !important
      height: 100% !important
</style>
