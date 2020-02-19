'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  AJAX_BASE_URL: '"http://0.0.0.0:5000"'
})
