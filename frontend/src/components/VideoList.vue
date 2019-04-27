<template>
  <div id="video_list">
    <p>{{ $route.query.name }}</p>
      <div v-for="info in videoList" v-bind:key=info.id>
        <p>タイトル:{{info.title}}</p>
        <p>公開日時:{{
              info.publishedAt.getFullYear() +
              '/' + (info.publishedAt.getMonth() + 1) +
              '/' + info.publishedAt.getDate()
           }}
        </p>
        <p>タグ:
          <router-link v-for="tag in info.tags" v-bind:key=tag :to="{path: '/tag', query: {name: tag}}">
            {{tag}}
          </router-link>
        </p>
        <iframe
            width="560"
            height="315"
            :src="'https://www.youtube.com/embed/' + info.id"
            frameborder="0"
            allow="autoplay;
            encrypted-media"
            allowfullscreen />
      </div>
  </div>
</template>

<script>
// TODO ajaxを用いて取得する様に修正する必要がある。
import videoListJson from '../../static/test_resource/video_list.json'

export default {
  computed: {
    videoList: () => {
      let videoList = videoListJson.videoList.sort(
        (a, b) => new Date(a.publishedAt) < new Date(b.publishedAt) ? -1 : 1)
      videoList.forEach(element => { element.publishedAt = new Date(element.publishedAt) })
      return videoList
    }
  }
}
</script>
