<template>
  <div id="video_list">
    <p>
      {{videoListTitle}}
    </p>
    <p>
      全{{allVideoLength}}件中{{ videoLengthPerPage * (currentPage - 1) + 1}}〜
      {{videoLengthPerPage * (currentPage - 1) + showVideoList.length}}件表示
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
      :per-page="videoLengthPerPage"
      :total="allVideoLength"
      :current.sync="currentPage" />
  </div>
</template>

<script>
import videoListTaker from '@/components/videoList/videoListTaker.js'
const VIDEO_LENGTH_PER_PAGE = 7

export default {
  mixins: [videoListTaker],
  data: () => {
    return {
      allVideoLength: null,
      showVideoList: null,
      currentPage: null,
      videoLengthPerPage: VIDEO_LENGTH_PER_PAGE
    }
  },
  computed: {
    allVideoList () {
      return this.$store.getters['videoList/allVideoList']
    }
  },
  watch: {
    allVideoList (newValue) {
      this.allVideoLength = newValue.length
      this.currentPage = 1
      this.updateShowVideoList(this.currentPage)
    },
    showVideoList: function () {
      // showVideoListの描画前にスクロールを行うと、トップに戻れないケースがある為、以下の通り対応する。
      this.$nextTick(function () {
        window.scrollTo({top: 0, behavior: 'smooth'})
      })
    },
    currentPage: function (newValue) {
      this.updateShowVideoList(newValue)
    }
  },
  created: function () {
    this.updateShowVideoList(1)
  },
  methods: {
    updateShowVideoList: function (currentPage) {
      let start = this.videoLengthPerPage * (currentPage - 1)
      let end = 0
      if (this.allVideoList.length < this.videoLengthPerPage * currentPage) {
        end = this.allVideoList.length
      } else {
        end = this.videoLengthPerPage * currentPage
      }
      this.showVideoList = this.allVideoList.slice(start, end)
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
