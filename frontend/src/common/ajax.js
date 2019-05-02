import axios from 'axios'

const httpClient = axios.create({
  baseURL: process.env.AJAX_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest'
  },
  responseType: 'json'
})

export default httpClient
