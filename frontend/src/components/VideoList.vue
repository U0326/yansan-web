<template>
  <div id="video_list">
    <p>
      <span v-if=!$route.query.name>ランダムピックアップ：</span>タグ「{{ tag }}」に該当する動画
    </p>
    <div class="box" v-for="info in videoList" v-bind:key=info.id>
      <p>{{info.title}}</p>
      <p>{{
            info.publishedAt.getFullYear() +
            '/' + (info.publishedAt.getMonth() + 1) +
            '/' + info.publishedAt.getDate()
         }}
      </p>
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
// TODO ajaxを用いて取得する様に修正する必要がある。
import videoListJson from '../../static/test_resource/video_list.json'

export default {
  computed: {
    tag: function () {
      return videoListJson.searchTag
    },
    videoList: function () {
      let videoList = videoListJson.videoList.sort(
        (a, b) => new Date(a.publishedAt) < new Date(b.publishedAt) ? -1 : 1)
      videoList.forEach(element => { element.publishedAt = new Date(element.publishedAt) })
      return videoList
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
