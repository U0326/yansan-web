<template>
  <div id="video_list">
    <p>
      <span v-if=!$route.query.name>ランダムピックアップ：</span>タグ「{{ tag }}」に該当する動画
    </p>
    <div class="box" v-for="info in showVideoList" v-bind:key=info.id>
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
    <b-pagination
      order="is-centered"
      aria-next-label="Next page"
      aria-previous-label="Previous page"
      aria-page-label="Page"
      aria-current-label="Current page"
      :per-page="perPage"
      :total="total"
      :current.sync="currentPage" />
  </div>
</template>

<script>
import httpClient from '@/common/ajax.js'
const PER_PAGE = 7

export default {
  data: () => {
    return {
      tag: null,
      allVideoList: null,
      showVideoList: null,
      perPage: PER_PAGE,
      total: null,
      currentPage: null
    }
  },
  computed: {
    redrawMonitoringTarget () {
      return [this.allVideoList, this.currentPage]
    }
  },
  watch: {
    '$route.query.name': function (newValue) {
      this.takeVideoList(newValue)
    },
    redrawMonitoringTarget: function (newValue) {
      let currentPage = newValue[1]
      let start = PER_PAGE * (currentPage - 1)
      let end = this.allVideoList.length < PER_PAGE * currentPage ? this.allVideoList.length : PER_PAGE * currentPage
      this.showVideoList = this.allVideoList.slice(start, end)
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
        this.allVideoList = list
        this.tag = response.data.searchTag
        this.total = list.length
        this.currentPage = 1
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
