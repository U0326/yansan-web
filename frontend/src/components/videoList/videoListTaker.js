import httpClient from '@/common/ajax.js'

export default {
  data: () => {
    return {
      videoListTitle: null
    }
  },
  computed: {
    allVideoList () {
      return this.$store.getters['videoList/allVideoList']
    }
  },
  created: function () {
    this.takeVideoListByQuery()
  },
  watch: {
    '$route.query.name': function (newValue) {
      this.takeVideoListByQuery(newValue)
    }
  },
  methods: {
    takeVideoListByQuery: function (query) {
      let path = '/api/video-list'
      if (query) {
        path += '?name=' + query
      }
      httpClient.get(path).then(response => {
        let list = response.data.videoList
        list.forEach(element => { element.published_at = new Date(element.published_at) })
        this.$store.commit('videoList/mutationAllVideoList', list)
        this.videoListTitle = 'タグ「' + response.data.searchTag + '」に該当する動画'
        // ランダムにタグを取得した際に、表示するタグとURIの不整合を以下の通り防ぐ。
        this.$router.push({path: '/tag', query: {name: response.data.searchTag}})
      })
    }
  }
}
