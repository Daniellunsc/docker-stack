const proxy = require('http-proxy-middleware')
    
module.exports = function(app) {
  app.use(proxy('/api', {target: 'http://172.18.0.3:5000'}))
}